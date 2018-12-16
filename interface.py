import tkinter
import tkinter.filedialog as tkinter_fl
import os


class interface:
    def __init__(self):

        self.fenetre = tkinter.Tk()
        self.input_directory = tkinter.StringVar(value="./markdown/")
        self.output_directory = tkinter.StringVar(value="./html/")
        self.make_interface()

    def make_interface(self):
        main = tkinter.LabelFrame(
            self.fenetre, text="convert markdown to a static site", padx=20, pady=20
        )
        main.pack(fill="both", expand="yes")

        Frame_data = tkinter.Frame(
            main, borderwidth=10, relief=tkinter.constants.GROOVE
        )
        Frame_data.pack(padx=5, pady=5, side=tkinter.constants.TOP)

        Frame_input = tkinter.Frame(Frame_data, borderwidth=10)
        Frame_input.pack(padx=5, pady=5, side=tkinter.constants.LEFT)

        lb_input = tkinter.Label(Frame_input, text="input setting")
        lb_input.pack()

        tf_input = tkinter.Entry(Frame_input, textvariable=self.input_directory)
        tf_input.pack()

        bouton_input = tkinter.Button(
            Frame_input, text="select", command=lambda: self.directory_ask(ID="input")
        )
        bouton_input.pack(side=tkinter.constants.LEFT)

        Frame_output = tkinter.Frame(Frame_data, borderwidth=10)
        Frame_output.pack(padx=5, pady=5, side=tkinter.constants.RIGHT)

        lb_output = tkinter.Label(Frame_output, text="output setting")
        lb_output.pack()

        tf_output = tkinter.Entry(Frame_output, textvariable=self.output_directory)
        tf_output.pack()

        bouton_output = tkinter.Button(
            Frame_output, text="select", command=lambda: self.directory_ask(ID="output")
        )
        bouton_output.pack(side=tkinter.constants.LEFT)

        Frame_bp = tkinter.Frame(main, borderwidth=2)
        Frame_bp.pack(padx=5, pady=5, side=tkinter.constants.BOTTOM)

        bouton_generate = tkinter.Button(
            Frame_bp, text="generate", command=lambda: self.generate()
        )
        bouton_generate.pack(side=tkinter.constants.LEFT)

        bouton_exit = tkinter.Button(Frame_bp, text="Exit", command=self.fenetre.quit)
        bouton_exit.pack(side=tkinter.constants.RIGHT)

        self.fenetre.mainloop()

    def directory_ask(self, ID=""):
        if ID == "input":
            self.input_directory.set(
                tkinter_fl.askdirectory(title="selectioné un dossier")
            )

        elif ID == "output":
            self.output_directory.set(
                tkinter_fl.askdirectory(title="selectioné un dossier")
            )

        print("input", self.input_directory.get())
        print("output", self.output_directory.get())

    def generate(self):
        os.system(
            f"python ./main.py -v -i {self.input_directory.get()}  -o {self.output_directory.get()} "
        )


interf = interface()

