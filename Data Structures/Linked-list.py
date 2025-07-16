"""
Linked List Implementation Practice Problem
==========================================

Your task is to implement a singly linked list from scratch with all essential operations.
A linked list is a linear data structure where elements are stored in nodes, and each node
contains data and a reference (pointer) to the next node in the sequence.

Key Concepts:
- Dynamic size: Can grow/shrink during runtime
- Sequential access: Must traverse from head to reach elements
- Efficient insertion/deletion at head: O(1)
- Memory overhead: Each node requires extra space for pointer
- No random access: Cannot directly access elements by index like arrays

Common Pitfalls to Avoid:
- Forgetting to handle empty list cases
- Not updating head pointer correctly
- Memory leaks (though Python handles garbage collection)
- Off-by-one errors in indexing
- Losing references to nodes during operations
"""

class Node:
    """
    A single node in the linked list.
    
    This is a helper class that represents one element in the linked list.
    Each node contains data and a reference to the next node.
    """
    
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in this node (can be any type)
        """
        self.data = data
        self.next = None  


class LinkedList:
    """
    A singly linked list implementation supporting various operations.
    
    This linked list supports:
    - Dynamic sizing
    - Mixed data types
    - Standard operations (insert, delete, search)
    - Iteration and representation
    
    Time Complexities:
    - Access: O(n) - must traverse from head
    - Search: O(n) - must check each node
    - Insertion at head: O(1) - direct reference
    - Insertion at tail: O(n) - must traverse to end
    - Deletion at head: O(1) - direct reference
    - Deletion at position: O(n) - must traverse to position
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        
        The head pointer starts as None, indicating an empty list.
        We also maintain a size counter for efficiency.
        """
        # TODO: Initialize the head pointer and size counter
        self.head = None
        self.tail = None
        self.length = 0
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self.head == None
    
    def size(self):
        """
        Get the number of elements in the linked list.
        
        Returns:
            int: The number of nodes in the list
            
        Time Complexity: O(1) with size counter, O(n) without
        """
        return self.length
    
    def prepend(self, data):
        """
        Add a new element at the beginning of the list.
        
        Args:
            data: The value to add (can be any type)
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        This is the most efficient insertion operation for linked lists.
        """
        # TODO: Create a new node
        # TODO: Set new node's next to current head
        # TODO: Update head to point to new node
        # TODO: Increment size counter

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length +=1
  
    def append(self, data):
        """
        Add a new element at the end of the list.
        
        Args:
            data: The value to add (can be any type)
            
        Time Complexity: O(n) - must traverse to end
        Space Complexity: O(1)
        
        Less efficient than prepend due to traversal requirement.
        """
        # TODO: Handle empty list case (same as prepend)
        # TODO: Traverse to the last node
        # TODO: Create new node and link it
        # TODO: Increment size counter
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def insert(self, index, data):
        """
        Insert a new element at the specified index.
        
        Args:
            index (int): The position to insert at (0-based)
            data: The value to insert
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(n) - may need to traverse to position
        Space Complexity: O(1)
        
        Index 0 is equivalent to prepend operation.
        """
        # TODO: Validate index bounds
        # TODO: Handle special case for index 0
        # TODO: Traverse to position index-1
        # TODO: Create new node and adjust pointers
        # TODO: Increment size counter
        if index < 0 or index > self.length:
            print(index,"index")
            raise IndexError("Index out of bounds")
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return
        current_node = self.head
        current_index = 0
        while current_index != (index -1):
            current_node = current_node.next
            current_index += 1
        new_node.next = current_node.next
        current_node.next = new_node
        self.length +=1

    def delete_first(self):
        """
        Remove and return the first element from the list.
        
        Returns:
            The data from the removed node
            
        Raises:
            IndexError: If the list is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Handle empty list case
        # TODO: Store data to return
        # TODO: Update head to next node
        # TODO: Decrement size counter
        # TODO: Return stored data
        if self.length < 1:
            raise IndexError("Index out of Bound")
        removed_ele = self.head
        self.head = removed_ele.next
        self.length -= 1
        return removed_ele.data
    
    def delete_last(self):
        """
        Remove and return the last element from the list.
        
        Returns:
            The data from the removed node
            
        Raises:
            IndexError: If the list is empty
            
        Time Complexity: O(n) - must traverse to second-to-last node
        Space Complexity: O(1)
        """
        # TODO: Handle empty list case
        # TODO: Handle single element case
        # TODO: Traverse to second-to-last node
        # TODO: Store data and update pointers
        # TODO: Decrement size counter
        # TODO: Return stored data
        if self.length < 1:
            raise IndexError("Index out of Bound")
        current_node  = self.head
        if self.length == 1:
            removed_ele = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_ele.data
        while current_node.next.next != None:
            current_node = current_node.next
        removed_ele = current_node.next
        current_node.next = None
        self.tail = current_node
        self.length -= 1
        return removed_ele.data
    
    def delete_at(self, index):
        """
        Remove and return the element at the specified index.
        
        Args:
            index (int): The position to remove from (0-based)
            
        Returns:
            The data from the removed node
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(n) - may need to traverse to position
        Space Complexity: O(1)
        """
        # TODO: Validate index bounds
        # TODO: Handle special case for index 0
        # TODO: Traverse to position index-1
        # TODO: Store data and adjust pointers
        # TODO: Decrement size counter
        # TODO: Return stored data
        if index < 0 or index >= self.length:
            raise  IndexError("Index out of bounds")
        if index == 0:
            return self.delete_first()
            
        if index == self.length - 1:
            return self.delete_last()
        curr_index  = 0
        curr_ele = self.head
        while curr_index != (index-1):
            curr_ele = curr_ele.next
            curr_index +=1
        removed_ele = curr_ele.next
        curr_ele.next = removed_ele.next
        self.length -=1
        return removed_ele.data
               
    def find(self, data):
        """
        Find the first occurrence of data in the list.
        
        Args:
            data: The value to search for
            
        Returns:
            int: The index of the first occurrence, or -1 if not found
            
        Time Complexity: O(n) - may need to check all nodes
        Space Complexity: O(1)
        """
        # TODO: Traverse the list while tracking index
        # TODO: Compare each node's data with target
        # TODO: Return index if found, -1 if not found
        curr_node = self.head
        curr_index = 0
        while curr_node:
            if curr_node.data == data:
                return curr_index
            curr_node = curr_node.next
            curr_index += 1
        return -1


    
    def get(self, index):
        """
        Get the element at the specified index without removing it.
        
        Args:
            index (int): The position to access (0-based)
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(n) - must traverse to position
        Space Complexity: O(1)
        """
        # TODO: Validate index bounds
        # TODO: Traverse to the specified position
        # TODO: Return the data at that position
        if index < 0 or index >= self.length:
            raise IndexError("Index Out of Range")
        current = self.head
        currentIndex = 0
        while current:
            if currentIndex == index:
                return current.data
            currentIndex += 1
            current = current.next
    
    def reverse(self):
        """
        Reverse the linked list in-place.
        
        This operation reverses the order of elements by changing
        the direction of pointers between nodes.
        
        Time Complexity: O(n) - must visit each node once
        Space Complexity: O(1) - only uses a constant amount of extra space
        
        Algorithm: Use three pointers (prev, current, next) to reverse links
        """
        # TODO: Initialize three pointers: prev=None, current=head, next=None
        # TODO: Iterate through list reversing each link
        # TODO: Update head to point to new first node (prev)
        curr = self.head
        prev = None
        self.tail = self.head
        while curr:
            next = curr.next

            curr.next = prev

            prev = curr
            curr = next
        self.head = prev

    
    def to_list(self):
        """
        Convert the linked list to a Python list.
        
        Returns:
            list: A Python list containing all elements in order
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Useful for testing and debugging.
        """
        res = []
        current  = self.head
        while current:
            res.append(current.data)
            current = current.next
        return res
    
    def __len__(self):
        """
        Enable len() function to work with linked list.
        
        Returns:
            int: The number of elements in the list
        """
        return self.size()
    
    def __str__(self):
        """
        String representation of the linked list.
        
        Returns:
            str: A string representation showing all elements
            
        Format: "LinkedList: [1, 2, 3]" or "LinkedList: []" if empty
        """
        # TODO: Convert to list and format as string
        res = []
        current  = self.head
        while current:
            res.append(current.data)
            current = current.next
        return f'LinkedList: {res}'
    
    def __iter__(self):
        """
        Make the linked list iterable.
        
        Yields:
            The data from each node in sequence
            
        This allows using the linked list in for loops and other iteration contexts.
        """
        # TODO: Traverse the list and yield each node's data
        current = self.head
        while current:
            yield current.data
            current = current.next



# Comprehensive Test Suite
# ========================

def test_basic_operations():
    """Test fundamental linked list operations."""
    print("Testing basic operations...")
    
    # Test initialization
    ll = LinkedList()
    assert ll.is_empty() == True
    assert ll.size() == 0
    assert str(ll) == "LinkedList: []"
    
    # Test prepend
    ll.prepend(1)
    assert ll.is_empty() == False
    assert ll.size() == 1
    assert ll.get(0) == 1
    
    
    ll.prepend(2)
    assert ll.size() == 2
    assert ll.get(0) == 2
    assert ll.get(1) == 1
 
    # Test append
    ll.append(3)
    assert ll.size() == 3
    assert ll.get(2) == 3

    
    print("✓ Basic operations passed")


def test_insertion_operations():
    """Test various insertion methods."""
    print("Testing insertion operations...")
    
    ll = LinkedList()
    
    # Test insert at various positions
    ll.insert(0, 'a')  # Insert at beginning
    assert ll.get(0) == 'a'
    
    ll.insert(1, 'c')  # Insert at end
    assert ll.get(1) == 'c'
    
    ll.insert(1, 'b')  # Insert in middle
    assert ll.to_list() == ['a', 'b', 'c']
    
    # Test insert at boundaries
    ll.insert(0, 'start')
    ll.insert(ll.size(), 'end')
    assert ll.to_list() == ['start', 'a', 'b', 'c', 'end']
    
    print("✓ Insertion operations passed")


def test_deletion_operations():
    """Test various deletion methods."""
    print("Testing deletion operations...")
    
    ll = LinkedList()
    for i in range(1, 6):  # [1, 2, 3, 4, 5]
        ll.append(i)
    
    # Test delete_first
    assert ll.delete_first() == 1
    assert ll.to_list() == [2, 3, 4, 5]
    
    # Test delete_last
    assert ll.delete_last() == 5
    assert ll.to_list() == [2, 3, 4]
    
    # Test delete_at
    assert ll.delete_at(1) == 3
    assert ll.to_list() == [2, 4]
    
    # Test delete until empty
    ll.delete_first()
    ll.delete_first()
    assert ll.is_empty() == True
    
    print("✓ Deletion operations passed")


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("Testing edge cases...")
    
    ll = LinkedList()
    
    # Test operations on empty list
    try:
        ll.delete_first()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.delete_last()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.get(0)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.delete_at(0)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    # Test invalid indices
    ll.append(1)
    try:
        ll.get(-1)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.get(1)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.insert(-1, 'invalid')
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll.insert(2, 'invalid')
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    # Test single element operations
    ll = LinkedList()
    ll.append('only')
    assert ll.delete_first() == 'only'
    assert ll.is_empty() == True
    
    ll.append('only')
    assert ll.delete_last() == 'only'
    assert ll.is_empty() == True
    
    print("✓ Edge cases passed")


def test_search_operations():
    """Test search and access operations."""
    print("Testing search operations...")
    
    ll = LinkedList()
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    for item in data:
        ll.append(item)
    
    # Test find existing elements
    assert ll.find('apple') == 0
    
    assert ll.find('cherry') == 2
    print(ll,'idhar')
    assert ll.find('elderberry') == 4
    # Test find non-existing element
    assert ll.find('grape') == -1
    
    # Test get operations
    assert ll.get(0) == 'apple'
    assert ll.get(2) == 'cherry'
    assert ll.get(4) == 'elderberry'
    
    print("✓ Search operations passed")


def test_mixed_data_types():
    """Test support for mixed data types."""
    print("Testing mixed data types...")
    
    ll = LinkedList()
    mixed_data = [1, 'hello', 3.14, [1, 2, 3], {'key': 'value'}, None]
    
    for item in mixed_data:
        ll.append(item)
    
    assert ll.size() == 6
    assert ll.to_list() == mixed_data
    
    # Test operations with mixed types
    assert ll.find('hello') == 1
    assert ll.find(3.14) == 2
    assert ll.find(None) == 5
    
    print("✓ Mixed data types passed")


def test_reverse_operation():
    """Test the reverse operation."""
    print("Testing reverse operation...")
    
    # Test reverse on empty list
    ll = LinkedList()
    ll.reverse()
    assert ll.is_empty() == True
    
    # Test reverse on single element
    ll.append(1)
    ll.reverse()
    assert ll.to_list() == [1]
    
    # Test reverse on multiple elements
    ll = LinkedList()
    original = [1, 2, 3, 4, 5]
    for item in original:
        ll.append(item)
    print(ll,"hi") 
    
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]
    
    # Test reverse twice returns to original
    ll.reverse()
    assert ll.to_list() == original
    
    print("✓ Reverse operation passed")


def test_iteration_and_representation():
    """Test iteration and string representation."""
    print("Testing iteration and representation...")
    
    ll = LinkedList()
    data = ['a', 'b', 'c']
    for item in data:
        ll.append(item)
    
    # Test iteration
    result = []
    for item in ll:
        result.append(item)
    assert result == data
    
    # Test string representation
    assert "LinkedList:" in str(ll)
    assert "['a', 'b', 'c']" in str(ll)
    
    # Test len function
    assert len(ll) == 3
    
    # Test list conversion
    assert ll.to_list() == data
    
    print("✓ Iteration and representation passed")


def test_performance_scenarios():
    """Test performance-related scenarios."""
    print("Testing performance scenarios...")
    
    ll = LinkedList()
    
    # Test large number of prepends (should be fast - O(1) each)
    import time
    start = time.time()
    for i in range(1000):
        ll.prepend(i)
    prepend_time = time.time() - start
    
    # Test large number of appends (should be slower - O(n) each)
    ll2 = LinkedList()
    start = time.time()
    for i in range(1000):
        ll2.append(i)
    append_time = time.time() - start
    
    # Prepend should be significantly faster for large lists
    # (This is more of a demonstration than a strict test)
    print(f"  Prepend time: {prepend_time:.4f}s")
    print(f"  Append time: {append_time:.4f}s")
    
    # Test memory efficiency - nodes should only store data and next pointer
    node = Node("test")
    assert hasattr(node, 'data')
    assert hasattr(node, 'next')
    assert len(node.__dict__) == 2  # Only data and next attributes
    
    print("✓ Performance scenarios passed")


def run_all_tests():
    """Run the complete test suite."""
    print("Running Linked List Test Suite")
    print("=" * 40)
    
    test_functions = [
        test_basic_operations,
        test_insertion_operations,
        test_deletion_operations,
        test_edge_cases,
        test_search_operations,
        test_mixed_data_types,
        test_reverse_operation,
        test_iteration_and_representation,
        test_performance_scenarios
    ]
    
    for test_func in test_functions:
        try:
            test_func()
        except Exception as e:
            print(f"✗ {test_func.__name__} failed: {e}")
            return False
    
    print("\n" + "=" * 40)
    print("🎉 All tests passed! Your linked list implementation is working correctly.")
    print("\nPerformance Analysis:")
    print("- Prepend: O(1) - Most efficient insertion")
    print("- Append: O(n) - Must traverse to end, O(1) if using tail pointer")
    print("- Insert at index: O(n) - Must traverse to position")
    print("- Delete first: O(1) - Direct access")
    print("- Delete last: O(n) - Must find second-to-last, O(1) if maintained tail pointer")
    print("- Search: O(n) - Must check each node")
    print("- Access by index: O(n) - Must traverse to position")
    print("- Space complexity: O(1) extra space per node")
    
    return True


if __name__ == "__main__":
    # Uncomment the line below to run tests after implementation
    run_all_tests()
    