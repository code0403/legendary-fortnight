def generate_batches(students, current_batch=[], index=0):
    # Base case: If all students have been processed, check if the current batch is valid
    if index == len(students):
        if is_valid_batch(current_batch):
            return [current_batch]
        else:
            return []
    
    # Exclude the current student and continue searching for Batches
    batches = generate_batches(students, current_batch, index + 1)
    
    # Include the current student if there are consecutive roll numbers
    if not current_batch or students[index] != current_batch[-1] + 1:
        batches += generate_batches(students, current_batch + [students[index]], index + 1)
    
    return batches

def is_valid_batch(batch):
    # Checking if the batch contains consecutive roll numbers
    for i in range(len(batch) - 1):
        if batch[i] == batch[i + 1] - 1:
            return False
    return True

def print_output(n):
    students = list(range(1, n + 1))
    # list of students
    # print(students)
    batches = generate_batches(students)
    # We need to remove the empty set if present
    batches = [batch for batch in batches if batch]
    num_ways = len(batches)
    if batches:
        largest = max(batches, key=len)
    else:
        largest = []

    # print(f"For n = {n}:")
    print("Number of ways a compatible batch can be chosen is:", num_ways)
    print("The sets are:")
    for batch in batches:
        print(batch)
    print("Largest batch:", largest)
    # print()


n = int(input("Number of Students: "))
print_output(n)




