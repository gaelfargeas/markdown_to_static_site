# Markdown_to_static_site

convert markdown to a static site

## Prerequis :

Python +> 3.6

Install markdown2 and jinja2 :

windows :

    python -m pip install markdown2

    python -m pip install jinja2

linux

    pip3 install markdown2

    pip3 install jinja2

## How to use :

    git clone https://github.com/gaelfargeas/markdown_to_static_site.git

    cd markdown_to_static_site

    python3 interface.py

## WARNING :

Template isn't fully implemented and may dont work.

Do not use two different images with the same name.

example :

    dir_a/test.png

and 

    dir_b/test.png

## Format :

Your main file : name_main.md

### Template :

In template you can call variables by :

    {{variable}}

#### Example :

For your main file (name_main.md) the variable is is "main" :

    {{main}}

For your x file (name_x.md) the variable is is "x" :

    {{x}}    

## Check before generate:

Make sure there aren't any space or point in input/output path and file name( file : name.md not name.somethink.md)
Make sure there aren't any "/" or "\\" in file name

Project from :
https://github.com/vpoulailleau/site_statique


Library used :

Markdown2 (https://github.com/trentm/python-markdown2 , license MIT)

jinja2 (https://github.com/pallets/jinja/tree/master/jinja2)