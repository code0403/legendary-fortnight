def generate_batches(n):
    if n == 0:
        return [[]]  # Base case: Return an empty batch
    elif n == 1:
        return [[1]]  # Base case: Return batches with one student each
    else:
        # Recursive case 1: Include the last student (n) in the batch
        batches_with_last_student = generate_batches(n - 2)
        batches_with_last_student = [[*batch, n] for batch in batches_with_last_student]
        
        # Recursive case 2: Exclude the last student (n) from the batch
        batches_without_last_student = generate_batches(n - 1)
        
        # Combine the batches from both recursive cases
        all_batches = batches_with_last_student + batches_without_last_student
        
        return all_batches

def largest_batch(batches):
    max_size = max(len(batch) for batch in batches)
    return [batch for batch in batches if len(batch) == max_size]

def print_output(n):
    batches = generate_batches(n)
    num_ways = len(batches)
    largest = largest_batch(batches)
    
    print(f"For n = {n}:")
    print("Number of ways a compatible batch can be chosen is:", num_ways)
    print("The sets are:")
    for batch in batches:
        print(batch)
    print("Largest batch:", largest)
    print()

# Test cases
test_cases = [3, 5, 6]
for n in test_cases:
    print_output(n)
