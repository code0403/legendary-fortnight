#Bubble Sort Function
def bubble_sort(A):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

#Main Function
def largest_difference(arr):

    # Checking if the array has less than two elements
    if len(arr) < 2:
        print(f"Sorted Array is : {arr}.")
        return 0

    # Sorting the array using bubble sort
    bubble_sort(arr)
    print(f"Sorted Array is : {arr}.")

    # Finding the largest difference between subsequent entries
    max_diff = 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff > max_diff:
            max_diff = diff

    return max_diff

# Take the input from user
input_array = input("Enter the Array (space-separated values): ")
arr = list(map(int, input_array.split(' ')))


result = largest_difference(arr)
print(f"Largest Difference between two subsequent entries is: {result}")
