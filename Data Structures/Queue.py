"""
Queue Implementation Practice Problem
====================================

Your task is to implement a Queue data structure from scratch using two different approaches:
1. Array-based implementation (using Python list)
2. Linked-list-based implementation

A Queue follows the FIFO (First In, First Out) principle - elements are added at the rear
and removed from the front. Think of it like a line of people waiting for service.

Key Concepts:
- FIFO ordering: First element added is first to be removed
- Two main operations: enqueue (add) and dequeue (remove)
- Front and rear pointers to track ends
- Dynamic or fixed size depending on implementation
- Common applications: task scheduling, breadth-first search, buffering

Performance Characteristics:
- Array-based: Simple but may need resizing, potential O(n) operations
- Linked-list-based: Dynamic size, consistent O(1) operations, more memory overhead

Common Pitfalls to Avoid:
- Not handling empty queue operations
- Circular array indexing errors
- Memory leaks in linked implementation
- Not maintaining proper front/rear pointers
- Forgetting to update size counters
"""

class ArrayQueue:
    """
    Array-based Queue implementation using Python list.
    
    This implementation uses a Python list as the underlying storage with
    front and rear indices to avoid expensive list operations.
    
    Two approaches possible:
    1. Simple approach: Use list.pop(0) and list.append() - but pop(0) is O(n)
    2. Circular array approach: Use indices to avoid shifting - O(1) operations
    
    We'll implement the circular array approach for better performance.
    
    Time Complexities:
    - Enqueue: O(1) amortized (may need to resize)
    - Dequeue: O(1)
    - Peek: O(1)
    - Size: O(1)
    - Space: O(n) where n is the capacity
    """
    
    def __init__(self, capacity=10):
        """
        Initialize an empty queue with specified capacity.
        
        Args:
            capacity (int): Maximum number of elements the queue can hold
            
        The circular array approach uses:
        - front: index of the first element
        - rear: index where next element will be added
        - size: current number of elements
        - data: underlying array storage
        """
        # TODO: Initialize capacity, data array, front, rear, and size
        # Hint: rear should be (front + size) % capacity
        pass
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        # TODO: Check if size is 0
        pass
    
    def is_full(self):
        """
        Check if the queue is full.
        
        Returns:
            bool: True if queue is at capacity, False otherwise
            
        Time Complexity: O(1)
        """
        # TODO: Check if size equals capacity
        pass
    
    def size(self):
        """
        Get the current number of elements in the queue.
        
        Returns:
            int: Number of elements currently in the queue
            
        Time Complexity: O(1)
        """
        # TODO: Return the size counter
        pass
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        
        Args:
            item: The element to add (can be any type)
            
        Raises:
            OverflowError: If the queue is full
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        In circular array implementation:
        - Add item at rear index
        - Update rear = (rear + 1) % capacity
        - Increment size
        """
        # TODO: Check if queue is full
        # TODO: Add item at rear position
        # TODO: Update rear pointer using modular arithmetic
        # TODO: Increment size
        pass
    
    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        
        Returns:
            The element that was at the front of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        In circular array implementation:
        - Get item at front index
        - Update front = (front + 1) % capacity
        - Decrement size
        """
        # TODO: Check if queue is empty
        # TODO: Get item at front position
        # TODO: Update front pointer using modular arithmetic
        # TODO: Decrement size
        # TODO: Return the item
        pass
    
    def peek(self):
        """
        Return the front element without removing it.
        
        Returns:
            The element at the front of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Check if queue is empty
        # TODO: Return item at front position
        pass
    
    def clear(self):
        """
        Remove all elements from the queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Reset front, rear, and size
        # Optional: Clear data array elements
        pass
    
    def to_list(self):
        """
        Convert queue to a Python list in front-to-rear order.
        
        Returns:
            list: Elements in the queue from front to rear
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Useful for testing and debugging.
        """
        # TODO: Create list by traversing from front to rear
        # Hint: Use modular arithmetic to handle circular nature
        pass
    
    def __len__(self):
        """Enable len() function."""
        return self.size()
    
    def __str__(self):
        """
        String representation of the queue.
        
        Returns:
            str: String showing queue contents from front to rear
            
        Format: "Queue: [front -> 1, 2, 3 -> rear]"
        """
        # TODO: Convert to list and format appropriately
        pass
    
    def __iter__(self):
        """
        Make the queue iterable from front to rear.
        
        Yields:
            Elements in the queue from front to rear
        """
        # TODO: Yield elements from front to rear
        pass


class QueueNode:
    """
    A node for the linked-list-based queue implementation.
    
    Each node contains data and a reference to the next node.
    """
    
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in this node
        """
        self.data = data
        self.next = None


class LinkedQueue:
    """
    Linked-list-based Queue implementation.
    
    This implementation uses a linked list with front and rear pointers
    for efficient enqueue and dequeue operations.
    
    Advantages:
    - Dynamic size (no fixed capacity)
    - Consistent O(1) operations
    - No wasted space
    
    Disadvantages:
    - Extra memory overhead for pointers
    - Not cache-friendly due to scattered memory locations
    
    Time Complexities:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Peek: O(1)
    - Size: O(1)
    - Space: O(n) where n is the number of elements
    """
    
    def __init__(self):
        """
        Initialize an empty queue.
        
        Uses front and rear pointers for efficient operations:
        - front: points to the first node (for dequeue)
        - rear: points to the last node (for enqueue)
        - size: tracks number of elements
        """
        # TODO: Initialize front, rear pointers and size counter
        pass
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        # TODO: Check if front is None or size is 0
        pass
    
    def size(self):
        """
        Get the current number of elements in the queue.
        
        Returns:
            int: Number of elements in the queue
            
        Time Complexity: O(1)
        """
        # TODO: Return size counter
        pass
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        
        Args:
            item: The element to add
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Algorithm:
        1. Create new node
        2. If queue is empty, set both front and rear to new node
        3. Otherwise, link new node to rear and update rear pointer
        """
        # TODO: Create new node
        # TODO: Handle empty queue case
        # TODO: Link new node and update rear pointer
        # TODO: Increment size
        pass
    
    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        
        Returns:
            The element that was at the front
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Algorithm:
        1. Check if queue is empty
        2. Store front node's data
        3. Update front pointer to next node
        4. Handle case where queue becomes empty
        """
        # TODO: Check if queue is empty
        # TODO: Store data from front node
        # TODO: Update front pointer
        # TODO: Handle empty queue case (update rear)
        # TODO: Decrement size
        # TODO: Return stored data
        pass
    
    def peek(self):
        """
        Return the front element without removing it.
        
        Returns:
            The element at the front of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        # TODO: Check if queue is empty
        # TODO: Return front node's data
        pass
    
    def clear(self):
        """
        Remove all elements from the queue.
        
        Time Complexity: O(1)
        """
        # TODO: Reset front, rear, and size
        pass
    
    def to_list(self):
        """
        Convert queue to a Python list in front-to-rear order.
        
        Returns:
            list: Elements from front to rear
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Traverse from front to rear, collecting data
        pass
    
    def __len__(self):
        """Enable len() function."""
        return self.size()
    
    def __str__(self):
        """String representation of the queue."""
        # TODO: Convert to list and format
        pass
    
    def __iter__(self):
        """Make the queue iterable from front to rear."""
        # TODO: Traverse from front to rear, yielding data
        pass


# Comprehensive Test Suite
# ========================

def test_array_queue_basic_operations():
    """Test basic operations of ArrayQueue."""
    print("Testing ArrayQueue basic operations...")
    
    # Test initialization
    q = ArrayQueue(5)
    assert q.is_empty() == True
    assert q.is_full() == False
    assert q.size() == 0
    
    # Test enqueue
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    assert q.peek() == 1
    
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.peek() == 1  # Still first element
    
    # Test dequeue
    assert q.dequeue() == 1
    assert q.size() == 2
    assert q.peek() == 2
    
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() == True
    
    print("✓ ArrayQueue basic operations passed")


def test_linked_queue_basic_operations():
    """Test basic operations of LinkedQueue."""
    print("Testing LinkedQueue basic operations...")
    
    # Test initialization
    q = LinkedQueue()
    assert q.is_empty() == True
    assert q.size() == 0
    
    # Test enqueue
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    assert q.peek() == 1
    
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.peek() == 1
    
    # Test dequeue
    assert q.dequeue() == 1
    assert q.size() == 2
    assert q.peek() == 2
    
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() == True
    
    print("✓ LinkedQueue basic operations passed")


def test_queue_edge_cases():
    """Test edge cases for both queue implementations."""
    print("Testing queue edge cases...")
    
    for QueueClass in [ArrayQueue, LinkedQueue]:
        if QueueClass == ArrayQueue:
            q = QueueClass(3)
        else:
            q = QueueClass()
        
        # Test operations on empty queue
        try:
            q.dequeue()
            assert False, "Should raise IndexError"
        except IndexError:
            pass
        
        try:
            q.peek()
            assert False, "Should raise IndexError"
        except IndexError:
            pass
        
        # Test single element operations
        q.enqueue('only')
        assert q.peek() == 'only'
        assert q.dequeue() == 'only'
        assert q.is_empty() == True
        
        # Test ArrayQueue capacity limits
        if QueueClass == ArrayQueue:
            # Fill to capacity
            for i in range(3):
                q.enqueue(i)
            assert q.is_full() == True
            
            try:
                q.enqueue('overflow')
                assert False, "Should raise OverflowError"
            except OverflowError:
                pass
    
    print("✓ Queue edge cases passed")


def test_queue_fifo_behavior():
    """Test FIFO (First In, First Out) behavior."""
    print("Testing FIFO behavior...")
    
    for QueueClass in [ArrayQueue, LinkedQueue]:
        if QueueClass == ArrayQueue:
            q = QueueClass(10)
        else:
            q = QueueClass()
        
        # Enqueue elements
        elements = ['first', 'second', 'third', 'fourth']
        for elem in elements:
            q.enqueue(elem)
        
        # Dequeue should return in same order
        result = []
        while not q.is_empty():
            result.append(q.dequeue())
        
        assert result == elements
        
        # Test mixed operations
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
    
    print("✓ FIFO behavior passed")


def test_queue_circular_array_behavior():
    """Test circular array behavior in ArrayQueue."""
    print("Testing circular array behavior...")
    
    q = ArrayQueue(3)
    
    # Fill queue
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    # Dequeue and enqueue to test circular behavior
    assert q.dequeue() == 1
    q.enqueue(4)
    
    assert q.dequeue() == 2
    q.enqueue(5)
    
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5
    
    # Test wrap-around multiple times
    for i in range(10):
        q.enqueue(i)
        assert q.dequeue() == i
    
    print("✓ Circular array behavior passed")


def test_queue_mixed_data_types():
    """Test support for mixed data types."""
    print("Testing mixed data types...")
    
    for QueueClass in [ArrayQueue, LinkedQueue]:
        if QueueClass == ArrayQueue:
            q = QueueClass(10)
        else:
            q = QueueClass()
        
        mixed_data = [1, 'hello', 3.14, [1, 2, 3], {'key': 'value'}, None]
        
        for item in mixed_data:
            q.enqueue(item)
        
        result = []
        while not q.is_empty():
            result.append(q.dequeue())
        
        assert result == mixed_data
    
    print("✓ Mixed data types passed")


def test_queue_iteration_and_representation():
    """Test iteration and string representation."""
    print("Testing iteration and representation...")
    
    for QueueClass in [ArrayQueue, LinkedQueue]:
        if QueueClass == ArrayQueue:
            q = QueueClass(10)
        else:
            q = QueueClass()
        
        data = ['a', 'b', 'c']
        for item in data:
            q.enqueue(item)
        
        # Test iteration
        result = list(q)
        assert result == data
        
        # Test string representation
        str_repr = str(q)
        assert "Queue:" in str_repr
        for item in data:
            assert str(item) in str_repr
        
        # Test len function
        assert len(q) == 3
        
        # Test to_list conversion
        assert q.to_list() == data
    
    print("✓ Iteration and representation passed")


def test_queue_clear_operation():
    """Test clear operation."""
    print("Testing clear operation...")
    
    for QueueClass in [ArrayQueue, LinkedQueue]:
        if QueueClass == ArrayQueue:
            q = QueueClass(10)
        else:
            q = QueueClass()
        
        # Add elements
        for i in range(5):
            q.enqueue(i)
        
        assert q.size() == 5
        assert not q.is_empty()
        
        # Clear queue
        q.clear()
        assert q.size() == 0
        assert q.is_empty()
        
        # Test that queue works after clearing
        q.enqueue('after_clear')
        assert q.peek() == 'after_clear'
        assert q.dequeue() == 'after_clear'
    
    print("✓ Clear operation passed")


def test_queue_performance_comparison():
    """Test performance characteristics of both implementations."""
    print("Testing performance comparison...")
    
    import time
    
    # Test enqueue performance
    print("  Performance comparison (1000 operations):")
    
    # ArrayQueue performance
    start = time.time()
    aq = ArrayQueue(1000)
    for i in range(1000):
        aq.enqueue(i)
    for i in range(1000):
        aq.dequeue()
    array_time = time.time() - start
    
    # LinkedQueue performance
    start = time.time()
    lq = LinkedQueue()
    for i in range(1000):
        lq.enqueue(i)
    for i in range(1000):
        lq.dequeue()
    linked_time = time.time() - start
    
    print(f"    ArrayQueue: {array_time:.4f}s")
    print(f"    LinkedQueue: {linked_time:.4f}s")
    
    # Test memory usage comparison
    import sys
    
    # Memory usage of nodes
    node = QueueNode("test")
    print(f"    QueueNode memory: {sys.getsizeof(node) + sys.getsizeof(node.data)}bytes")
    
    # Memory usage of array elements
    arr = [None] * 100
    print(f"    Array element memory: {sys.getsizeof(arr) // 100}bytes per element")
    
    print("✓ Performance comparison completed")


def test_queue_capacity_management():
    """Test capacity management in ArrayQueue."""
    print("Testing capacity management...")
    
    q = ArrayQueue(2)
    
    # Test initial capacity
    assert q.is_empty() == True
    assert q.is_full() == False
    
    # Fill to capacity
    q.enqueue(1)
    assert q.is_full() == False
    
    q.enqueue(2)
    assert q.is_full() == True
    
    # Test overflow
    try:
        q.enqueue(3)
        assert False, "Should raise OverflowError"
    except OverflowError:
        pass
    
    # Test that dequeue frees space
    q.dequeue()
    assert q.is_full() == False
    
    # Can enqueue again
    q.enqueue(3)
    assert q.is_full() == True
    
    print("✓ Capacity management passed")


def run_all_tests():
    """Run the complete test suite."""
    print("Running Queue Implementation Test Suite")
    print("=" * 50)
    
    test_functions = [
        test_array_queue_basic_operations,
        test_linked_queue_basic_operations,
        test_queue_edge_cases,
        test_queue_fifo_behavior,
        test_queue_circular_array_behavior,
        test_queue_mixed_data_types,
        test_queue_iteration_and_representation,
        test_queue_clear_operation,
        test_queue_performance_comparison,
        test_queue_capacity_management
    ]
    
    passed = 0
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} failed: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{passed}/{len(test_functions)} tests passed")
    
    if passed == len(test_functions):
        print("\n" + "=" * 50)
        print("🎉 All tests passed! Your queue implementations are working correctly.")
        print("\nImplementation Comparison:")
        print("ArrayQueue:")
        print("  ✓ Fast access with indices")
        print("  ✓ Cache-friendly memory layout")
        print("  ✓ Fixed memory overhead")
        print("  ✗ Fixed capacity limit")
        print("  ✗ Potential memory waste")
        
        print("\nLinkedQueue:")
        print("  ✓ Dynamic size")
        print("  ✓ No capacity limits")
        print("  ✓ Efficient memory usage")
        print("  ✗ Extra memory for pointers")
        print("  ✗ Less cache-friendly")
        
        print("\nTime Complexities (Both):")
        print("  • Enqueue: O(1)")
        print("  • Dequeue: O(1)")
        print("  • Peek: O(1)")
        print("  • Size: O(1)")
        print("  • Clear: O(1)")
        
        print("\nCommon Applications:")
        print("  • Task scheduling in operating systems")
        print("  • Breadth-first search in graphs")
        print("  • Handling requests in web servers")
        print("  • Buffer for data streams")
        print("  • Print job management")
    
    return passed == len(test_functions)


if __name__ == "__main__":
    # Uncomment the line below to run tests after implementation
    # run_all_tests()
    
    # Example usage after implementation:
    print("\nExample Usage:")
    print("# Array-based queue")
    print("aq = ArrayQueue(5)")
    print("aq.enqueue('first')")
    print("aq.enqueue('second')")
    print("print(aq.dequeue())  # 'first'")
    print("print(aq.peek())     # 'second'")
    print()
    print("# Linked-list-based queue")
    print("lq = LinkedQueue()")
    print("lq.enqueue(1)")
    print("lq.enqueue(2)")
    print("print(list(lq))      # [1, 2]")
    print("print(len(lq))       # 2")