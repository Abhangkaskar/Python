import tkinter as tk
import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

def update_record():
    e_id = entry_id.get()
    new_name = entry_name.get()
    new_salary = entry_salary.get()

    cursor.execute("UPDATE EMP SET e_name=?, e_salary=? WHERE e_id=?", (new_name, new_salary, e_id))
    connection.commit()

    label_result.config(text=f"Record with ID {e_id} updated.")

root = tk.Tk()
root.title("Update Employee Record")

label_id = tk.Label(root, text="Enter ID:")
entry_id = tk.Entry(root)

label_name = tk.Label(root, text="New Name:")
entry_name = tk.Entry(root)

label_salary = tk.Label(root, text="New Salary:")
entry_salary = tk.Entry(root)

button_update = tk.Button(root, text="Update Record", command=update_record)

label_result = tk.Label(root, text="")
label_result.config(font=("Helvetica", 12))

label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_name.grid(row=1, column=0, padx=10, pady=5)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_salary.grid(row=2, column=0, padx=10, pady=5)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

button_update.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

connection.close()
