# Insertion Sort Algorithm

print("\n\nProgram Created by Kieran\n\n")

def Insertion_Sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        pos = i
        
        while pos > 0 and array[pos-1] > current_value:
            array[pos] = array[pos-1]
            pos -= 1
        
        array[pos] = current_value
    return array


item_array = [5, 3, 10, 4, 2, 11, 1, 7, 6, 9, 7, 8]

print(Insertion_Sort(item_array))