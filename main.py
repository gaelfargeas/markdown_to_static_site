import argparse
from pathlib import Path
import markdown2
import jinja2
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Chemin du/des source.", type=str)

parser.add_argument("-o", help="Chemin du dossier des fichiers générés.", type=str)

parser.add_argument("-t", help="Chemin du dossier des fichiers modeles.", type=str)

parser.add_argument(
    "-s", help="type de sources (fichier ou dossier).", action="store_true"
)

parser.add_argument("-v", "--verbose", help="Verbose mode.", action="store_true")
args = parser.parse_args()
VERBOSE = args.verbose

if VERBOSE:
    print("input :", args.i)
    print("output :", args.o)
    print("template:", args.t)
    print("type input", args.s)


def add_image(html_test):
    # dans le output file crée un dossier src
    src_path = Path(args.o + "/src")
    if not os.path.exists(src_path):
        os.makedirs(src_path)

    # get le path du dossier input
    if args.s:
        input_path = os.path(args.i)
    else:
        input_path = os.path.dirname(args.i)

    # parse le html , cp chaque image dans scr et modif le link
    result_string = ""
    for line in html_test.split("\n"):

        line = str(line)
        if "<img " in line:
            # get image
            image_path = line.split('src="')[1].split('" ')[0]
            if VERBOSE:
                print("image_path", image_path)

            image_name = image_path.split("/")[-1].split("\\")[-1]
            if VERBOSE:
                print("image_name", image_name)

            shutil.copyfile(
                str(input_path) + "/" + image_path, str(src_path) + "/" + image_name
            )

            line = (
                line.split('src="')[0]
                + 'src="./src/'
                + image_name
                + '" '
                + line.split('src="')[-1].split('" ')[-1]
            )
            result_string += line + "\n"

        else:
            result_string += line + "\n"

    return result_string


if __name__ == "__main__":
    if args.s:
        if args.i != None and args.o != None:

            with Path(args.i) as directory:
                for file in list(directory.glob("*_main.md")):

                    config_dict = {}
                    with open(file, "r") as input_file:
                        if VERBOSE:
                            print("intput file :", input_file.name)

                        file_name = (
                            input_file.name.split(".")[-2]
                            .split("/")[-1]
                            .split("\\")[-1]
                            .split("_main")[0]
                        )
                        with open(
                            str(args.o) + "/" + str(file_name) + ".html", "w"
                        ) as output_file:

                            if VERBOSE:
                                print("output file :", output_file.name)

                            html = markdown2.markdown(input_file.read())
                            config_dict["main"] = html

                            if args.t != None:

                                for config_file in list(
                                    directory.glob(file_name + "*.md")
                                ):

                                    config_name = (
                                        config_file.name.split(".")[-2]
                                        .split(file_name + "_")[-1]
                                        .lower()
                                    )
                                    if config_name != "main":
                                        with open(config_file, "r") as open_config_file:
                                            config_dict[
                                                config_name
                                            ] = open_config_file.read()

                                with open(args.t) as template_file:
                                    resutl = jinja2.Template(
                                        template_file.read()
                                    ).render(config_dict)
                            else:
                                resutl = html

                            if VERBOSE:
                                print("template file :", args.t)

                            output_file.write(resutl)

    else:

        if args.i != None and args.o != None:

            config_dict = {}
            with open(args.i, "r") as input_file:
                if VERBOSE:
                    print("intput file :", input_file.name)

                file_name = (
                    input_file.name.split(".")[-2]
                    .split("/")[-1]
                    .split("\\")[-1]
                    .split("_main")[0]
                )

                with open(
                    str(args.o) + "/" + str(file_name) + ".html", "w"
                ) as output_file:

                    if VERBOSE:
                        print("output file :", output_file.name)

                    html = markdown2.markdown(input_file.read())
                    config_dict["main"] = html

                    if args.t != None:
                        path_directory = args.i.split(file_name + "_main.md")[0]
                        with Path(path_directory) as directory:
                            # recupe le dossier ou est le fichier
                            for config_file in list(directory.glob(file_name + "*.md")):

                                config_name = (
                                    config_file.name.split(".")[-2]
                                    .split(file_name + "_")[-1]
                                    .lower()
                                )

                                if config_name != "main":
                                    with open(config_file, "r") as open_config_file:
                                        config_dict[
                                            config_name
                                        ] = open_config_file.read()

                        with open(args.t) as template_file:
                            resutl = jinja2.Template(template_file.read()).render(
                                config_dict
                            )
                    else:
                        resutl = html

                    if VERBOSE:
                        print("template file :", args.t)

                    resutl = add_image(resutl)
                    output_file.write(resutl)

