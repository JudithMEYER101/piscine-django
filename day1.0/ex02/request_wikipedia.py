import sys
import requests
import json
import dewiki


#Request id for wikipedia
HEADERS = {
    "User-Agent": "DjangoPiscine (student project)"
}

def build_filename(search):
    """ Create filename search.wiki"""

    return search.strip().replace(" ", "_") + ".wiki"


def search_wikipedia(query):
    """ Connect to API endspoint and search for best match to query"""

    url = "https://fr.wikipedia.org/w/api.php"  #endpoint

    #Query parameters
    params = {
        "action": "query",
        "list": "search", #search for article
        "srsearch": query,  #search term (ex: chocolatine)
        "format": "json",   #Return format
        "utf8": 1
    }

    #request query with our url(wikipedia) parameters and headers(id)
    response = requests.get(url, params=params, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Error: server problem")

    #Turns string into dict
    data = json.loads(response.text)

    if "query" not in data or len(data["query"]["search"]) == 0:
        raise Exception("Error: no result found")

    #return best matching article title
    return data["query"]["search"][0]["title"]


def get_page_content(title):
    """ Get the page content of "title" through a query and returns it"""

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvprop": "content",
        "rvslots": "main",
        "format": "json",
        "utf8": 1
    }

    response = requests.get(url, params=params, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Error: server problem")

    data = json.loads(response.text)
    pages = data["query"]["pages"]

    #Searching for our pages id in wikipedia ID-Keyed dictionary
    for page_id in pages:
        page = pages[page_id]

        if "missing" in page:
            raise Exception("Error: page not found")

        return page["revisions"][0]["slots"]["main"]["*"] #Extract raw wiki page

    raise Exception("Error: no content found")


def write_result(query, content):
    """ Build filename, create file, fill it with dewikified content"""

    filename = build_filename(query)
    cleaned = dewiki.from_string(content)   #make wiki format into a readable text

    file = open(filename, "w")
    file.write(cleaned)
    file.close()


def request_wikipedia():
    """ Get user input, search wikipedia API, get best match, fetch raw article
        clean wiki markup, save to file.wiki"""

    if len(sys.argv) != 2:
        raise Exception("Error: expected one search argument")

    query = sys.argv[1].strip()

    if query == "":
        raise Exception("Error: empty search")

    title = search_wikipedia(query)
    content = get_page_content(title)
    write_result(query, content)


if __name__ == '__main__':
    try:
        request_wikipedia()
    except Exception as error:
        print(error)

#python3 -m venv venv
#source venv/bin/activate
#pip install -r requirement.txt
#python3 request_wikipedia.py "chocolatine"