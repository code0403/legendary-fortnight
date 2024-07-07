class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):

        return len(self.items) == 0

    def push(self, item):

        self.items.append(item)

    def pop(self):
        
        if self.is_empty():
            print("Stack is empty")
            return
        return self.items.pop()

    def peek(self):
        
        if self.is_empty():
            print("Stack is empty")
            return
        return self.items[-1]
    

# Dynamically Push a new item onto the stack
def push_element(stack):
    while True:
        try:
            element = int(input("Enter an element to push (or 0 to stop): "))
            if element == 0:
                break
            stack.push(element)
        except ValueError:
            print("Invalid input.")


# Create a stack
stack = Stack()

# Push three elements to the stack
push_element(stack)


# Pop an element from the stack
pop_ele = stack.pop()
print("Popped element:", pop_ele)

# Push an three elements to the stack
push_element(stack)


# Pop two elements
pop_ele1 = stack.pop()
pop_ele2 = stack.pop()
print("Popped elements:", pop_ele1, pop_ele2)

# Push an element to the stack
push_element(stack)

# Check if the stack is empty
is_empty = stack.is_empty()
print(is_empty)

# Print the final state of the stack
print(stack.items)
