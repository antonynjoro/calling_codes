"""Tkinter UI for the Nato Alphabet program."""
import tkinter as tk
import pandas

class NatoUI(tk.Tk):
    """Tkinter UI for the Nato Alphabet program."""

    def __init__(self, master=None):
        """Initialize the UI."""
        super().__init__(master)
        self.letter_data = pandas.read_csv('nato_phonetic_alphabet.csv')
        self.dictionary = {data['letter']: data['code'] for (index, data) in self.letter_data.iterrows()}
        self.title("Nato Alphabet")
        self.geometry("400x400")
        self.config(padx=20, pady=20)
        self.prompt = tk.Label(self, text="Enter a word to convert to Nato Alphabet", font=("Arial", 16, "bold"), wraplength=300, justify="center")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Convert", command=self.generate_phonetic)
        self.result = tk.Label(self, text="", wraplength=300, justify="center")
    #     Pack all the widgets in the vertical center of the window.
        self.prompt.pack()
        self.entry.pack(pady=20)
        self.button.pack()
        self.result.pack(pady=20, fill="both", expand=True)
        self.mainloop()

    def generate_phonetic(self):
        """Convert the word to Nato Alphabet."""
        name = self.entry.get()
        try:
            code_name = [self.dictionary[letter.upper()] + " " for letter in name]
            code_name_string = "".join(code_name)
            self.result.config(text=f"Your Code Name is: {code_name_string}")
        except KeyError:
            self.result.config(text="Please only use letters in the alphabet.")



