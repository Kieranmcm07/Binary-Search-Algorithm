# Bubble Sort Algorithm

# Array to be sorted
item_array = [5, 3, 8, 4, 2, 8, 1, 7, 6, 9, 7, 8]

# Conditional Loop

def Conditional_Bubble_Sort(array):
    swaps = True    
    outer = len(array) - 1
    
    while swaps == True:
        swaps = False
        for i in range(outer):
            if array[i] > array[i + 1]:
                swaps = True
                
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    outer -= 1
    
    return array

# For Loop

def ForLoop_Bubble_Sort(array):
    swaps = 0
    min = 0
    max = len(array) - 1
    
    for i in range(min,max):
        swaps += 1 
        
        for j in range(i, max):
            
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

# Input

select = input("Bubble Sort\n1. Conditional Loop\n2. For Loop\nSelect: ")

if select == "1":
    print(Conditional_Bubble_Sort(item_array))
elif select == "2":
    print(ForLoop_Bubble_Sort(item_array))
else:
    print("Invalid selection. Please select 1 or 2.")
    exit(0)