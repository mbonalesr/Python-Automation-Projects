from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def converting_mi_to_km():
    """Multiplies a number times 1.6 to transform it to kilometres."""
    km = round(float(miles_input.get()) * 1.609,1)
    km_result.config(text=f"{km}")

#User Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#'Miles' Label
miles_label = Label(text="Miles", font=("Lexend", 12, "normal"))
miles_label.grid(column=2, row=0)

#'is equal to' Label
is_equal_to_label = Label(text="is equal to", font=("Lexend", 12, "normal"))
is_equal_to_label.grid(column=0, row=1)

# Km result
km_result = Label(text="0", font=("Lexend", 12, "bold"))
km_result.grid(column=1, row=1)

# 'km' Label
km_label = Label(text="km", font=("Lexend", 12, "normal"))
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=converting_mi_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
