import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import sympy

class PasswordChecker:
    def __init__(self):
        self.spice_girls = ["Melanie Brown", "Melanie Chisholm", "Emma Bunton", "Geri Halliwell", "Victoria Beckham"]
        self.requirements = self.define_requirements()

    def define_requirements(self):
        return [
          ("Minimum length of 10 characters", lambda p: len(p) >= 10),
            ("Password must contain an Upper case letter", lambda p: any(c.isupper() for c in p)),
            ("Password must contain a Lower case letter", lambda p: any(c.islower() for c in p)),
            ("Password must contain a number", lambda p: any(c.isdigit() for c in p)),
            ("Password must contain a Special character", lambda p: any(c in "!@#$%^&*()_+" for c in p)),
            ("Password must contain the Morse code for 'hello'", lambda p: ".... . .-.. .-.. ---" in p),
            ("Password must contain the element symbols for Gold, Platinum, and Sodium", lambda p: all(x in p for x in ["Au", "Pt", "Na"])),
            ("Password must contain 3 even numbers", lambda p: sum(1 for c in p if c.isdigit() and int(c) % 2 == 0) >= 3),
            ("Password must add up to 80", lambda p: sum(int(c) for c in p if c.isdigit()) == 80),
            ("Password must start with a vowel", lambda p: p[0].lower() in "aeiou"),
            ("Password must contain a month of the year", lambda p: any(month in p for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])),
            ("Password must contain 3 odd numbers, descending", lambda p: any(p[i:i+3] in "97531" for i in range(len(p)-2))),
            ("Password must contain the Greek symbol delta", lambda p: "Δ" in p),
            ("Password must contain the Value for x when, 3x+2y-7 = 4x - y + 5", lambda p: "3y-12" in p),
            ("Password must not contain the letter 'S'", lambda p: "S" not in p.upper()),
            ("Password must contain the Hex code for RGB(255, 0, 68)", lambda p: "#FF0044" in p),
            ("Password must include the 9th prime number at the end of your password.", lambda p: p.endswith(str(sympy.prime(9)))),
            ("Password must contain a leap year from the 1817-1831 range.", lambda p: any(year in p for year in ["1820", "1824", "1828"])),
            ("Password must include the current prime number of the month.", lambda p: str(sympy.prime(datetime.datetime.now().month)) in p),
            ("Password must include one of the spice girls.", self.spice_girls_included)
        ]

    def spice_girls_included(self, p):
        return any(spice_girl in p for spice_girl in self.spice_girls)

    def check_requirements(self, p):
        passed = []
        current_requirement = None
        for text, check in self.requirements:
            try:
                if check(p):
                    passed.append(text)
                elif current_requirement is None:
                    current_requirement = text
            except Exception as e:
                print(f"Error checking requirement '{text}': {e}")
        return passed, current_requirement

class SimpleCalculator:
    def __init__(self, parent, password_entry):
        self.entry = tk.Entry(parent)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.password_entry = password_entry 
        buttons = [
            ('5', 1), ('8', 1), ('3', 1), ('/', 1),
            ('0', 2), ('7', 2), ('+', 2), ('*', 2),
            ('1', 3), ('2', 3), ('9', 3), ('-', 3),
            ('4', 4), ('C', 4), ('=', 4), ('6', 4),
        ]
        for (text, row) in buttons:
            tk.Button(parent, text=text, command=lambda text=text: self.on_button_click(text)).grid(row=row, column=buttons.index((text, row)) % 4)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.password_entry.insert(tk.END, result)  # Append results
            except Exception:
                self.entry.insert(tk.END, " (error)")
        else:
            self.entry.insert(tk.END, char)
            self.password_entry.insert(tk.END, char)  # Append character 

class PeriodicTableDisplay:
    def __init__(self, parent):
        elements = [
             ("Hydrogen", "H", 1.008), ("Helium", "He", 4.0026),
    ("Lithium", "Li", 6.94), ("Beryllium", "Be", 9.0122),
    ("Boron", "B", 10.81), ("Carbon", "C", 12.011),
    ("Nitrogen", "N", 14.007), ("Oxygen", "O", 15.999),
    ("Fluorine", "F", 18.998), ("Neon", "Ne", 20.1797),
    ("Sodium", "Na", 22.989), ("Magnesium", "Mg", 24.305),
    ("Aluminum", "Al", 26.982), ("Silicon", "Si", 28.085),
    ("Phosphorus", "P", 30.974), ("Sulfur", "S", 32.06),
    ("Chlorine", "Cl", 35.45), ("Argon", "Ar", 39.948),
    ("Potassium", "K", 39.098), ("Calcium", "Ca", 40.078),
    ("Scandium", "Sc", 44.956), ("Titanium", "Ti", 47.867),
    ("Vanadium", "V", 50.942), ("Chromium", "Cr", 51.996),
    ("Manganese", "Mn", 54.938), ("Iron", "Fe", 55.845),
    ("Cobalt", "Co", 58.933), ("Nickel", "Ni", 58.693),
    ("Copper", "Cu", 63.546), ("Zinc", "Zn", 65.38),
    ("Gallium", "Ga", 69.723), ("Germanium", "Ge", 72.63),
    ("Arsenic", "As", 74.922), ("Selenium", "Se", 78.971),
    ("Bromine", "Br", 79.904), ("Krypton", "Kr", 83.798),
    ("Rubidium", "Rb", 85.468), ("Strontium", "Sr", 87.62),
    ("Yttrium", "Y", 88.906), ("Zirconium", "Zr", 91.224),
    ("Niobium", "Nb", 92.906), ("Molybdenum", "Mo", 95.95),
    ("Technetium", "Tc", 98), ("Ruthenium", "Ru", 101.07),
    ("Rhodium", "Rh", 102.91), ("Palladium", "Pd", 106.42),
    ("Silver", "Ag", 107.87), ("Cadmium", "Cd", 112.41),
    ("Indium", "In", 114.82), ("Tin", "Sn", 118.71),
    ("Antimony", "Sb", 121.76), ("Tellurium", "Te", 127.6),
    ("Iodine", "I", 126.9), ("Xenon", "Xe", 131.29),
    ("Cesium", "Cs", 132.91), ("Barium", "Ba", 137.33),
    ("Lanthanum", "La", 138.91), ("Cerium", "Ce", 140.12),
    ("Praseodymium", "Pr", 140.91), ("Neodymium", "Nd", 144.24),
    ("Promethium", "Pm", 145), ("Samarium", "Sm", 150.36),
    ("Europium", "Eu", 151.96), ("Gadolinium", "Gd", 157.25),
    ("Terbium", "Tb", 158.93), ("Dysprosium", "Dy", 162.5),
    ("Holmium", "Ho", 164.93), ("Erbium", "Er", 167.26),
    ("Thulium", "Tm", 168.93), ("Ytterbium", "Yb", 173.05),
    ("Lutetium", "Lu", 174.97), ("Hafnium", "Hf", 178.49),
    ("Tantalum", "Ta", 180.95), ("Tungsten", "W", 183.84),
    ("Rhenium", "Re", 186.21), ("Osmium", "Os", 190.23),
    ("Iridium", "Ir", 192.22), ("Platinum", "Pt", 195.08),
    ("Gold", "Au", 196.97), ("Mercury", "Hg", 200.59),
    ("Thallium", "Tl", 204.38), ("Lead", "Pb", 207.2),
    ("Bismuth", "Bi", 208.98), ("Polonium", "Po", 209),
    ("Astatine", "At", 210), ("Radon", "Rn", 222),
    ("Francium", "Fr", 223), ("Radium", "Ra", 226),
    ("Actinium", "Ac", 227), ("Thorium", "Th", 232.04),
    ("Protactinium", "Pa", 231.04), ("Uranium", "U", 238.03),
    ("Neptunium", "Np", 237), ("Plutonium", "Pu", 244),
    ("Americium", "Am", 243), ("Curium", "Cm", 247),
    ("Berkelium", "Bk", 247), ("Californium", "Cf", 251),
    ("Einsteinium", "Es", 252), ("Fermium", "Fm", 257),
    ("Mendelevium", "Md", 258), ("Nobelium", "No", 259),
    ("Lawrencium", "Lr", 262), ("Rutherfordium", "Rf", 267),
    ("Dubnium", "Db", 268), ("Seaborgium", "Sg", 271),
    ("Bohrium", "Bh", 272), ("Hassium", "Hs", 270),
    ("Meitnerium", "Mt", 276), ("Darmstadtium", "Ds", 281),
    ("Roentgenium", "Rg", 282), ("Copernicium", "Cn", 285),
    ("Nihonium", "Nh", 286), ("Flerovium", "Fl", 289),
    ("Moscovium", "Mc", 290), ("Livermorium", "Lv", 293),
    ("Tennessine", "Ts", 294), ("Oganesson", "Og", 294)
        ]
        self.listbox = tk.Listbox(parent)
        for el in elements:
            self.listbox.insert(tk.END, f"{el[0]} ({el[1]}) - {el[2]}")
        self.listbox.grid(row=0, column=0)

class SpiceGirlIdentifier:
    def __init__(self, parent):
        people = [
               "Adele (not a spice girl)", "Alex Morgan (not a spice girl)",
    "Alicia Keys (not a spice girl)", "Amanda Seyfried (not a spice girl)",
    "Amy Adams (not a spice girl)", "Amy Poehler (not a spice girl)",
    "Angelina Jolie (not a spice girl)", "Anne Hathaway (not a spice girl)",
    "Ariana Grande (not a spice girl)", "Ashley Olsen (not a spice girl)",
    "Audrey Hepburn (not a spice girl)", "Ava Gardner (not a spice girl)",
    "Beyoncé Knowles (not a spice girl)", "Billie Holiday (not a spice girl)",
    "Blake Lively (not a spice girl)", "Brie Larson (not a spice girl)",
    "Britney Spears (not a spice girl)", "Cameron Diaz (not a spice girl)",
    "Cara Delevingne (not a spice girl)", "Cate Blanchett (not a spice girl)",
    "Catherine Zeta-Jones (not a spice girl)", "Charlize Theron (not a spice girl)",
    "Cher (not a spice girl)", "Christina Aguilera (not a spice girl)",
    "Cindy Crawford (not a spice girl)", "Claire Danes (not a spice girl)",
    "Daisy Ridley (not a spice girl)","Geri Halliwell (a spice girl)", 
    "Dakota Fanning (not a spice girl)",
    "Dame Judi Dench (not a spice girl)", "Demi Lovato (not a spice girl)",
    "Diana Ross (not a spice girl)", "Diane Keaton (not a spice girl)",
    "Drew Barrymore (not a spice girl)", "Ellen DeGeneres (not a spice girl)",
    "Ellen Page (not a spice girl)", "Elle Fanning (not a spice girl)",
    "Ellie Goulding (not a spice girl)", "Emilia Clarke (not a spice girl)",
    "Emily Blunt (not a spice girl)", "Emma Stone (not a spice girl)",
    "Emma Watson (not a spice girl)", "Eva Green (not a spice girl)",
    "Eva Longoria (not a spice girl)", "Eva Mendes (not a spice girl)",
    "Felicity Jones (not a spice girl)", "Florence Welch (not a spice girl)",
    "Gal Gadot (not a spice girl)", "Gigi Hadid (not a spice girl)",
    "Gillian Anderson (not a spice girl)", "Gisele Bündchen (not a spice girl)",
    "Grace Kelly (not a spice girl)", "Greta Gerwig (not a spice girl)",
    "Gwen Stefani (not a spice girl)", "Halle Berry (not a spice girl)",
    "Hayley Atwell (not a spice girl)", "Heidi Klum (not a spice girl)",
    "Helena Bonham Carter (not a spice girl)", "Hilary Duff (not a spice girl)",
    "Idina Menzel (not a spice girl)", "Irina Shayk (not a spice girl)",
    "Jada Pinkett Smith (not a spice girl)", "Janelle Monáe (not a spice girl)",
    "January Jones (not a spice girl)", "Emma Bunton (a spice girl)", 
    "Jennifer Aniston (not a spice girl)",
    "Jennifer Garner (not a spice girl)", "Jennifer Hudson (not a spice girl)",
    "Jennifer Lawrence (not a spice girl)", "Jennifer Lopez (not a spice girl)",
    "Jenny Slate (not a spice girl)", "Jessica Alba (not a spice girl)",
    "Jessica Biel (not a spice girl)", "Jessica Chastain (not a spice girl)",
    "Jessica Lange (not a spice girl)", "Jodie Foster (not a spice girl)",
    "Julia Roberts (not a spice girl)", "Julianne Moore (not a spice girl)",
    "Julie Andrews (not a spice girl)", "Juliette Binoche (not a spice girl)",
    "Kaley Cuoco (not a spice girl)", "Karen Gillan (not a spice girl)",
    "Kate Beckinsale (not a spice girl)", "Kate Hudson (not a spice girl)",
    "Kate Middleton (not a spice girl)", "Kate Moss (not a spice girl)",
    "Kate Winslet (not a spice girl)", "Katharine Hepburn (not a spice girl)",
    "Katherine Langford (not a spice girl)", "Kathy Bates (not a spice girl)",
    "Katie Holmes (not a spice girl)", "Katy Perry (not a spice girl)",
    "Keira Knightley (not a spice girl)", "Kendall Jenner (not a spice girl)",
    "Kerry Washington (not a spice girl)", "Kim Kardashian (not a spice girl)",
    "Kirsten Dunst (not a spice girl)", "Kristen Bell (not a spice girl)",
    "Kristen Stewart (not a spice girl)","Victoria Beckham (a spice girl)",
    "Lady Gaga (not a spice girl)",
    "Lana Del Rey (not a spice girl)", "Laura Dern (not a spice girl)",
    "Lauren Bacall (not a spice girl)", "Lea Michele (not a spice girl)",
    "Lena Headey (not a spice girl)", "Lena Waithe (not a spice girl)",
    "Lindsay Lohan (not a spice girl)", "Liv Tyler (not a spice girl)",
    "Lorde (not a spice girl)", "Lupita Nyong'o (not a spice girl)",
    "Maggie Smith (not a spice girl)", "Margot Robbie (not a spice girl)",
    "Maria Sharapova (not a spice girl)", "Marilyn Monroe (not a spice girl)",
    "Marion Cotillard (not a spice girl)", "Mariska Hargitay (not a spice girl)",
    "Maya Rudolph (not a spice girl)", "Meg Ryan (not a spice girl)",
    "Megan Fox (not a spice girl)", "Meryl Streep (not a spice girl)",
    "Mila Kunis (not a spice girl)", "Miley Cyrus (not a spice girl)",
    "Mindy Kaling (not a spice girl)", "Miranda Kerr (not a spice girl)",
    "Missy Elliott (not a spice girl)","Melanie Brown (a spice girl)"
    "Naomi Campbell (not a spice girl)",
    "Naomi Watts (not a spice girl)", "Natalie Dormer (not a spice girl)",
    "Natalie Portman (not a spice girl)", "Nicole Kidman (not a spice girl)",
    "Nina Dobrev (not a spice girl)", "Octavia Spencer (not a spice girl)",
    "Olivia Colman (not a spice girl)", "Olivia Munn (not a spice girl)",
    "Olivia Wilde (not a spice girl)", "Oprah Winfrey (not a spice girl)",
    "Pamela Anderson (not a spice girl)", "Paris Hilton (not a spice girl)",
    "Penélope Cruz (not a spice girl)", "Pink (not a spice girl)",
    "Priyanka Chopra (not a spice girl)", "Queen Latifah (not a spice girl)",
    "Quvenzhané Wallis (not a spice girl)", "Rachel McAdams (not a spice girl)",
    "Rebel Wilson (not a spice girl)", "Reese Witherspoon (not a spice girl)",
    "Rihanna (not a spice girl)", "Rita Ora (not a spice girl)",
    "Rosamund Pike (not a spice girl)", "Ruby Rose (not a spice girl)",
    "Sandra Bullock (not a spice girl)", "Saoirse Ronan (not a spice girl)",
    "Sarah Jessica Parker (not a spice girl)", "Sarah Paulson (not a spice girl)",
    "Scarlett Johansson (not a spice girl)", "Selena Gomez (not a spice girl)",
    "Shailene Woodley (not a spice girl)", "Shakira (not a spice girl)",
    "Sharon Stone (not a spice girl)", "Sigourney Weaver (not a spice girl)",
    "Sofía Vergara (not a spice girl)","Melanie Chisholm (a spice girl)",
    "Sophia Loren (not a spice girl)",
    "Sophie Turner (not a spice girl)", "Stevie Nicks (not a spice girl)",
    "Susan Sarandon (not a spice girl)", "Taylor Swift (not a spice girl)",
    "Tessa Thompson (not a spice girl)", "Tina Fey (not a spice girl)",
    "Uma Thurman (not a spice girl)", "Vanessa Hudgens (not a spice girl)",
    "Viola Davis (not a spice girl)", "Whitney Houston (not a spice girl)",
    "Whoopi Goldberg (not a spice girl)", "Winona Ryder (not a spice girl)",
    "Yara Shahidi (not a spice girl)", "Zoe Saldana (not a spice girl)",
    "Zoë Kravitz (not a spice girl)"  
        ]
        self.listbox = tk.Listbox(parent)
        for person in people:
            self.listbox.insert(tk.END, person)
        self.listbox.grid(row=0, column=0)

import random

class MorseCodeTranslator:
    def __init__(self, parent):
        self.text_to_translate = tk.Entry(parent)
        self.text_to_translate.grid(row=0, column=0)
        self.translated_text = tk.Entry(parent)
        self.translated_text.grid(row=1, column=0)
        self.translate_button = tk.Button(parent, text="Translate to Morse", command=self.translate)
        self.translate_button.grid(row=2, column=0)

    def translate(self):
        text = self.text_to_translate.get().upper()
        morse_dict = {
              'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
        }
        translated = ''.join(morse_dict.get(char, char) + self.random_delimiter() for char in text)
        translated = translated[:-len(self.random_delimiter())] if translated else translated
        self.translated_text.delete(0, tk.END)
        self.translated_text.insert(0, translated)

    def random_delimiter(self):
        chars = ";:,"
        return ''.join(random.choice(chars) for _ in range(random.randint(1, 3)))


class PasswordApp:
    def __init__(self, root):
        self.checker = PasswordChecker()
        self.setup_gui(root)

    def setup_gui(self, root):
        self.password_entry = tk.Text(root, height=10, width=80)
        self.password_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.current_requirement_label = tk.Label(root, text="Start typing your password...", fg="red", font=("Helvetica", 12))
        self.current_requirement_label.grid(row=1, column=0, columnspan=2, padx=10)
        self.progress = ttk.Progressbar(root, length=400, mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.requirements_list = tk.Listbox(root, width=100, height=10)
        self.requirements_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.submit_button = tk.Button(root, text="Submit Password", state=tk.DISABLED, command=self.submit_password)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.password_entry.bind("<KeyRelease>", self.on_key_release)

        # Helper areas
        tk.Label(root, text="Helpers", fg="blue", font=("Helvetica", 16)).grid(row=0, column=3, columnspan=2)
        calc_frame = tk.LabelFrame(root, text="Calculator")
        calc_frame.grid(row=1, column=3, padx=10, pady=10)
        SimpleCalculator(calc_frame, self.password_entry)  # Pass the password_entry to the calculator
        periodic_table_frame = tk.LabelFrame(root, text="Periodic Table")
        periodic_table_frame.grid(row=2, column=3, padx=10, pady=10)
        PeriodicTableDisplay(periodic_table_frame)
        spice_girls_frame = tk.LabelFrame(root, text="Spice Girl Identifier")
        spice_girls_frame.grid(row=3, column=3, padx=10, pady=10)
        SpiceGirlIdentifier(spice_girls_frame)
        morse_code_frame = tk.LabelFrame(root, text="Morse Code Translator")
        morse_code_frame.grid(row=4, column=3, padx=10, pady=10)
        MorseCodeTranslator(morse_code_frame)

    def on_key_release(self, event):
        password = self.password_entry.get("1.0", "end-1c")
        passed, current_requirement = self.checker.check_requirements(password)
        self.update_progress(len(passed))
        self.update_requirements_list(passed, current_requirement)
        if current_requirement:
            self.current_requirement_label.config(text=f"Next Requirement: {current_requirement}", fg="red")
        else:
            self.current_requirement_label.config(text="All requirements met!", fg="green")
        self.submit_button.config(state=tk.NORMAL if not current_requirement else tk.DISABLED)

    def update_progress(self, passed_count):
        total_requirements = len(self.checker.requirements)
        percentage_met = (passed_count / total_requirements) * 100
        self.progress['value'] = percentage_met

    def update_requirements_list(self, passed, current_requirement):
        self.requirements_list.delete(0, tk.END)
        for text, _ in self.checker.requirements:
            if text in passed:
                self.requirements_list.insert(tk.END, f"✓ {text}")
                self.requirements_list.itemconfig(tk.END, {'fg': 'green'})
            elif text == current_requirement:
                self.requirements_list.insert(tk.END, f"→ {text}")  
                self.requirements_list.itemconfig(tk.END, {'fg': 'orange'})
            else:
                self.requirements_list.insert(tk.END, f"✗ {text}")
                self.requirements_list.itemconfig(tk.END, {'fg': 'red'})

    def submit_password(self):
        messagebox.showinfo("Password Submitted", "Your password has been accepted!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Requirements Game")
    app = PasswordApp(root)
    root.geometry('1200x800')  
    root.mainloop()
