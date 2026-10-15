def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    first = 0; 
    last = len(arr) - 1;

    while first <= last:
        mid = (first + last) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            first = mid + 1
        # If target is smaller, ignore right half
        else:
            last = mid - 1

    # Target was not found in the array
    return None;

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the array.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
result = binary_search(numbers, 8);
verify(result);

result = binary_search(numbers, 3);
verify(result);