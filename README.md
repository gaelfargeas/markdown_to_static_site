# markdown_to_static_site

convert markdown static site

## prerequis :

Python +> 3.6

## how to use :

git clone https://github.com/gaelfargeas/markdown_to_static_site.git

cd markdown_to_static_site

python3 interface.py

## WARNING :

template isn't fully implemented and may dont work.

curently, convert 1 markdown file into 1 html file. 
is template is used : the whole markdown file is use as "content" in template.

in template use :

    <div class="container">
    {{content}}
    </div>

## check before generate:

make sure there aren't any space or point in input/output path and file name( file : name.md not name.somethink.md)
make sure there aren't any "/" or "\\" in file name

project from :
https://github.com/vpoulailleau/site_statique


library used :

markdown2 ( https://github.com/trentm/python-markdown2 , license MIT)
