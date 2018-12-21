# markdown_to_static_site

convert markdown static site

## bug :

code only work on windows because python3 is call by python in the command line interface.

## prerequis :

Python +> 3.6

## how to use :

git clone https://github.com/gaelfargeas/markdown_to_static_site.git

cd markdown_to_static_site

python3 interface.py

## WARNING :

template isn't fully implemented and may dont work.

## format :

your main file : name_main.md

### template :

in template you can call variables by :

    {{variable}}

#### example :

for your main file (name_main.md) the variable is is "main" :

    {{main}}

for your x file (name_x.md) the variable is is "x" :

    {{x}}    

## check before generate:

make sure there aren't any space or point in input/output path and file name( file : name.md not name.somethink.md)
make sure there aren't any "/" or "\\" in file name

project from :
https://github.com/vpoulailleau/site_statique


library used :

markdown2 ( https://github.com/trentm/python-markdown2 , license MIT)
