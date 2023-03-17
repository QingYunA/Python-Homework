import tkinter as tk

root = tk.Tk()


def button_click():
    print("Button clicked!")


button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()
