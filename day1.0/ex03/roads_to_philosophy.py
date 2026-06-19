import sys
import requests
from bs4 import BeautifulSoup


def make_url(search):
    """Turns terminal input into wikipedia url"""

    return "https://en.wikipedia.org/wiki/" + search.strip().replace(" ", "_")


def get_page(url):
    """Download HTML page, turn it into searchable python object, returns it"""

    headers = {"User-Agent": "DjangoPiscine (student project)"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Error: unable to reach Wikipedia.")

    return BeautifulSoup(response.text, "html.parser")


def get_title(soup):
    """ Find and return Title of the page"""

    title = soup.find("h1", id="firstHeading")
    if title is None:
        raise Exception("Error: page title not found.")
    return title.get_text()


def valid_link(href):
    """ Check if a link is valid or not"""

    return (
        href is not None
        and href.startswith("/wiki/")
        and ":" not in href
        and "#" not in href
    )


def get_first_link(soup):
    """ Check for link until a valid link is found or the page is finished"""

    content = soup.find("div", id="mw-content-text")
    if content is None:
        return None

    paragraphs = content.find_all("p", recursive=True)

    for paragraph in paragraphs:
        links = paragraph.find_all("a")
        for link in links:
            href = link.get("href")
            if valid_link(href):
                return "https://en.wikipedia.org" + href

    return None


def roads_to_philosophy():
    """ From arg.wiki try to find and print the title of the first link found
        go to this link and repeat until it reaches either a dead end, a loop
        or the philosophy page"""

    if len(sys.argv) != 2:
        raise Exception("Error: expected one search argument.")

    search = sys.argv[1].strip()
    if search == "":
        raise Exception("Error: empty search.")

    visited = []
    url = make_url(search)

    while True:
        soup = get_page(url)
        title = get_title(soup)

        if title in visited:
            print("It leads to an infinite loop !")
            return

        visited.append(title)
        print(title)

        if title.lower() == "philosophy":
            print(
                str(len(visited))
                + " roads from "
                + search
                + " to philosophy !"
            )
            return

        url = get_first_link(soup)

        if url is None:
            print("It's a dead end !")
            return


if __name__ == '__main__':
    try:
        roads_to_philosophy()
    except Exception as error:
        print(error)

#python3 -m venv venv
#source venv/bin/activate
#pip install -r requirement.txt
#python3 roads_to_philosophy.py "42 (number)"