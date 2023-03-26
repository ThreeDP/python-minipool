import  sys

def find_state(i , ts, capital):
    for key, value in ts:
            if key == i.title():
                print('{0} is the capital of {1}'.format(capital[value], key))
                return True
    return False

def find_capital(i , tc, ts):
    for key, value in tc:
        if value == i.title():
            for key_s, value_s in ts:
                if key == value_s:
                    print('{0} is the capital of {1}'.format(value, key_s))
                    return True
    return False

def print_info(av, ls, capital_cities, states):
    for i in ls:
        if len(i) <= 0:
            continue
        if find_state(i, list(states.items()), capital_cities):
            continue
        if find_capital(i, list(capital_cities.items()), list(states.items())):
            continue
        print('{0} is neither a capital city nor a state'.format(i))

def define_dicts(av):
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
    ls = [i.rstrip(' ').strip(' ') for i in av.split(',')]
    for i in range(len(ls)):
        while '  ' in ls[i]:
            ls[i] = ls[i].replace('  ', ' ')
    print_info(av, ls, capital_cities, states)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    define_dicts(sys.argv[1])