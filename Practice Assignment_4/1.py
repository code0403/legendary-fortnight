def find_leaders(arr):
    n = len(arr)
    max_from_right = arr[-1]
    leaders = []

    leaders.append(arr[-1])

    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    leaders.reverse()
    
    print("Leaders in the array are:", ' '.join(map(str, leaders)))



n = int(input("Enter the size of the Array: "))
arr = list(map(int, input("Enter the Elements of the Array space seprated: ").split())) 

if len(arr) == n:
    find_leaders(arr)
else:
    print("Size of the Array is incorrect.")



