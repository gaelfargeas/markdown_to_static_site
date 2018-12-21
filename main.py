import argparse
from pathlib import Path
import markdown2
import jinja2

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Chemin du dossier des fichiers source.", type=str)

parser.add_argument("-o", help="Chemin du dossier des fichiers générés.", type=str)

parser.add_argument("-t", help="Chemin du dossier des fichiers modeles.", type=str)

parser.add_argument("-v", "--verbose", help="Verbose mode.", action="store_true")
args = parser.parse_args()
VERBOSE = args.verbose

if VERBOSE:
    print("input :", args.i)
    print("output :", args.o)
    print("template:", args.t)

if __name__ == "__main__":
    if args.i != None and args.o != None:

        with Path(args.i) as directory:
            for file in list(directory.glob("*.md")):

                with open(file, "r") as input_file:
                    if VERBOSE:
                        print("intput file :", input_file.name)

                    file_name = (
                        input_file.name.split(".")[0].split("/")[-1].split("\\")[-1]
                    )
                    with open(
                        str(args.o) + "/" + str(file_name) + ".html", "w"
                    ) as output_file:

                        if VERBOSE:
                            print("output file :", output_file.name)
                        html = markdown2.markdown(input_file.read())

                        if args.t != None:
                            with open(args.t) as template_file:
                                resutl = jinja2.Template(template_file.read()).render(
                                    content=html
                                )
                        else:
                            resutl = html

                        if VERBOSE:
                            print("template file :", args.t)

                        output_file.write(resutl)

