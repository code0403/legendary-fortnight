def find_two_sum_indices(arr, target):
    indices_map = {}
    
    for i, num in enumerate(arr):

        complement = target - num
        
        if complement in indices_map:
            return [indices_map[complement], i]
        
        indices_map[num] = i
    
    return [-1, -1]

try:
    n = int(input("Enter the size of the array: "))
    if n <= 0:
        print("Array size must be a positive integer.")
        exit()

    arr = list(map(int, input("Enter the array elements: ").split()))
    if len(arr) != n:
        print("The number of array elements does not match the specified size.")
        exit()

    target = int(input("Enter the target sum: "))
    
    result = find_two_sum_indices(arr, target)
    print("Indices of the two numbers:", result)

except ValueError:
    print("Invalid input. Please enter valid integers.")
