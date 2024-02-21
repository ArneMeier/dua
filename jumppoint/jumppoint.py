import tkinter as tk

root = tk.Tk()
root.title("Datenstrukturen und Algorithmen")
root.state('zoomed')


button1 = tk.Button(root, text="Open Window 1", command=None)
button1.pack()

button2 = tk.Button(root, text="Open Window 2", command=None)
button2.pack()

button3 = tk.Button(root, text="Open Window 3", command=None)
button3.pack()

root.mainloop()