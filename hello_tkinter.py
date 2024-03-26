import tkinter as tk


def beaver():
    print('BEAVER')

def beaver2(event: tk.Event):
    print('beaver?')

def fighter():
    print('FIGHTERX')

def n():
    print('coordinator is a ____')

root = tk.Tk()
root.geometry('400x400')
button = tk.Button(root, text='BEAVER', command=beaver)
button.bind('<Enter>', beaver2)
button.pack()
button2 = tk.Button(root, text='FIGHTERX', command=fighter)
button2.pack()
button3 = tk.Button(root, text='N', command=n)
button3.pack()
root.title("Hello Fighter")
label = tk.Label(root, text="label")
label.pack()
root.mainloop()