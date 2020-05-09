import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random

#Global variables
max_elements = 500
window_height = 500 + 50 # +50 is the bar below the graph
window_width = 1250
sides_offset = 50
array = []
rectangles_array = []


def draw_main_window():
    global max_elements
    global array
    global rectangles_array

    array = []
    rectangles_array = []

    for widget in window.winfo_children():
        widget.destroy()

    canvas1 = tk.Canvas(window,width=500,height=300)
    canvas1.pack()

    label1 = tk.Label(window,text='Bubble Sort Algorithm Viewer')
    label1.config(font=('helvetica',14))
    canvas1.create_window(250,35,window=label1)

    label2 = tk.Label(window,text='Number of elements in the list:')
    label2.config(font=('helvetica',11))
    canvas1.create_window(150,100,window=label2)

    scale1 = Scale(window,from_=2,to=max_elements,length=150,orient=HORIZONTAL)
    canvas1.create_window(350,100,window=scale1)

    label3 = tk.Label(window,text='Minimum value:')
    label3.config(font=('helvetica',11))
    canvas1.create_window(102,150,window=label3)

    scale2 = Scale(window,from_=0,to=100,length=150,orient=HORIZONTAL)
    canvas1.create_window(350,150,window=scale2)

    label4 = tk.Label(window,text='Maximum value:')
    label4.config(font=('helvetica',11))
    canvas1.create_window(104,200,window=label4)

    scale3 = Scale(window,from_=0,to=500,length=150,orient=HORIZONTAL)
    canvas1.create_window(350,200,window=scale3)

    button1 = tk.Button(text='Quit',command=window.quit,bg='brown',fg='white',font=('helvetica',9,'bold'))
    button1.config(height=2,width=15)
    canvas1.create_window(150,260,window=button1)

    button2 = tk.Button(text='Start Algorithm',
                        command=lambda: start_program(scale1.get(),scale2.get(),scale3.get()),
                        bg='green',fg='white',
                        font=('helvetica',9,'bold'))
    button2.config(height=2,width=15)
    canvas1.create_window(350,260,window=button2)


def start_program(array_n_elements,min_value,max_value):
    global array
    global rectangles_array

    try:
        if array_n_elements < 2 or min_value > max_value:
            raise Exception()

        array = create_array(array_n_elements,min_value,max_value)
        rectangles_array = [None for x in range(len(array))]

        for widget in window.winfo_children():
            widget.destroy()

        display_graphic_window()

    except Exception:
        messagebox.showerror("Error","Invalid input.\nMinimum value must be lower than the maximum value.")


def create_array(array_n_elements,min_value,max_value):
    global array

    min_index = 0
    max_index = 0
    while min_index == max_index:
        min_index = random.randint(0,array_n_elements - 1)
        max_index = random.randint(0,array_n_elements - 1)

    for i in range(0,array_n_elements):
        if i == min_index:
            array.append(min_value)

        elif i == max_index:
            array.append(max_value)

        else:
            array.append(random.randint(min_value,max_value))

    return array


def display_graphic_window():
    global window_height
    global window_width

    canvas = tk.Canvas(window,width=window_width,height=window_height)
    canvas.create_line(0,window_height - 50,window_width,window_height - 50,fill="#476042")

    display_array(canvas)

    restart_btn = tk.Button(text='Restart',command=draw_main_window,bg='brown',fg='white',font=('helvetica',9,'bold'))
    restart_btn.config(height=1,width=10)
    canvas.create_window(50,window_height - 24,window=restart_btn)

    label4 = tk.Label(window,text='Time between comparisons [s]:')
    label4.config(font=('helvetica',11))
    canvas.create_window(window_width - 450,window_height - 24,window=label4)

    scale3 = Scale(window,from_=0.0,to=2.0,length=150,resolution=0.1,orient=HORIZONTAL)
    canvas.create_window(window_width - 250,window_height - 24,window=scale3)

    start_btn = tk.Button(text='Run',command=lambda:bubble_sort(canvas,scale3.get()),bg='green',fg='white',
                          font=('helvetica',9,'bold'))
    start_btn.config(height=1,width=10)
    canvas.create_window(window_width - 50,window_height - 24,window=start_btn)


def display_array(canvas):
    global window_height
    global window_width
    global array
    global rectangles_array
    global max_elements
    global sides_offset

    columns_size = (window_width - sides_offset*2) / len(array)

    for i in range(0, len(array)):
        rect = canvas.create_rectangle(sides_offset + (i*columns_size),
                                -0.9*array[i] + 500,
                                sides_offset + (i*columns_size) + columns_size,
                                window_height-50,
                                fill="red")

        rectangles_array[i] = rect

    canvas.pack()


def bubble_sort(canvas,wait_time):
    global array
    global rectangles_array

    n = len(array)

    for i in range(n-1):
        for j in range(0, n-i-1):
            color_compared_rectangles(canvas,j,j+1,'green')
            #time.sleep(wait_time)

            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]
                switch_array_positions(canvas,j,j+1)

            color_compared_rectangles(canvas,j,j + 1,'red')

        canvas.itemconfig(rectangles_array[n-i-1],fill='green')


def color_compared_rectangles(canvas,r1_index,r2_index,color):
    canvas.itemconfig(rectangles_array[r1_index],fill=color)
    canvas.itemconfig(rectangles_array[r2_index],fill=color)


def switch_array_positions(canvas,r1_index,r2_index):
    rect1_coords = canvas.coords(rectangles_array[r1_index])
    rect2_coords = canvas.coords(rectangles_array[r2_index])

    canvas.move(rectangles_array[r1_index],rect2_coords[0] - rect1_coords[0],0)

    canvas.move(rectangles_array[r2_index],-(rect2_coords[0]-rect1_coords[0]),0)

    rectangles_array[r1_index], rectangles_array[r2_index] = rectangles_array[r2_index], rectangles_array[r1_index]


window = tk.Tk()
window.title("Bubble Sorting")
window.resizable(width=False,height=False)

draw_main_window()

window.mainloop()
