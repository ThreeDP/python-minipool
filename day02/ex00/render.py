import sys, os, re

def print_html(template, infos, html):
    for key, value in list(infos.items()):
        try:
            template = re.sub("{" + key + "}", value, template)
        except:
            continue
    html.write(template)
     
if __name__ == '__main__':
    if (len(sys.argv) != 2 or not sys.argv[1].endswith(".template")):
       exit()
    if (not os.path.isfile("./" + sys.argv[1])):
        exit()
    if (not os.path.isfile("./" + "settings.py")):
        exit()
    file_html = sys.argv[1].replace(".template", ".html")
    exec(open("settings.py").read())
    infos = globals()
    html = open(file_html, "w")
    template = open(sys.argv[1]).read()
    print_html(template, infos, html)