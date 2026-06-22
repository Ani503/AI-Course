import customtkinter as ctk
import math
import tkinter as tk

# =========================
# Window configuration
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Scientific Calculator")
root.geometry("400x650")
root.resizable(False, False)

# =========================
# Display
# =========================
entry = ctk.CTkEntry(root, font=("Helvetica", 40), justify="right", height=80, 
                     border_width=0, corner_radius=10,
                     fg_color="#8F9A8D",
                     text_color="black")
entry.grid(row=0, column=0, columnspan=5, padx=20, pady=(30, 20), sticky="nsew")

# =========================
# Functions logic
# =========================
def insert_value(value):
    entry.insert("end", value)

def clear():
    entry.delete(0, "end")

def delete():
    text = entry.get()
    entry.delete(0, "end")
    entry.insert(0, text[:-1])

def equal():
    try:
        # replace certain symbols that eval can't handle if necessary
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")

def single_op(func):
    try:
        val = float(entry.get())
        entry.delete(0, "end")
        entry.insert("end", str(func(val)))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")

def nCr():
    try:
        val_str = entry.get()
        if "," in val_str:
            n_str, r_str = val_str.split(",")
            n, r = int(n_str), int(r_str)
            entry.delete(0, "end")
            entry.insert("end", str(math.comb(n, r)))
        else:
            raise ValueError
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Format: n,r")

def nPr():
    try:
        val_str = entry.get()
        if "," in val_str:
            n_str, r_str = val_str.split(",")
            n, r = int(n_str), int(r_str)
            entry.delete(0, "end")
            entry.insert("end", str(math.perm(n, r)))
        else:
            raise ValueError
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Format: n,r")

def show_msg(name):
    entry.delete(0, "end")
    entry.insert("end", name + " Mode")

ops = {
    "√": math.sqrt,
    "x²": lambda x: x**2,
    "1/x": lambda x: 1/x,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log10,
    "ln": math.log,
    "%": lambda x: x/100
}

# =========================
# Layout Configuration
# =========================
button_layout = [
    ["SHIFT", "ALPHA", "REPLAY", "MODE", "ON"],
    ["sin", "cos", "tan", "log", "ln"],
    ["π", "1/x", "x²", "nCr", "nPr"],
    ["7", "8", "9", "DEL", "AC"],
    ["4", "5", "6", "*", "/"],
    ["1", "2", "3", "+", "-"],
    ["0", ".", "%", "√", "="]
]

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    
for i in range(1, 8):
    root.grid_rowconfigure(i, weight=1)

# =========================
# Button Creation
# =========================
for row_idx, row in enumerate(button_layout, start=1):
    for col_idx, text in enumerate(row):
        
        # Color coding
        if text in ["DEL", "AC"]:
            fg_color = "#D32F2F"
            hover_color = "#B71C1C"
            text_color = "white"
        elif text in ["ON", "SHIFT", "ALPHA"]:
            fg_color = "#FFB300"
            hover_color = "#FF8F00"
            text_color = "black"
        elif text in ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]:
            fg_color = "#E0E0E0"
            hover_color = "#BDBDBD"
            text_color = "black"
        elif text in ["+", "-", "*", "/", "="]:
            fg_color = "#9E9E9E"
            hover_color = "#757575"
            text_color = "black"
        else:
            fg_color = "#424242"
            hover_color = "#616161"
            text_color = "white"

        # Special commands routing
        if text == "=":
            cmd = equal
        elif text == "AC":
            cmd = clear
        elif text == "DEL":
            cmd = delete
        elif text == "π":
            cmd = lambda: insert_value(str(math.pi))
        elif text == "nCr":
            cmd = nCr
        elif text == "nPr":
            cmd = nPr
        elif text in ops:
            # We use named arguments in lambda to avoid late binding issue in loop
            cmd = lambda t=text: single_op(ops[t])
        elif text in ["SHIFT", "ALPHA", "REPLAY", "MODE", "ON"]:
            cmd = lambda t=text: show_msg(t)
        else:
            cmd = lambda t=text: insert_value(t)

        btn = ctk.CTkButton(root, text=text, font=("Arial", 16, "bold"),
                            command=cmd, width=50, height=40,
                            fg_color=fg_color, text_color=text_color, hover_color=hover_color,
                            corner_radius=8)
        
        pady = 5 if row_idx < 4 else 8
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=pady, sticky="nsew")

# =========================
root.mainloop()