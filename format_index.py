import sys
import fileinput

file = 'dist/index.html'

with open(file, "r+") as f:
    s = f.read()
    f.seek(0)
    f.write("{% load staticfiles %}\n" + s)
    g = f.read()
 
# https://www.bworldonline.com/wp-content/uploads/2017/05/Smart-Padala-logo-FB.jpg


#starting tag

for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace('css/', "{% static 'css/"))   
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace('js/', "{% static 'js/"))


# for i, line in enumerate(fileinput.input(file, inplace=1)):
#     sys.stdout.write(line.replace('img/', "{% static 'img/"))

# for i, line in enumerate(fileinput.input(file, inplace=1)):
#     sys.stdout.write(line.replace('<link href=js/2d0e8be2.c7637194.js rel=prefetch><link href=js/2d22c0ff.693506dc.js rel=prefetch>', "<script src=\"{% static 'js/2d22c0ff.693506dc.js'%}\"></script><script src=\"{% static 'js/2d0e8be2.c7637194.js'%}\"></script>"))



#endtag
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace('.css', ".css' %}"))
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace('.js', ".js' %}"))

# for i, line in enumerate(fileinput.input(file, inplace=1)):
    # sys.stdout.write(line.replace('<body>', "<body>{% csrf_token %} <script charset=\"utf-8\" src=\"js/2d0e8be2.497e8aaf.js\"></script>  <script src=\"{% static 'js/2d22c0ff.693506dc.js'%}\"></script> <script src=\"{% static 'js/2d0e8be2.c7637194.js'%}\"></script>"))
# for i, line in enumerate(fileinput.input(file, inplace=1)):
#     sys.stdout.write(line.replace('.png', ".png' %}"))
# for i, line in enumerate(fileinput.input(file, inplace=1)):
#     sys.stdout.write(line.replace('.jpeg', ".jpeg' %}"))
# for i, line in enumerate(fileinput.input(file, inplace=1)):
#     sys.stdout.write(line.replace('.svg', ".svg' %}"))


 
    # <script src="{% static 'js/2d22c0ff.693506dc.js'%}"></script>
    # <script src="{% static 'js/2d0e8be2.c7637194.js'%}"></script>


    # <script charset="utf-8" src="js/2d0e8be2.497e8aaf.js"></script>
