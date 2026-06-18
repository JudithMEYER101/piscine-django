import sys


def normalize(text):
    """Normalize text so sAlem and Salem works"""

    return text.strip().lower()


def find_state_from_code(states, code):
    """ Use code (abbreviation) to find  state like in previous ex"""

    for state in states:
        if states[state] == code:
            return state
    return None


def handle_expression(expr, states, capital_cities):
    """Normalize, strip, then check if expr matches either state or capital
        print result accodingly (capital->state, state->capital, neither)"""

    cleaned = expr.strip() # Removes spaces in front and back
    normalized = normalize(expr)

    for state in states:
        if normalize(state) == normalized:
            code = states[state]
            print(capital_cities[code], "is the capital of", state)
            return

    for code in capital_cities:
        if normalize(capital_cities[code]) == normalized:
            state = find_state_from_code(states, code)
            print(capital_cities[code], "is the capital of", state)
            return

    print(cleaned, "is neither a capital city nor a state")


def all_in():
    """ Takes a string as parameter, clean it then print every corresponding info
    state -> capital, capital->state"""

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

    expressions = sys.argv[1].split(",")

    for expr in expressions:
        if expr.strip() == "": #Get rid of empy expression
            continue
        handle_expression(expr, states, capital_cities)


if __name__ == '__main__':
    all_in()