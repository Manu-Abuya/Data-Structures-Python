# Stack Data Structure

# Create a stack
def create_stack():
    stack = []
    return stack

# Create an empty stack


def check_empty(stack):
    return len(stack) == 0

# Add items to the stack


def push(stack, item):
    stack.append(item)
    print("Item pushes to the stack: " + item)

# Remove an element from the stack


def pop(stack):
    if (check_empty(stack)):
        return "The stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

print("Item popped: " + pop(stack))
print("After popping an element, the stack is as displayed: " + str(stack))
