def my_var():
    for item in [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]:
        print("{0} has a type {1}".format(item, type(item)))

if __name__ == '__main__':
    my_var()
