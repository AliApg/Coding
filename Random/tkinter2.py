import tkinter as tk
border_effects = {"FLAT": tk.FLAT,"SUNKEN": tk.SUNKEN,"RAISED": tk.RAISED,
                  "GROOVE": tk.GROOVE,"RIDGE": tk.RIDGE}
root=tk.Tk()
for relief_name, relief in border_effects.items():
    frame = tk.Frame(root, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(frame, text=relief_name)
    label.pack()
root.mainloop()
