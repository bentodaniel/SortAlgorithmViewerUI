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
        merge_sort(data, wait_time, draw_data)

    elif algorithm == 'QuickSort':
        print('QuickSort')

    elif algorithm == 'Radix Sort':
        print('Radix Sort')

    elif algorithm == 'Selection Sort':
        selection_sort(data, wait_time, draw_data)

#
# BUBBLE SORT
#
def bubble_sort(data, wait_time, draw_data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(wait_time)

    draw_data(data, ['green' for x in range(len(data))])


#
# INSERTION SORT
#
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


#
# MERGE SORT
#
def merge_sort(data, wait_time, draw_data): 
    merge_sort_sort(data, 0, len(data) - 1, wait_time, draw_data)

    draw_data(data, ['green' for x in range(len(data))])

def merge_sort_sort(data, left, right, wait_time, draw_data):
    if left < right: 
        mid = (left + right) // 2 
  
        # Sort first and second halves
        merge_sort_sort(data, left, mid, wait_time, draw_data)
        merge_sort_sort(data, mid + 1, right, wait_time, draw_data)
  
        # Merge the sorted halves 
        merge_sort_merge(data, left, mid, right, wait_time, draw_data)

def merge_sort_merge(data, left, mid, right, wait_time, draw_data):
    left_data = data[left : mid+1]
    right_data = data[mid+1 : right+1]
    
    l_index = r_index = 0

    # Cycle through original data allows to keep all data in the UI
    for i in range(left, right+1):
        if l_index < len(left_data) and r_index < len(right_data): 
            if left_data[l_index] <= right_data[r_index]: 
                data[i] = left_data[l_index] 
                l_index += 1 
            else: 
                data[i] = right_data[r_index]
                r_index += 1
  
        elif l_index < len(left_data): 
            data[i] = left_data[l_index]
            l_index += 1 
  
        elif r_index < len(right_data): 
            data[i] = right_data[r_index]
            r_index += 1

    draw_data(data, ['green' if x >= left and x <= right else 'red' for x in range(len(data))])
    time.sleep(wait_time)


#
# SELECTION SORT
#
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

