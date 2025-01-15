import tkinter as tk

def change_label_text():
    label.config(text="Button Clicked")
    
root = tk.Tk()
root.title("GUI Contril Example")

label = tk.Label(root, text="Hello, GUI Control!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=change_label_text)
button.pack()

root.mainloop()