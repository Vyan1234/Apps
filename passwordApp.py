import tkinter as tk

username = "Vyan"
password = "1234"
root = tk.Tk()
root.title("Password game")
# root.geometry("1000x500")
buttonframe = tk.Frame(root)
buttonframe.grid(row = 3, column = 0, columnspan = 2)
label1 = tk.Label(root, text = "This is a  Password game.", font = ("ComicSansMS", 24, "bold"))
label1.grid(row = 0, column = 0, columnspan = 2)
label2 = tk.Label(root, text = "Enter the username:")
label2.grid(row = 1, column = 0, padx = 10)
entry1 = tk.Entry(root)
entry1.grid(row = 1, column = 1, padx = 10)
label3 = tk.Label(root, text = "Enter the password:")
label3.grid(row = 2, column = 0, padx = 10)
entry2 = tk.Entry(root, show = "#")
entry2.grid(row = 2, column = 1, padx = 10)
label4 = tk.Label(root, text = "")
label4.grid(row = 4, column = 0, pady = 10)

def check():
    a = entry1.get()
    b = entry2.get()
    print(a, b)
    if a == username and b == password:
        label4.config(text = "You are authorized")
    else:
        label4.config(text = "You are not authorized")
checkbutton = tk.Button(buttonframe, text = "CHECK", command = check)
checkbutton.grid(row = 3, column = 4)
root.mainloop()
