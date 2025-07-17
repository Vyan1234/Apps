import tkinter as tk

pin = "1234"
money = 43212
root = tk.Tk()
root.title("ATM")
# root.geometry("1000x500")
buttonframe = tk.Frame(root)
buttonframe.grid(row = 3, column = 0, columnspan = 2)
buttonframe2 = tk.Frame(root)
buttonframe2.grid(row = 9, column = 0, columnspan = 2)
label1 = tk.Label(root, text = "This is a ATM app.", font = ("ComicSansMS", 24, "bold"))
label1.grid(row = 0, column = 0, columnspan = 2)
label2 = tk.Label(root, text = "Enter the pin:")
label2.grid(row = 1, column = 0, padx = 10)
entry1 = tk.Entry(root, show = "#")
entry1.grid(row = 1, column = 1, padx = 10)
label3 = tk.Label(root, text = "")
label3.grid(row = 2, column = 0, padx = 10)
def check():
    a = entry1.get()
    if a == pin:
        label3.config(text = "You are authorized.")
    else:
        label3.config(text = "You are not authorized.")
checkbutton = tk.Button(buttonframe, text = "CHECK", command = check)
checkbutton.grid(row = 5, column = 0)
label6 = tk.Label(root, text = "Choose what to do.")
label6.grid(row = 6, column = 0)
label5 = tk.Label(root, text = "")
label5.grid(row = 8, column = 0)
def checkbalance():
    global money
    label5.config(text = f"This is your balance ${money}")
balancebutton = tk.Button(buttonframe2, text = "CHECK BALANCE", command = checkbalance)
balancebutton.grid(row = 0, column = 0, pady = 10, padx = 10)
label0 = tk.Label(root, text = "Enter the amount of money: ")
label0.grid(row = 6, column = 0, padx = 10)
entry2 = tk.Entry(root)
entry2.grid(row = 6, column = 1, padx = 10)
def addmoney():
    global money
    a = int(entry2.get())
    money = a + money
    label5.config(text = f"This is your balance ${money}")
addbutton = tk.Button(buttonframe2, text = "ADD MONEY", command = addmoney)
addbutton.grid(row = 0, column = 2, pady = 10)
def withdrawmoney():
    global money
    a = int(entry2.get())
    money = money - a
    label5.config(text = f"This is your balance ${money}")
withdrawbutton = tk.Button(buttonframe2, text = "WITHDRAW", command = withdrawmoney)
withdrawbutton.grid(row = 0, column = 3, pady = 10)
def exit():
    label5.config(text = "Bye bye")
    root.quit()
exitbutton = tk.Button(buttonframe2, text = "EXIT", command = exit)
exitbutton.grid(row = 0, column = 4, padx = 10, pady = 10)
root.mainloop()
