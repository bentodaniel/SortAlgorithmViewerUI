import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random

def draw_main_window():
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

    scale1 = Scale(window,from_=2,to=25,length=150,orient=HORIZONTAL)
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
                        command=lambda: start_bubble_sort(scale1.get(),scale2.get(),scale3.get()),
                        bg='green',fg='white',
                        font=('helvetica',9,'bold'))
    button2.config(height=2,width=15)
    canvas1.create_window(350,260,window=button2)


def start_bubble_sort(n_elems,min,max):
    try:
        array_n_elements = int(n_elems)
        min_value = int(min)
        max_value = int(max)

        if array_n_elements < 2 or min_value > max_value:
            raise Exception()

        array = create_array(array_n_elements,min_value,max_value)

        for widget in window.winfo_children():
            widget.destroy()

        display_array(array)
    except Exception:
        messagebox.showerror("Error","Invalid input.\nMinimum value must be lower than the maximum value.")


def create_array(array_n_elements,min_value,max_value):
    min_index = 0
    max_index = 0
    while min_index == max_index:
        min_index = random.randint(0,array_n_elements - 1)
        max_index = random.randint(0,array_n_elements - 1)


    array = []
    for i in range(0,array_n_elements):
        if i == min_index:
            array.append(min_value)

        elif i == max_index:
            array.append(max_value)

        else:
            array.append(random.randint(min_value,max_value))

    return array


def display_array(array):

    window_height = 500 + 50
    window_width = 25 * 50

    offset = 50
    columns_space = 25 - len(array)
    columns_size = ((window_width - offset*2) - (columns_space*(len(array)-1))) / len(array)

    canvas = tk.Canvas(window,width=window_width,height=window_height)
    canvas.create_line(0,window_height-50,window_width,window_height-50,fill="#476042")

    for i in range(0, len(array)):
        canvas.create_rectangle(offset + (i*columns_size) + (columns_space*i),
                                -0.9*array[i] + 500,
                                offset + (i*columns_size) + columns_size + (columns_space*i),
                                window_height-50,
                                fill="red")

        label4 = tk.Label(window,text=array[i])
        label4.config(font=('helvetica',12))
        canvas.create_window(offset + (i*columns_size) + (columns_size/2) + (columns_space*i),
                             -0.9 * array[i] + 500 - 15,
                             window=label4)

    canvas.pack()

    restart_btn = tk.Button(text='Restart',command=draw_main_window,bg='brown',fg='white',font=('helvetica',9,'bold'))
    restart_btn.config(height=1,width=10)
    canvas.create_window(50,window_height - 24,window=restart_btn)

    label4 = tk.Label(window,text='Execution speed:')
    label4.config(font=('helvetica',11))
    canvas.create_window(window_width-400,window_height - 24,window=label4)

    scale3 = Scale(window,from_=0.1,to=2.0,length=150,resolution=0.1,orient=HORIZONTAL)
    canvas.create_window(window_width-250,window_height - 24,window=scale3)

    start_btn = tk.Button(text='Run',command=lambda:find_repeated_occurrence(array),bg='green',fg='white',
                          font=('helvetica',9,'bold'))
    start_btn.config(height=1,width=10)
    canvas.create_window(window_width - 50,window_height - 24,window=start_btn)


window = tk.Tk()
window.title("Bubble Sorting")
window.resizable(width=False,height=False)

draw_main_window()

window.mainloop()