# Binary Search
# Memorised


def binary_search(list,goal):
    start_position = 0
    end_position = len(list) - 1
    
    while (start_position <= end_position):
        middle = (start_position + end_position) // 2
        
        
        if list[middle] == goal:
            return middle
        elif list[middle] < goal:
            start_position = middle + 1 
        else:
            end_position = middle - 1
    return -1


# print("Binary Search\n\n")

# print(binary_search([1,2,3,4,5,6,7,8,9], 5))



# Bubble Sort


def bubbles(list):
    swaps = True
        
    out = len(list) - 1
    
    while swaps == True:
        swaps = False
        
        for i in range(out):
            if list[i] > list[i+1]:
                swaps = True
                temporary = list[i]
                list[i] = list[i+1]
                list[i+1] = temporary
    out -= 1
    return list

print("Bubble Sort\n\n")

print(bubbles([1,2,3,4,5,6,7,8,9]))
