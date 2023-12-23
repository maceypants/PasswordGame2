import tkinter as tk
from tkinter import messagebox
import datetime
import sympy

def spice_girls_included(p):
    spice_girls = ["Melanie Brown", "Melanie Chisholm", "Emma Bunton", "Geri Halliwell", "Victoria Beckham"]
    return any(spice_girl in p for spice_girl in spice_girls)

requirements = [
    ("Minimum length of 10 characters", lambda p: len(p) >= 10),
    ("Password must contain an Upper case letter", lambda p: any(c.isupper() for c in p)),
    ("Password must contain a Lower case letter", lambda p: any(c.islower() for c in p)),
    ("Password must contain a number", lambda p: any(c.isdigit() for c in p)),
    ("Password must contain a Special character", lambda p: any(c in "!@#$%^&*()_+" for c in p)),
    ("Password must contain the Morse code for 'hello' ", lambda p: ".... . .-.. .-.. ---" in p),
    ("Password must contain the element symbols for Gold, Platinum, and Sodium ", lambda p: all(x in p for x in ["Au", "Pt", "Na"])),
    ("Password must contain 3 even numbers", lambda p: sum(1 for c in p if c.isdigit() and int(c) % 2 == 0) >= 3),
    ("Password must add up to 42", lambda p: sum(int(c) for c in p if c.isdigit()) == 42),
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
    ("Password must include one of the spice girls.", spice_girls_included)
]

root = tk.Tk()
root.title("Password Requirements Game")

password_entry = tk.Text(root, height=10, width=100)
password_entry.pack()

current_requirement_label = tk.Label(root, text="Start typing your password...", fg="red")
current_requirement_label.pack()

passed_requirements_list = tk.Listbox(root, width=100, height=20) 
passed_requirements_list.pack()

submit_button = tk.Button(root, text="Submit Password", state=tk.DISABLED)
submit_button.pack()

def check_requirements(event):
    password = password_entry.get("1.0", "end-1c")
    passed = []
    current_requirement = None
    for text, check in requirements:
        if check(password):
            passed.append(text)
        elif current_requirement is None:
            current_requirement = text
    
    passed_requirements_list.delete(0, tk.END)
    for item in passed:
        passed_requirements_list.insert(tk.END, item)
    
    if current_requirement:
        current_requirement_label.config(text=current_requirement, fg="red") 
    else:
        current_requirement_label.config(text="All requirements met!", fg="green") 
    
    submit_button.config(state=tk.NORMAL if not current_requirement else tk.DISABLED)

password_entry.bind("<KeyRelease>", check_requirements)

def submit_password():
    messagebox.showinfo("Password Submitted", "Your password has been accepted!")

submit_button.config(command=submit_password)

root.mainloop()
