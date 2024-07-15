def is_subset_sum(arr, n, target):
    dp = [False] * (target + 1)
    dp[0] = True
    
    for i in range(n):
        for j in range(target, arr[i] - 1, -1):
            if dp[j - arr[i]]:
                dp[j] = True
    
    return dp[target]

def find_subsets(arr, n, target):
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        if sum(subset) % target == 0:
            subsets.append(subset)
    return subsets

if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    X = int(input("Enter the value of X: "))
    array = list(map(int, input("Array is: ").split()))
    
    subsets = find_subsets(array, N, X)
    
    if is_subset_sum(array, N, X):
        print("Subsets are:", subsets)
        print("Output: Yes")
    else:
        print("Output: No")
