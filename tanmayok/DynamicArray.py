class DynamicArray:
    """
    A Dynamic Array implementation that automatically resizes when needed.
    Similar to Python's list but implemented from scratch to understand the concepts.
    """
    
    def __init__(self, initial_capacity=4):
        """
        Initialize a dynamic array with given initial capacity.
        
        Args:
            initial_capacity (int): Initial capacity of the array (default: 4)
        """
        # TODO: Initialize the dynamic array
        # Hint: You'll need to track capacity, size, and the actual data
        pass
        self.capacity = initial_capacity
        self.arr = [None] * initial_capacity
        self.size = 0
    
    def __len__(self):
        """
        Return the number of elements in the array.
        
        Returns:
            int: Number of elements currently stored
        """
        return self.size
    
    def __getitem__(self, index):
        """
        Get an element at the specified index.
        
        Args:
            index (int): Index of the element to retrieve
            
        Returns:
            The element at the given index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if self.size < index -1:
            raise IndexError("Index out of Bounds")
        return self.arr[index]
    
    def __setitem__(self, index, value):
        """
        Set an element at the specified index.
        
        Args:
            index (int): Index where to set the value
            value: Value to set at the index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if self.size < index - 1:
            raise IndexError("Index out of Bounds")
        self.arr[index] = value
    
    def append(self, item):
        """
        Add an element to the end of the array.
        
        Args:
            item: Element to add to the array
        """
        if self.size >= self.capacity:
            self._resize()
        self.arr[self.size] = item
        self.size += 1
        
    
    def insert(self, index, item):
        """
        Insert an element at the specified index.
        
        Args:
            index (int): Index where to insert the element
            item: Element to insert
            
        Raises:
            IndexError: If index is out of bounds
        """
        if self.size < index - 1:
            raise IndexError("Index out of Bounds")
        for i in range(index,0,-1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = item
        self.size += 1
        

    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the array.
        
        Args:
            item: Item to remove from the array
            
        Raises:
            ValueError: If item is not found in the array
        """
        # TODO: Implement remove operation
        # Hint: Find the item, then shift elements left
        for i in range(self.size):
            print(self.arr[i],item,"ho")
            if self.arr[i] == item:
                for j in range(self.size):
                    self.arr[j] = self.arr[j+1]
                self.size -= 1
        print("Element Not found")

    
    def pop(self, index=-1):
        """
        Remove and return an element at the specified index.
        
        Args:
            index (int): Index of element to remove (default: -1 for last element)
            
        Returns:
            The removed element
            
        Raises:
            IndexError: If index is out of bounds or array is empty
        """
        if index > self.size:
            raise IndexError("Index is out of bounds")
        if index == -1:
            self.arr[size] = None
        return self.arr[index]

        

    
    def _resize(self):
        """
        Resize the array when capacity is exceeded.
        This is a private method (internal implementation detail).
        """
        newArr = [None] * (self.capacity * 2)
        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr
        self.capacity = self.capacity * 2
    
    def _is_full(self):
        """
        Check if the array is at full capacity.
        
        Returns:
            bool: True if array is full, False otherwise
        """
        return self.size >= self.capacity
    
    def getCapacity(self):
        """
        Return the current capacity of the array.
        
        Returns:
            int: Current capacity
        """
        return self.capacity
    
    def is_empty(self):
        """
        Check if the array is empty.
        
        Returns:
            bool: True if array is empty, False otherwise
        """
        return self.size < 1
    
    def __str__(self):
        """
        String representation of the dynamic array.
        
        Returns:
            str: String representation of the array contents
        """
        return str(self.arr)


# Test cases for your Dynamic Array implementation
def test_dynamic_array():
    print("Testing Dynamic Array Implementation...")
    
    # Test 1: Create empty array
    arr = DynamicArray()
    assert len(arr) == 0, "New array should have length 0"
    assert arr.is_empty() == True, "New array should be empty"
    assert arr.getCapacity() >= 4, "Initial capacity should be at least 4"
    print("✓ Test 1 passed: Empty array creation")
    
    # Test 2: Append single item
    arr.append(10)
    assert len(arr) == 1, "Array should have length 1"
    assert arr[0] == 10, "First element should be 10"
    assert arr.is_empty() == False, "Array should not be empty"
    print("✓ Test 2 passed: Append single item")
    
    # Test 3: Append multiple items
    arr.append(20)
    arr.append(30)
    arr.append(40)
    assert len(arr) == 4, "Array should have length 4"
    assert arr[3] == 40, "Last element should be 40"
    print("✓ Test 3 passed: Append multiple items")
    
    # Test 4: Test resizing (add more items than initial capacity)
    initial_capacity = arr.getCapacity()
    arr.append(50)  # This should trigger resize
    assert len(arr) == 5, "Array should have length 5"
    assert arr.getCapacity() > initial_capacity, "Capacity should have increased"
    assert arr[4] == 50, "New element should be accessible"
    print("✓ Test 4 passed: Automatic resizing")
    
    # Test 5: Index access and assignment
    arr[2] = 35
    assert arr[2] == 35, "Element at index 2 should be 35"
    print("✓ Test 5 passed: Index access and assignment")
    
    # Test 6: Insert operation
    arr.insert(1, 15)
    assert len(arr) == 6, "Array length should be 6"
    assert arr[1] == 15, "Element at index 1 should be 15"
    assert arr[2] == 20, "Element at index 2 should be 20 (shifted)"
    print("✓ Test 6 passed: Insert operation")
    
    # Test 7: Remove operation
    arr.remove(35)
    assert len(arr) == 5, "Array length should be 5"
    assert 35 not in [arr[i] for i in range(len(arr))], "35 should be removed"
    print("✓ Test 7 passed: Remove operation")
    
    # Test 8: Pop operation
    last_item = arr.pop()
    assert len(arr) == 4, "Array length should be 4"
    assert last_item == 50, "Popped item should be 50"
    
    second_item = arr.pop(1)
    assert len(arr) == 3, "Array length should be 3"
    assert second_item == 15, "Popped item should be 15"
    print("✓ Test 8 passed: Pop operation")
    
    # Test 9: Error handling - out of bounds access
    try:
        _ = arr[10]
        assert False, "Should raise IndexError for out of bounds access"
    except IndexError:
        print("✓ Test 9a passed: Out of bounds access raises IndexError")
    
    try:
        arr[10] = 100
        assert False, "Should raise IndexError for out of bounds assignment"
    except IndexError:
        print("✓ Test 9b passed: Out of bounds assignment raises IndexError")
    
    # Test 10: Error handling - remove non-existent item
    try:
        arr.remove(999)
        assert False, "Should raise ValueError for non-existent item"
    except ValueError:
        print("✓ Test 10 passed: Remove non-existent item raises ValueError")
    
    # Test 11: Error handling - pop from empty array
    empty_arr = DynamicArray()
    try:
        empty_arr.pop()
        assert False, "Should raise IndexError when popping from empty array"
    except IndexError:
        print("✓ Test 11 passed: Pop from empty array raises IndexError")
    
    # Test 12: String representation
    test_arr = DynamicArray()
    test_arr.append(1)
    test_arr.append(2)
    test_arr.append(3)
    arr_str = str(test_arr)
    print(f"Array string representation: {arr_str}")
    print("✓ Test 12 passed: String representation")
    
    # Test 13: Custom initial capacity
    custom_arr = DynamicArray(initial_capacity=8)
    assert custom_arr.getCapacity() == 8, "Custom capacity should be 8"
    for i in range(10):  # Add more than initial capacity
        custom_arr.append(i)
    assert len(custom_arr) == 10, "Should handle more items than initial capacity"
    print("✓ Test 13 passed: Custom initial capacity")
    
    # Test 14: Mixed data types
    mixed_arr = DynamicArray()
    mixed_arr.append(1)
    mixed_arr.append("hello")
    mixed_arr.append([1, 2, 3])
    mixed_arr.append({"key": "value"})
    assert len(mixed_arr) == 4, "Should handle mixed data types"
    assert mixed_arr[1] == "hello", "Should store strings"
    assert mixed_arr[3] == {"key": "value"}, "Should store dictionaries"
    print("✓ Test 14 passed: Mixed data types")
    
    print("\nAll tests passed! Your Dynamic Array implementation is working correctly.")


if __name__ == "__main__":
    try:
        # Uncomment the line below once you've implemented the DynamicArray class
        test_dynamic_array()
    except Exception as e:
        print(f"An error occurred during the tests: {e}")
    finally:
        print("Test execution complete!")
