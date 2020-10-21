import tkinter as tk
from tkinter import messagebox, Scale, HORIZONTAL, ttk
from tkinter import *
import random
from algorithms import run_algorithm

#Global variables
max_elements = 500
window_height = 500 + 50 # +50 is the bar below the graph
window_width = 1250
sides_offset = 50
array = []

sort_algorithms = ['Bubble Sort', 'HeapSort', 'Insertion Sort', 'Merge Sort', 'QuickSort', 'Radix Sort', 'Selection Sort']

# Display the UI functions
def generate_UI():
    #User Interface Area
    #Row[0]
    Label(UI_frame,text='Sorting Algorithm Viewer', font=('helvetica',20)).grid(row=0, column=0, padx=5, pady=5)

    #Row[1]
    sizeEntry = Scale(UI_frame, from_=2, to=max_elements, length=200, resolution=1, orient=HORIZONTAL, label='Number of elements: ')
    sizeEntry.grid(row=1, column=0, padx=50, pady=5)

    minEntry = Scale(UI_frame, from_=0, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Min Value")
    minEntry.grid(row=1, column=1, padx=50, pady=5)

    maxEntry = Scale(UI_frame, from_=0, to=500, length=200, resolution=1, orient=HORIZONTAL, label="Max Value")
    maxEntry.grid(row=1, column=2, padx=50, pady=5)

    Button(UI_frame, text='Generate Array',
            command=lambda: generate_n_display(sizeEntry.get(),minEntry.get(),maxEntry.get()),
            bg='blue',fg='white', height=2,width=15,
            font=('helvetica',9,'bold')).grid(row=1, column=3, padx=50, pady=5)

    #Row[2]
    Label(UI_frame, text="Algorithm: ", font=('helvetica',10)).grid(row=2, column=0, padx=50, pady=5, sticky=E)
    algMenu = ttk.Combobox(UI_frame, values=sort_algorithms)
    algMenu.grid(row=2, column=1, padx=100, pady=5)
    algMenu.current(0)

    speedScale = Scale(UI_frame, from_=0.0, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label='Time between comparisons [s]:')
    speedScale.grid(row=2, column=2, padx=5, pady=5)

    Button(UI_frame, text='Start Algorithm',
            command=lambda: run_algorithm(array, speedScale.get(), display_array, algMenu.get()),
            bg='green',fg='white', height=2,width=15,
            font=('helvetica',9,'bold')).grid(row=2, column=3, padx=50, pady=5)


# Starts the program, creating the array and displaying it on the second window
def generate_n_display(array_n_elements, min_value, max_value):
    global array

    array = []

    try:
        if array_n_elements < 2 or min_value > max_value:
            raise Exception()

        array = create_array(array_n_elements,min_value,max_value)

        display_array(array, ['red' for x in range(len(array))])

    except Exception:
        messagebox.showerror("Error","Invalid input.\nMinimum value must be lower or equal to the maximum value.")


# Creates a random array
def create_array(array_n_elements,min_value,max_value):
    global array

    min_index = 0
    max_index = 0
    while min_index == max_index:
        # Defines the indexes in the array for the minimum and maximum values
        # This makes sure the given values will exist in the array
        min_index = random.randint(0,array_n_elements - 1)
        max_index = random.randint(0,array_n_elements - 1)

    # Creates the array with random values between min and max
    # Randomly ordered
    for i in range(0,array_n_elements):
        if i == min_index:
            array.append(min_value)
        elif i == max_index:
            array.append(max_value)
        else:
            array.append(random.randint(min_value,max_value))

    return array
    

# Displays the array in the window
def display_array(array, colors_array):
    global window_height
    global window_width
    global sides_offset

    canvas.delete("all")

    columns_size = (window_width - sides_offset*2) / len(array)

    for i in range(0, len(array)):
        canvas.create_rectangle(sides_offset + (i*columns_size),
                            -0.9*array[i] + 500,
                            sides_offset + (i*columns_size) + columns_size,
                            window_height-50,
                            fill=colors_array[i])

    
    root.update_idletasks()


root = tk.Tk()
root.title('Sorting Algorithm Viewer')
root.resizable(width=False,height=False)

#frame / base lauout
UI_frame = tk.Frame(root, width= 1250, height=100)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Just a frame separator
tk.Frame(root, width= 1250, height=2, bg='black').grid(row=1, column=0, padx=10, pady=5)

canvas = tk.Canvas(root,width=1250,height=550)
canvas.grid(row=2, column=0, padx=10, pady=5)

generate_UI()


root.mainloop()
