def get_next_num():
    fd = open('numbers.txt')
    for num in fd.read().rstrip("\n").split(','):
        print(num)

if __name__ == '__main__':
    get_next_num()