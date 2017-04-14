
def bubble_sort(array):
    input_array = array
    starter_index = 0
    next_index = 1


    if input_array[starter_index] > input_array[next_index]:
        input_array[starter_index], input_array[next_index] = input_array[next_index], input_array[starter_index]
