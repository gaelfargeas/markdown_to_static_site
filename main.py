import argparse
from pathlib import Path
import markdown2

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
                print(file)

                with open(file, "r") as input_file:
                    print("intput file :", input_file.name)

                    with open(
                        str(args.o)
                        + "/"
                        + input_file.name.split("\\")[1].split(".")[0]
                        + ".html",
                        "w",
                    ) as output_file:

                        print("output file :", output_file.name)
                        output_file.write(markdown2.markdown(input_file.read()))

