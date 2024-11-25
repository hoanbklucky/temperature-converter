# program to convert F to C


# create GUI using tkinter

import tkinter as tk

# create window
window = tk.Tk()
window.title("Convert Fahrenheit to Celsius")

def convert():
    F_temp = float(F_temp_ent.get())
    C_temp = (F_temp - 32)*5/9
    C_temp_lbl["text"] = f"{C_temp:.1f}"



# create entry and label for F temp
F_temp_ent = tk.Entry(master=window, width=20, justify="center", font=12)
F_temp_ent.grid(row=0, column=0)

F_lbl = tk.Label(master=window, text="F", height=20, font=12)
F_lbl.grid(row=0, column=1)
# create button
convert_btn = tk.Button(master=window, text="Convert", relief="raised", command=convert, font=12)
convert_btn.grid(row=0, column=2)

# create labels for C temp
C_temp_lbl = tk.Label(master=window, width=10, relief="groove", font=12)
C_temp_lbl.grid(row=0, column=3)

C_lbl = tk.Label(master=window, text="C", font=12)
C_lbl.grid(row=0, column=4)

window.mainloop()
