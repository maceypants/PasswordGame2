import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import sympy
import random
from elements import elements
from People import people

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
        self.listbox = tk.Listbox(parent)
        for el in elements:
            self.listbox.insert(tk.END, f"{el[0]} ({el[1]}) - {el[2]}")
        self.listbox.grid(row=0, column=0)

class SpiceGirlIdentifier:
    def __init__(self, parent):
        self.listbox = tk.Listbox(parent)
        for person in people:
            self.listbox.insert(tk.END, person)
        self.listbox.grid(row=0, column=0)

class MorseCodeTranslator:
    def __init__(self, parent):
        self.text_to_translate = tk.Entry(parent)
        self.text_to_translate.grid(row=0, column=0)
        self.translated_text = tk.Entry(parent)
        self.translated_text.grid(row=1, column=0)
        self.translate_button = tk.Button(parent, text="Translate to Morse", command=self.translate)
        self.translate_button.grid(row=2, column=0)
        self.first_time = True  # track message to see if first time

    def translate(self):
        if self.first_time:
            messagebox.showinfo("Notice", "I am still learning how to code 😔, there will be delimiters in this translation, use cautiously")
            self.first_time = False  # set flag to False after showing message

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
        self.question_button = None  # question mark button

    def create_tooltip_window(self):
        tooltip_window = tk.Toplevel()
        tooltip_window.title("Requirement Tip")

        message = "The requirement 'Password must include the current prime number of the month', means you must include the current prime number of the month."
        tk.Label(tooltip_window, text=message, wraplength=300).pack(padx=10, pady=10)

        return_button = tk.Button(tooltip_window, text="Return to the game", command=tooltip_window.destroy)
        return_button.pack(pady=10)

        tooltip_window.grab_set()

    def setup_gui(self, root):
        #  mainframe
        main_frame = tk.Frame(root)
        main_frame.grid(row=0, column=0, sticky='nsew')

        # Helpers frame
        helpers_frame = tk.Frame(root)
        helpers_frame.grid(row=0, column=1, sticky='nsew')

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.password_entry = tk.Text(main_frame, height=10, width=50)
        self.password_entry.grid(row=0, column=0, padx=10, pady=10)
        self.current_requirement_label = tk.Label(main_frame, text="Start typing your password...", fg="red", font=("Helvetica", 12))
        self.current_requirement_label.grid(row=1, column=0, padx=10, sticky='w')

        # Placeholder for question mark
        self.question_mark_placeholder = tk.Label(main_frame, width=2)
        self.question_mark_placeholder.grid(row=1, column=1, sticky='w')

        self.progress = ttk.Progressbar(main_frame, length=300, mode='determinate')
        self.progress.grid(row=2, column=0, padx=10, pady=10)
        self.requirements_list = tk.Listbox(main_frame, width=50, height=10)
        self.requirements_list.grid(row=3, column=0, padx=10, pady=10)

        self.submit_button = tk.Button(main_frame, text="Submit Password", state=tk.DISABLED, command=self.submit_password)
        self.submit_button.grid(row=4, column=0, padx=10, pady=10)
        self.password_entry.bind("<KeyRelease>", self.on_key_release)

        # Helpers
        tk.Label(helpers_frame, text="Helpers", fg="blue", font=("Helvetica", 16)).grid(row=0, column=0, padx=10, pady=10)
        calc_frame = tk.LabelFrame(helpers_frame, text="Calculator")
        calc_frame.grid(row=1, column=0, padx=10, pady=10)
        SimpleCalculator(calc_frame, self.password_entry)

        periodic_table_frame = tk.LabelFrame(helpers_frame, text="Periodic Table")
        periodic_table_frame.grid(row=2, column=0, padx=10, pady=10)
        PeriodicTableDisplay(periodic_table_frame)

        spice_girls_frame = tk.LabelFrame(helpers_frame, text="Spice Girl Identifier")
        spice_girls_frame.grid(row=3, column=0, padx=10, pady=10)
        SpiceGirlIdentifier(spice_girls_frame)

        morse_code_frame = tk.LabelFrame(helpers_frame, text="Morse Code Translator")
        morse_code_frame.grid(row=4, column=0, padx=10, pady=10)
        MorseCodeTranslator(morse_code_frame)


    def on_key_release(self, event):
        password = self.password_entry.get("1.0", "end-1c")
        passed, current_requirement = self.checker.check_requirements(password)
        self.update_progress(len(passed))
        self.update_requirements_list(passed, current_requirement)
        self.update_question_mark(current_requirement)
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

    def update_question_mark(self, current_requirement):
        target_requirement = "Password must include the current prime number of the month."
        if current_requirement == target_requirement:
            if not self.question_button:
                self.question_button = tk.Button(self.question_mark_placeholder, text="?", command=self.create_tooltip_window, padx=0, pady=0)
                self.question_button.pack(side="left", fill='both', expand=True)
        else:
            if self.question_button:
                self.question_button.destroy()
                self.question_button = None

    def submit_password(self):
        messagebox.showinfo("Password Submitted", "Your password has been accepted!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Requirements Game")
    app = PasswordApp(root)
    root.geometry('900x600')
    root.mainloop()
