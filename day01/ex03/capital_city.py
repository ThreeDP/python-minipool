import sys

def find_capital(av):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    try:
        print(capital_cities[states[av]])
    except:
        print("Unknown state")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    find_capital(sys.argv[1])