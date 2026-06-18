import sys


def find_state():
    """ Takes a capital as parameter and print assosiated country
        else return or print error if missing argv[1]"""

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

    capital = sys.argv[1]

    #We first find the corresponding abbreviation then must find wich state
    #is the key for this abreviation, much slower than the previous exercise 
    #we see here that dict is good for key->value but bad for value->key
    for abbreviation in capital_cities:
        if capital_cities[abbreviation] == capital:
            for state in states:
                if states[state] == abbreviation:
                    print(state)
                    return

    print("Unknown capital city")


if __name__ == '__main__':
    find_state()