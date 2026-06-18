import sys


def find_capital():
    """Takes an argument as input, if arg matches with one of the states
        print the capital, else print error or return if no argv[1]"""

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    state = sys.argv[1]

    if state in states:
        abbreviation = states[state]
        print(capital_cities[abbreviation])
    else:
        print("Unknown state")


if __name__ == '__main__':
    find_capital()