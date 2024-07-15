# Function to generate all the posssible subsets of an array
def find_subsets(arr, X):
    def generate_subsets(index, current_subset):
        if index == len(arr):
            if current_subset:
                subsets.append(current_subset)
            return
        # Include the current element
        generate_subsets(index + 1, current_subset + [arr[index]])
        # Exclude the current element
        generate_subsets(index + 1, current_subset)
    

    # Function to check if the sum of the subsets is divisible by the the target element
    def check_divisibility(subsets, X):
        divisible_subsets = []
        for subset in subsets:
            if sum(subset) % X == 0:
                divisible_subsets.append(subset)
        return divisible_subsets
    
    #  Empty arry intialized
    subsets = []
    # calls the generate_subsets function with the intial value 
    generate_subsets(0, [])
    # Check Divisiblity function is called
    divisible_subsets = check_divisibility(subsets, X)
    if divisible_subsets:
        print("Subsets are:", divisible_subsets)
        # return "Yes"
        print("Yes")
    else:
        # return "No"
        print("No")

# Input N and X from the user
N = int(input("Enter the value of N: "))
X = int(input("Enter the value of X: "))

# Input the array elements from the user
arr = []
print("Enter the array elements:")
for _ in range(N):
    arr.append(int(input()))

# Check if there exists any subset for whose sum is divisible by X
result = find_subsets(arr, X)

