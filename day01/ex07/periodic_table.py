def print_td(key, values, fd, i):
    while i != int(values['position']):
        fd.write('\
                    <td class="col hide">\n \
                    </td>\n')
        i += 1
    td =    '\
                    <td class="col">\n \
                        <div class="col-content">\n \
                            <ul class="list">\n \
                                <li class="number">{num}</li>\n \
                                <li><h1 class="symbol">{symbol}</h1></li>\n \
                                <li><h4 class="name">{name}</h4></li>\n \
                                <li>{molar}</li>\n \
                                <li>{elec}<br>electron</li>\n \
                            </ul>\n \
                        </div>\n \
                    </td>\n'
    fd.write(td.format(name = key, num = values['number'], \
        symbol = values['small'], molar = values['molar'], \
        elec = values['electron']))
    return i

def get_info():
    fd = open('periodic_table.txt', 'r').read()
    d = dict()
    for line in fd.split('\n'):
        if len(line) <= 0:
            continue
        piece = line.split('=')
        d2 = dict()
        for items in piece[1].split(','):
            item = items.split(':')
            d2[item[0].rstrip(' ').strip(' ')] = item[1].rstrip(' ').strip(' ')
        d[piece[0].rstrip(' ').strip(' ')] = d2
    return d

def print_init(fd):
    head = '\
<!DOCTYPE html>\n \
<html lang="en">\n \
    <head>\n \
        <meta charset="UTF-8">\n \
        <title>Periodic table</title>\n \
        <style>\n \
             * {\n \
                 margin:0; padding:0;\n \
                 box-sizing: border-box;\n \
             }\n \
\n \
             .container {\n \
                 background-color: grey;\n \
                 width: 100%;\n \
             }\n \
\n \
             table, th, .col-content, td, tr {\n \
                 border-collapse: collapse;\n \
             }\n \
\n \
             .periodic-table {\n \
                 margin: 100px auto;\n \
                 width: 1800px;\n \
                 background: rgb(0,0,0);\n \
                 background: linear-gradient(120deg, rgba(0,0,0,1) 0%, rgba(18,18,18,1) 40%, rgba(43,43,43,1) 100%);\n \
                 border-collapse: collapse;\n \
             }\n \
\n \
             .symbol {\n \
                 font-size: 25px;\n \
                 color: white;\n \
             }\n \
\n \
             tbody {\n \
                 margin: 0 auto;\n \
             }\n \
\n \
             .col {\n \
                 background: rgb(0,0,0);\n \
                 background: linear-gradient(120deg, rgba(0,0,0,1) 0%, rgba(18,18,18,1) 40%, rgba(43,43,43,1) 100%);\n \
                 min-width: 100px;\n \
                 max-width: 100px;\n \
                 min-height: 10px;\n \
                 max-height: 10px;\n \
                 border: white solid 5px;\n \
                 text-align: center;\n \
             }\n \
\n \
             .col:hover {\n \
                 background: white;\n \
             }\n \
\n \
             .col:hover .symbol, .col:hover .name, .col:hover .list {\n \
                 color: black;\n \
             }\n \
\n \
             .col-content {\n \
                 width: 80%;\n \
                 margin: 0 auto;\n \
                 padding-top: 5px;\n \
                 padding-bottom: 10px;\n \
             }\n \
\n \
             .number {\n \
                 text-align: left;\n \
                 padding-top: 4px;\n \
             }\n \
\n \
             .name {\n \
                 color: white;\n \
                 font-size: 0.6rem;\n \
                 text-align: center;\n \
             }\n \
\n \
             .list {\n \
                 font-size: 10px;\n \
                 color: white;\n \
                 list-style: none;\n \
                 padding: 0;\n \
                 margin: 0 auto;\n \
             }\n \
\n \
             .col.hide {\n \
                border: none;\n \
                background: transparent;\n \
             }\n \
        </style>\n \
    </head>\n \
    <body class="container">\n \
        <table class="periodic-table">\n \
            <tbody>\n'
    fd.write(head)

def print_end(fd):
    end = '\
            </tbody>\n \
        </table>\n \
    </body>\n \
</html>\n'
    fd.write(end)


if __name__ == '__main__':
    d = get_info()
    fd = open('periodic_table.html', 'w')
    print_init(fd)
    i = 0
    for key in d:
        if i == 0:
            fd.write('\
                <tr class="row">\n')
        i = print_td(key, d[key], fd, i)
        if i == 17:
            fd.write('\
                </tr>\n')
            i = 0
        else:
            i += 1
    print_end(fd)
