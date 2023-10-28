from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)


def result():
    miles = float(mile_entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Convert", command=result)
button.grid(column=1, row=2)





window.mainloop()
