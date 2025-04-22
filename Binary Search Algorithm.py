# Binary Search Algorithm


def Binary_Search(array, target):
    start_index = 0
    end_index = len(array) -1
    
    while (start_index <= end_index):
        mid = (start_index + end_index) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            start_index = mid + 1
        
        else:
            end_index = mid - 1
    return -1

# Example usage
# The array must be sorted for binary search to work correctly
# The target is the number we are searching for in the array
# The function returns the index of the target if found, otherwise returns None
array_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

goal_target = 5

print(Binary_Search(array_items, goal_target))