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
    root.geometry('800x600')  
    root.mainloop()
