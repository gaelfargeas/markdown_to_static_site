# Markdown_to_static_site

Convert markdown fils to html. Those html files can be used to create a static site.

## Prerequis :

Python +> 3.6

Install markdown2 and jinja2 :

Windows :

    python -m pip install markdown2

    python -m pip install jinja2

Linux :

    pip3 install markdown2

    pip3 install jinja2

## How to use :

### Get sources :

    git clone https://github.com/gaelfargeas/markdown_to_static_site.git

    cd markdown_to_static_site

### Generate html :

Windows :

    python interface.py

Linux :

    python3 interface.py

Or you can direcly use main.py :

    python or python3 main.py -i input_file/directory -o output_directory -t template_file

You can add -s if you want use directory as input and -v to activate verbose.

### Make an static site :

First rename the main html file to index.html.

#### local site :

You can use tools like Apache or Nginx . you can also use python.

Windows :

    python -m http.server 8080  --directory ./site_directory/

Linux :

    python3 -m http.server 8080  --directory ./site_directory/

To acces this static site use those link :

http://localhost:8080/ or http://your_ip:8080/

#### github site :

Create a new github repositorie , then create a new branch "gh-pages".

In a new folder :

    git clone --branch gh-pages repositorie_url

Add you html files :

    git add all_files_in_html_folder

Do not copy the folder, only copy files in it.

    git push

Then use https://your_login.github.io/repositorie_name/ link to watch you static site.


## WARNING :

Template isn't fully implemented and may dont work exactly as you need.

Do not use two different images with the same name.

Example :

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

## Project from :

https://github.com/vpoulailleau/site_statique


### Library used :

Markdown2 (https://github.com/trentm/python-markdown2 , license MIT)

jinja2 (https://github.com/pallets/jinja/tree/master/jinja2)