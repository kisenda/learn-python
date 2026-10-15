print("hello there!");

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None;

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the array.")

numbers = [1, 2, 3, 4, 5];
result = linear_search(numbers, 8);
verify(result);

result = linear_search(numbers, 3);
verify(result);