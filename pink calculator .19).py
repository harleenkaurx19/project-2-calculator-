import tkinter as tk
import math

root = tk.Tk()
root.title("💗 Pink Advanced Calculator")
root.geometry("350x500")
root.config(bg="#ffb6c1")  # pink background

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bg="#ffe4e1", fg="black", bd=8, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10)

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            value = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, math.sqrt(value))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "sin":
        entry.insert(tk.END, "math.sin(")
    elif text == "cos":
        entry.insert(tk.END, "math.cos(")
    elif text == "tan":
        entry.insert(tk.END, "math.tan(")
    elif text == "log":
        entry.insert(tk.END, "math.log(")
    else:
        entry.insert(tk.END, text)

# Buttons layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "√"],
    ["sin", "cos", "tan", "log"]
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), bg="#ff69b4", fg="white", width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
