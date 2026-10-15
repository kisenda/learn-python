def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False  # Target not found      
    else: 
        mid = (len(arr)) // 2
    
        if arr[mid] == target:
            return True    # Target found
        elif arr[mid] < target:
            return recursive_binary_search(arr[mid + 1:], target)  # Search in the right half
        else:
            return recursive_binary_search(arr[:mid], target)  # Search in the left half

def verify(result):
    print("Target is :", result);

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
result = recursive_binary_search(numbers, 8);
verify(result);

result = recursive_binary_search(numbers, 12);
verify(result);