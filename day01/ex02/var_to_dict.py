def convert_for_dict():
    my_dir = dict()
    d = [('Hendrix' , '1942'), ('Allman' , '1946'), ('King' , '1925'),
        ('Clapton' , '1945'), ('Johnson' , '1911'), ('Berry' , '1926'),
        ('Vaughan' , '1954'), ('Cooder' , '1947'), ('Page' , '1944'),
        ('Richards' , '1943'), ('Hammett' , '1962'), ('Cobain' , '1967'),
        ('Garcia' , '1942'), ('Beck' , '1944'), ('Santana' , '1947'),
        ('Ramone' , '1948'), ('White' , '1975'), ('Frusciante', '1970'),
        ('Thompson' , '1949'), ('Burton' , '1939')]
    for value, key in d:
        try:
            my_dir[key] = my_dir[key] + ' ' + value
        except:
            my_dir[key] = value
    for key in my_dir:
        print("{key} : {value}".format(key = key, value = my_dir[key]))

if __name__ == '__main__':
    convert_for_dict()
