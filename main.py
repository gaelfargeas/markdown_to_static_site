import argparse
from pathlib import Path
import markdown2
import jinja2

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

                    output_file.write(resutl)

