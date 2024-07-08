def largest_difference(sorted_array):
    lgd = 0
    if len(sorted_array) < 2:
        return 0
    else:
        for i in range(len(sorted_array) - 1):
            difference = sorted_array[i+1] - sorted_array[i]
            if difference > lgd:
                lgd = difference
        return lgd
            
# Input the Integer Array
# Input the Integer one by one seperated by spaces at once.
array = list(map(int, input("Enter the Array [A]: ").split()))
print("Array:", array)

sorted_array = sorted(array)
print("Sorted Array:", sorted_array)

largest_diff = largest_difference(sorted_array)
print("Largest Difference between two subsequent entries is:", largest_diff)