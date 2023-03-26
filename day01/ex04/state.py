import sys

def find_state(av):
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

    for key in capital_cities:
        if capital_cities[key] == av:
            state = key
    try:
        for key in states:
            if states[key] == state:
                print(key)
    except:
        print("Unknown capital city")
        exit()
if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    find_state(sys.argv[1])