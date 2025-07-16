from Dynamic_array import DynamicArray #using Dynamic Array i created

class Stack:
    """
    A Stack implementation using a list as the underlying data structure.
    Last In, First Out (LIFO) principle.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        # TODO: Initialize the stack data structure
        self.array = DynamicArray()
        self.top = -1

    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
        """
        self.array.append(item)
        self.top += 1
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.top < 0:
            raise IndexError("Stack is already empty")
        pop = self.array.pop()
        self.top -= 1
        return pop
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.top < 0:
             raise IndexError("Stack is empty")
        return self.array[self.top]
        
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        print(self.array,"hi")
        if len(self.array) <= 0:
            return True
        else:
            return False
    
    def size(self):
        """
        Return the number of items in the stack.
        
        Returns:
            int: Number of items in the stack
        """
        return self.top + 1
    
    def __str__(self):
        """
        String representation of the stack.
        
        Returns:
            str: String representation showing stack contents
        """
        # TODO: Implement string representation
        # Hint: Show the stack with top element on the right
        
        return str(self.array)


# Test cases for your Stack implementation
def test_stack():
    print("Testing Stack Implementation...")
    
    # Test 1: Create empty stack
    stack = Stack()
    assert stack.is_empty() == True, "New stack should be empty"
    assert stack.size() == 0, "New stack should have size 0"
    print("✓ Test 1 passed: Empty stack creation")
    
    # Test 2: Push single item
    stack.push(10)
    assert stack.is_empty() == False, "Stack with item should not be empty"
    assert stack.size() == 1, "Stack should have size 1"
    assert stack.peek() == 10, "Top item should be 10"
    print("✓ Test 2 passed: Push single item")
    
    # Test 3: Push multiple items
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3, "Stack should have size 3"
    assert stack.peek() == 30, "Top item should be 30 (last pushed)"
    print("✓ Test 3 passed: Push multiple items")
    
    # Test 4: Pop operation
    popped = stack.pop()
    assert popped == 30, "Popped item should be 30"
    assert stack.size() == 2, "Stack size should be 2 after pop"
    assert stack.peek() == 20, "New top should be 20"
    print("✓ Test 4 passed: Pop operation")
    
    # Test 5: Pop all items
    stack.pop()  # Remove 20
    stack.pop()  # Remove 10
    assert stack.is_empty() == True, "Stack should be empty after popping all items"
    assert stack.size() == 0, "Stack size should be 0"
    print("✓ Test 5 passed: Pop all items")
    
    # Test 6: Error handling - pop from empty stack
    try:
        stack.pop()
        assert False, "Should raise IndexError when popping from empty stack"
    except IndexError:
        print("✓ Test 6 passed: Pop from empty stack raises IndexError")
    
    # Test 7: Error handling - peek at empty stack
    try:
        stack.peek()
        assert False, "Should raise IndexError when peeking at empty stack"
    except IndexError:
        print("✓ Test 7 passed: Peek at empty stack raises IndexError")
    
    # Test 8: String representation
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack_str = str(stack)
    print(f"Stack string representation: {stack_str}")
    print("✓ Test 8 passed: String representation")
    
    # Test 9: Mixed data types
    stack_mixed = Stack()
    stack_mixed.push(1)
    stack_mixed.push("hello")
    stack_mixed.push([1, 2, 3])
    stack_mixed.push({"key": "value"})
    assert stack_mixed.size() == 4, "Stack should handle mixed data types"
    assert stack_mixed.peek() == {"key": "value"}, "Top should be the dictionary"
    print("✓ Test 9 passed: Mixed data types")
    
    print("\nAll tests passed! Your Stack implementation is working correctly.")


if __name__ == "__main__":
    test_stack()
    print("Complete the Stack implementation above, then uncomment test_stack() to run the tests!")