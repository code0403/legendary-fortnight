def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        if left_sum == (total_sum - arr[i] - left_sum):
            return i
        left_sum += arr[i]

    return -1

def main():
    n = int(input("Enter the size of the array: "))
    if n <= 0:
        print("Invalid Array Size")
        return

    arr = list(map(int, input("Enter the array elements: ").split()))
    if len(arr) != n:
        print("Invalid Array")
        return

    index = find_equilibrium_index(arr)

    if index != -1:
        print(f"Required Index: {index}")
    else:
        print("Required Index: -1")

if __name__ == "__main__":
    main()
