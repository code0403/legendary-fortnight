def is_equal_half_sum(n):
    n_str = str(n)
    
    length = len(n_str)

    if length == 1:
        return True
    
    if length % 2 != 0:
        mid = length // 2
        first_half = n_str[:mid]  
        second_half = n_str[mid+1:]  
    else:
        mid = length // 2
        first_half = n_str[:mid] 
        second_half = n_str[mid:]  
    
    
    first_sum = 0
    second_sum = 0
    
    
    for digit in first_half:
        first_sum += int(digit)
    
    
    for digit in second_half:
        second_sum += int(digit)
    
    
    return first_sum == second_sum


user_input = int(input("Please enter an positive integer:"))

if user_input == 0:
    print(" please entera  positive interger number greater than 0.")

else:
    sum_of_digit = is_equal_half_sum(user_input)
    print(sum_of_digit)
