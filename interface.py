import tkinter
import tkinter.filedialog as tkinter_fl
import os

VERBOSE = True


class interface:
    def __init__(self):

        self.fenetre = tkinter.Tk()
        self.input_directory = tkinter.StringVar(value="./markdown/")
        self.output_directory = tkinter.StringVar(value="./html/")
        self.template_directory = tkinter.StringVar(value="./template/")
        self.use_template = tkinter.BooleanVar(value=False)
        self.type_input = tkinter.BooleanVar(value=False)
        self.make_interface()

    def make_interface(self):
        main = tkinter.LabelFrame(
            self.fenetre, text="convert markdown to a static site", padx=50, pady=50
        )
        main.pack(fill="both", expand="yes")

        Frame_data = tkinter.Frame(
            main, borderwidth=10, relief=tkinter.constants.GROOVE
        )
        Frame_data.pack(fill="both", expand=True, side=tkinter.constants.TOP)

        Frame_input = tkinter.Frame(Frame_data, borderwidth=10)
        Frame_input.pack(fill="both", expand=True)

        lb_input = tkinter.Label(Frame_input, text="input setting")
        lb_input.pack(fill="both", expand=True)

        tf_input = tkinter.Entry(Frame_input, textvariable=self.input_directory)
        tf_input.pack(fill="both", expand=True, side=tkinter.constants.LEFT)

        bouton_input = tkinter.Button(
            Frame_input, text="select", command=lambda: self.directory_ask(ID="input")
        )
        bouton_input.pack(side=tkinter.constants.RIGHT)

        Frame_output = tkinter.Frame(Frame_data, borderwidth=10)
        Frame_output.pack(fill="both", expand=True)

        lb_output = tkinter.Label(Frame_output, text="output setting")
        lb_output.pack(fill="both", expand=True)

        tf_output = tkinter.Entry(Frame_output, textvariable=self.output_directory)
        tf_output.pack(fill="both", expand=True, side=tkinter.constants.LEFT)

        bouton_output = tkinter.Button(
            Frame_output, text="select", command=lambda: self.directory_ask(ID="output")
        )
        bouton_output.pack(side=tkinter.constants.RIGHT)

        Frame_template = tkinter.Frame(Frame_data, borderwidth=10)
        Frame_template.pack(fill="both", expand=True)

        lb_template = tkinter.Label(Frame_template, text="template setting")
        lb_template.pack(fill="both", expand=True)

        tf_template = tkinter.Entry(
            Frame_template, textvariable=self.template_directory
        )
        tf_template.pack(fill="both", expand=True, side=tkinter.constants.LEFT)

        bouton_template = tkinter.Button(
            Frame_template,
            text="select",
            command=lambda: self.directory_ask(ID="template"),
        )
        bouton_template.pack(side=tkinter.constants.RIGHT)

        Frame_bp = tkinter.Frame(main, borderwidth=2)
        Frame_bp.pack(fill="both", expand=True, side=tkinter.constants.BOTTOM)

        bouton_generate = tkinter.Button(
            Frame_bp, text="generate", command=lambda: self.generate()
        )
        bouton_generate.pack(fill="both", expand=True, side=tkinter.constants.LEFT)

        bouton_exit = tkinter.Button(Frame_bp, text="Exit", command=self.fenetre.quit)
        bouton_exit.pack(fill="both", expand=True, side=tkinter.constants.RIGHT)

        Frame_opt = tkinter.Frame(main, borderwidth=2)
        Frame_opt.pack(fill="both", expand=True, side=tkinter.constants.BOTTOM)

        chkbp_use_template = tkinter.Checkbutton(
            Frame_opt, text="use template  ?", variable=self.use_template
        )
        chkbp_use_template.pack(fill="both", expand=True, side=tkinter.constants.BOTTOM)

        chkbp_type_input = tkinter.Checkbutton(
            Frame_opt, text="input is a folder ?", variable=self.type_input
        )
        chkbp_type_input.pack(fill="both", expand=True, side=tkinter.constants.BOTTOM)

        self.fenetre.mainloop()

    def directory_ask(self, ID=""):
        if ID == "input":
            print(self.type_input.get())
            if self.type_input.get():
                self.input_directory.set(
                    tkinter_fl.askdirectory(title="selectioné un dossier")
                )
            else:
                self.input_directory.set(
                    tkinter_fl.askopenfile(
                        mode="r",
                        title="selectioné un fichier",
                        filetypes=(
                            ("markdown files", "*main.md"),
                            ("all files", "*.*"),
                        ),
                    ).name
                )

        elif ID == "output":
            self.output_directory.set(
                tkinter_fl.askdirectory(title="selectioné un dossier")
            )
        elif ID == "template":
            self.template_directory.set(
                tkinter_fl.askopenfile(
                    mode="r",
                    title="selectioné un fichier",
                    filetypes=(("html files", "*.html"), ("all files", "*.*")),
                ).name
            )

        if VERBOSE:
            print("input", self.input_directory.get())
            print("output", self.output_directory.get())
            print("template", self.template_directory.get())

    def generate(self):
        if self.use_template.get():
            if VERBOSE:
                print("Generate with template")
                command = f"python ./main.py -v -i {self.input_directory.get()}  -o {self.output_directory.get()} -t {self.template_directory.get()}"
                if self.type_input.get():
                    command += "-s"

            os.system(command)
        else:
            if VERBOSE:
                print("Generate without template")
            command = f" python ./main.py -v -i {self.input_directory.get()}  -o {self.output_directory.get()}"
            if self.type_input.get():
                command += "-s"

            os.system(command)


interf = interface()

