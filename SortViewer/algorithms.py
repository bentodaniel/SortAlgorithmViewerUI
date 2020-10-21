import time

def run_algorithm(data, wait_time, draw_data, algorithm):
    # This allows for an easy call of an algorithm

    if algorithm == 'Bubble Sort':
        bubble_sort(data, wait_time, draw_data)

    elif algorithm == 'HeapSort':
        print('HeapSort')

    elif algorithm == 'Insertion Sort':
        insertion_sort(data, wait_time, draw_data)

    elif algorithm == 'Merge Sort':
        print('Merge Sort')

    elif algorithm == 'QuickSort':
        print('QuickSort')

    elif algorithm == 'Radix Sort':
        print('Radix Sort')

    elif algorithm == 'Selection Sort':
        selection_sort(data, wait_time, draw_data)


def bubble_sort(data, wait_time, draw_data):
    for i in range(len(data)):
        for j in range(0, len(data) - i):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(wait_time)

    draw_data(data, ['green' for x in range(len(data))])


def insertion_sort(data, wait_time, draw_data): 
    # Go through all array elements from 1
    for i in range(1, len(data)): 
        value = data[i] 
  
        j = i - 1
        while j >= 0 and value < data[j]: 
            data[j + 1] = data[j] 
            j -= 1
            draw_data(data, ['green' if x == i or x == j else 'red' for x in range(len(data))])
            time.sleep(wait_time)

        # Compensate the last j-1 in the while loop
        data[j + 1] = value
    
    draw_data(data, ['green' for x in range(len(data))])


def selection_sort(data, wait_time, draw_data):
    # Go through all array elements 
    for i in range(len(data)): 
        
        # Find min
        min_index = i
        for j in range(i + 1, len(data)): 
            if data[min_index] > data[j]: 
                min_index = j
                draw_data(data, ['green' if x == min_index or x == j else 'red' for x in range(len(data))])
                time.sleep(wait_time)
                
        # Swap the found minimum element        
        data[i], data[min_index] = data[min_index], data[i] 

    draw_data(data, ['green' for x in range(len(data))])

