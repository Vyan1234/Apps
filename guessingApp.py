import tkinter as tk
import random

root = tk.Tk()
root.title("Guessing game")
# root.geometry("1000x500")
buttonframe = tk.Frame(root)
buttonframe.grid(row = 3, column = 0, columnspan = 2)
n = random.randint(1, 50)
label1 = tk.Label(root, text = "This is a  Guessing game.", font = ("ComicSansMS", 24, "bold"))
label1.grid(row = 0, column = 0, columnspan = 2)
label2 = tk.Label(root, text = "Enter the your guess:")
label2.grid(row = 1, column = 0, padx = 10)
entry1 = tk.Entry(root)
entry1.grid(row = 1, column = 1, padx = 10)
label3 = tk.Label(root, text = "")
label3.grid(row = 2, column = 0, padx = 10)
def check():
    a = int(entry1.get())
    if a == n:
        label3.config(text = "You won!")
    if a < n:
        label3.config(text = "Too low.")
    if a > n:
        label3.config(text = "Too high.")
checkbutton = tk.Button(buttonframe, text = "CHECK", command = check)
checkbutton.grid(row = 0, column = 4)
root.mainloop()
