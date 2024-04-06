import tkinter as tk
from tkinter import messagebox
def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = lambda c: (c * 9/5) + 32
        result = fahrenheit(celsius)
        label_result.config(text=f"{celsius}°C = {result}°F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Celsius.")

root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("360x200")

label_celsius = tk.Label(root, text="Enter Celsius temperature:")
label_celsius.pack()
entry_celsius = tk.Entry(root)
entry_celsius.pack()

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
