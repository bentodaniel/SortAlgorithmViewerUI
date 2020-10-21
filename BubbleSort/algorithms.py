import time

def run_algorithm(data, wait_time, draw_data, algorithm):
    # This allows for an easy call of an algorithm

    if algorithm == 'Bubble Sort':
        bubble_sort(data, wait_time, draw_data)
    elif algorithm == 'Merge Sort':
        print('merge sort')


def bubble_sort(data, wait_time, draw_data):
    for i in range(len(data) - 1):
        for j in range(0, len(data) - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(wait_time)

    draw_data(data, ['green' for x in range(len(data))])