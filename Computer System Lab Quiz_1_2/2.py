def combination_sum(nums, target):
    def backtrack(start, target, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            backtrack(i, target - nums[i], path + [nums[i]])

    result = []
    backtrack(0, target, [])
    return result

# Input
size = int(input("Enter the size of the array: "))
print("Enter the array elements:")

# Initialize an empty array to store the elements
array = []

for i in range(size):
    while True:
        try:
            element = int(input(f"Enter element {i + 1}: "))
            array.append(element)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

target = int(input("Enter the target: "))


# Finding the unique combinations
combinations = combination_sum(array, target)

# Dispay the Output
print("Unique combinations are:", combinations)
