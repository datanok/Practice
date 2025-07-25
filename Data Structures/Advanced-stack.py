from Stack import Stack
import re

class AdvancedStackProblems:
    def __init__(self):
        self.stack = Stack()
    
    def clear_stack(self):
        """Clear the stack for next problem"""
        self.stack = Stack()

    # ========== ADVANCED STACK PROBLEMS ==========
    
    def infix_to_postfix(self, expression):
        """Problem 11: Convert infix expression to postfix
        
        Convert infix notation (2 + 3 * 4) to postfix (2 3 4 * +)
        Handle operator precedence: ^(right assoc) > */  > +-
        Handle parentheses correctly
        
        Examples:
        - "2 + 3 * 4" → "2 3 4 * +"
        - "(2 + 3) * 4" → "2 3 + 4 *"
        - "2 ^ 3 ^ 2" → "2 3 2 ^ ^"
        """
        # TODO: Implement infix to postfix conversion
        # Hint: Use stack for operators, consider precedence and associativity
        pass
    
    def evaluate_infix(self, expression):
        """Problem 12: Evaluate infix expression directly
        
        Evaluate infix expressions like "2 + 3 * 4" = 14
        Handle operator precedence and parentheses
        
        Examples:
        - "2 + 3 * 4" → 14
        - "(2 + 3) * 4" → 20
        - "10 - 2 * 3" → 4
        """
        # TODO: Implement infix expression evaluation
        # Hint: Use two stacks - one for numbers, one for operators
        pass
    
    def stack_with_min(self):
        """Problem 13: Design stack with getMin() in O(1)
        
        Design a stack that supports push, pop, top, and getMin in O(1) time
        Return a custom class that maintains minimum element efficiently
        
        Operations:
        - push(x): Push element x onto stack
        - pop(): Remove top element
        - top(): Get top element
        - getMin(): Get minimum element in O(1)
        """
        # TODO: Return a custom MinStack class
        # Hint: Use auxiliary stack to track minimums
        
        class MinStack:
            def __init__(self):
                # TODO: Initialize your data structures
                self.array = []
                self.minStack = []
            
            def push(self, val):
                # TODO: Push val and update min tracking
                self.array.append(val)
                if not self.minStack or self.minStack[-1] >= val:
                    self.minStack.append(val)
            
            def pop(self):
                # TODO: Pop and update min tracking
                
                val = self.array.pop()
                if val == self.minStack[-1]:
                    self.minStack.pop()
                return val

            
            def top(self):
                # TODO: Return top element
                return self.array[-1]
                
            
            def getMin(self):
                # TODO: Return minimum in O(1)
                return self.minStack[-1]
        
        return MinStack()
    
    def trapping_rain_water(self, height):
        """Problem 14: Trapping Rain Water using Stack
        
        Given elevation map, calculate trapped rainwater
        Use stack-based approach (alternative to two-pointer method)
        
        Examples:
        - [0,1,0,2,1,0,1,3,2,1,2,1] → 6
        - [4,2,0,3,2,5] → 9
        """
        # TODO: Implement using stack approach
        # Hint: Stack stores indices, calculate water when popping
        pass
    
    def asteroid_collision(self, asteroids):
        """Problem 15: Asteroid Collision
        
        Asteroids move right (+) or left (-). When they collide:
        - Smaller explodes, larger continues
        - Same size: both explode
        - No collision if moving in same direction or away from each other
        
        Examples:
        - [5, 10, -5] → [5, 10] (10 destroys -5)
        - [8, -8] → [] (both explode)
        - [10, 2, -5] → [10] (10 destroys -5, then 2)
        """
        # TODO: Simulate asteroid collisions using stack
        pass
    
    def decode_string(self, s):
        """Problem 16: Decode String
        
        Decode strings like "3[a2[c]]" → "accaccacc"
        Handle nested brackets and multipliers
        
        Examples:
        - "3[a]2[bc]" → "aaabcbc"
        - "2[abc]3[cd]ef" → "abcabccdcdcdef"
        - "abc3[cd]xyz" → "abccdcdcdxyz"
        """
        # TODO: Use stack to handle nested structure
        # Hint: Stack can store both numbers and partial strings
        pass
    
    def exclusive_time_functions(self, n, logs):
        """Problem 17: Exclusive Time of Functions
        
        Given function call logs, calculate exclusive execution time
        Logs format: ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
        
        Examples:
        - n=2, logs=["0:start:0","1:start:2","1:end:5","0:end:6"] → [3,4]
        """
        # TODO: Use stack to track function call hierarchy
        # Hint: Stack stores function IDs and their start times
        pass
    
    def verify_preorder_serialization(self, preorder):
        """Problem 18: Verify Preorder Serialization of Binary Tree
        
        Check if preorder traversal string represents valid binary tree
        '#' represents null nodes
        
        Examples:
        - "9,3,4,#,#,1,#,#,2,#,6,#,#" → True
        - "1,#" → False
        - "9,#,#,1" → False
        """
        # TODO: Use stack to verify tree structure
        # Hint: Track available slots for children
        pass
    
    def longest_valid_parentheses(self, s):
        """Problem 19: Longest Valid Parentheses
        
        Find length of longest valid parentheses substring
        
        Examples:
        - "(()" → 2
        - ")()())" → 4
        - "()(()" → 2
        """
        # TODO: Use stack to track indices of unmatched parentheses
        pass
    
    def maximal_rectangle(self, matrix):
        """Problem 20: Maximal Rectangle in Binary Matrix
        
        Find largest rectangle containing only 1's in binary matrix
        Extension of largest rectangle in histogram
        
        Examples:
        - [["1","0","1","0","0"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"],
           ["1","0","0","1","0"]] → 6
        """
        # TODO: Use histogram approach for each row
        # Hint: Convert each row to histogram heights, then use largest_rectangle_histogram
        pass
    
    def sliding_window_maximum(self, nums, k):
        """Problem 21: Sliding Window Maximum using Deque/Stack
        
        Find maximum in each sliding window of size k
        Use monotonic deque approach (can simulate with two stacks)
        
        Examples:
        - nums=[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]
        """
        # TODO: Implement using stack-based approach or deque simulation
        pass
    
    def remove_duplicate_letters(self, s):
        """Problem 22: Remove Duplicate Letters
        
        Remove duplicate letters so result is smallest lexicographically
        Each letter appears exactly once in result
        
        Examples:
        - "bcabc" → "abc"
        - "cbacdcbc" → "acdb"
        """
        # TODO: Use stack with greedy approach
        # Hint: Track last occurrence of each character
        pass
    
    def basic_calculator(self, s):
        """Problem 23: Basic Calculator
        
        Evaluate expression with +, -, (, ) and spaces
        No multiplication or division
        
        Examples:
        - "1 + 1" → 2
        - " 2-1 + 2 " → 3
        - "(1+(4+5+2)-3)+(6+8)" → 23
        """
        # TODO: Handle parentheses with stack
        pass
    
    def basic_calculator_ii(self, s):
        """Problem 24: Basic Calculator II
        
        Evaluate expression with +, -, *, / and spaces
        No parentheses
        
        Examples:
        - "3+2*2" → 7
        - " 3/2 " → 1
        - " 3+5 / 2 " → 5
        """
        # TODO: Use stack to handle operator precedence
        pass
    
    def score_of_parentheses(self, s):
        """Problem 25: Score of Parentheses
        
        Calculate score: "()" = 1, "(A)" = 2*score(A), "AB" = score(A)+score(B)
        
        Examples:
        - "()" → 1
        - "(())" → 2
        - "()()" → 2
        - "(()(()))" → 6
        """
        # TODO: Use stack to track nested scores
        pass


def test_advanced_problems():
    """Test cases for advanced stack problems"""
    solver = AdvancedStackProblems()

    # Test data with expected outputs
    test_cases = {
        "infix_to_postfix": [
            ("2 + 3 * 4", "2 3 4 * +"),
            ("(2 + 3) * 4", "2 3 + 4 *"),
            ("2 ^ 3 ^ 2", "2 3 2 ^ ^"),
            ("a + b * c - d", "a b c * + d -")
        ],
        "evaluate_infix": [
            ("2 + 3 * 4", 14),
            ("(2 + 3) * 4", 20),
            ("10 - 2 * 3", 4),
            ("2 + 3 - 1", 4)
        ],
        "trapping_rain_water": [
            ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
            ([4,2,0,3,2,5], 9),
            ([3,0,2,0,4], 7)
        ],
        "asteroid_collision": [
            ([5, 10, -5], [5, 10]),
            ([8, -8], []),
            ([10, 2, -5], [10]),
            ([-2, -1, 1, 2], [-2, -1, 1, 2])
        ],
        "decode_string": [
            ("3[a]2[bc]", "aaabcbc"),
            ("2[abc]3[cd]ef", "abcabccdcdcdef"),
            ("abc3[cd]xyz", "abccdcdcdxyz"),
            ("3[a2[c]]", "accaccacc")
        ],
        "longest_valid_parentheses": [
            ("(()", 2),
            (")()())", 4),
            ("()(()", 2),
            ("", 0)
        ],
        "remove_duplicate_letters": [
            ("bcabc", "abc"),
            ("cbacdcbc", "acdb"),
            ("ecbacba", "eacb")
        ],
        "basic_calculator": [
            ("1 + 1", 2),
            (" 2-1 + 2 ", 3),
            ("(1+(4+5+2)-3)+(6+8)", 23)
        ],
        "basic_calculator_ii": [
            ("3+2*2", 7),
            (" 3/2 ", 1),
            (" 3+5 / 2 ", 5)
        ],
        "score_of_parentheses": [
            ("()", 1),
            ("(())", 2),
            ("()()", 2),
            ("(()(()))", 6)
        ]
    }

    # MinStack special test
    print("=== Testing: stack_with_min ===")
    min_stack = solver.stack_with_min()

    try:
        # Test Case 1: Basic push and getMin
        min_stack.push(2)
        min_stack.push(0)
        min_stack.push(-3)
        min1 = min_stack.getMin()  # Should return -3
        min_stack.pop()
        top = min_stack.top()      # Should return 0
        min_stack.push(-2)
        min2 = min_stack.getMin()  # Should return -2
        print(f"Test 1 - min1={min1}, top={top}, min2={min2}")
        print("Expected: min1=-3, top=0, min2=-2\n")

        # Test Case 2: Push increasing elements
        min_stack = solver.stack_with_min()
        min_stack.push(1)
        min_stack.push(2)
        min_stack.push(3)
        print("Test 2 - getMin():", min_stack.getMin())  # Expected: 1
        min_stack.pop()
        print("Test 2 - top():", min_stack.top())        # Expected: 2
        print("Test 2 - getMin():", min_stack.getMin())  # Expected: 1
        print()

        # Test Case 3: Push decreasing elements
        min_stack = solver.stack_with_min()
        min_stack.push(3)
        min_stack.push(2)
        min_stack.push(1)
        print("Test 3 - getMin():", min_stack.getMin())  # Expected: 1
        min_stack.pop()
        print("Test 3 - getMin():", min_stack.getMin())  # Expected: 2
        print()

        # Test Case 4: Repeated minimum values
        min_stack = solver.stack_with_min()
        min_stack.push(5)
        min_stack.push(1)
        min_stack.push(1)
        min_stack.push(2)
        print("Test 4 - getMin():", min_stack.getMin())  # Expected: 1
        min_stack.pop()  # Removes 2
        min_stack.pop()  # Removes 1
        print("Test 4 - getMin():", min_stack.getMin())  # Expected: 1
        min_stack.pop()  # Removes 1
        print("Test 4 - getMin():", min_stack.getMin())  # Expected: 5
        print()

        # Test Case 5: Edge case - pop from single-element stack
        min_stack = solver.stack_with_min()
        min_stack.push(10)
        print("Test 5 - getMin():", min_stack.getMin())  # Expected: 10
        min_stack.pop()
        print("Test 5 - Stack emptied.")
        try:
            print("Test 5 - getMin():", min_stack.getMin())  # Should be handled gracefully
        except IndexError:
            print("Test 5 - getMin() raised IndexError as expected.")
        print()

    except Exception as e:
        print("Test failed:", str(e))

    print("-" * 50)

    # Run other test cases
    total_tests = 0
    passed_tests = 0

    for problem_name, test_data in test_cases.items():
        print(f"\n=== Testing: {problem_name} ===")
        method = getattr(solver, problem_name, None)
        
        if method is None:
            print(f"Method {problem_name} not found!")
            continue

        for i, test in enumerate(test_data):
            total_tests += 1
            if isinstance(test, tuple) and len(test) == 2:
                input_data, expected = test
            else:
                input_data, expected = test, None
            
            test_args = input_data if isinstance(input_data, tuple) else (input_data,)

            try:
                result = method(*test_args)
                if expected is not None:
                    if result == expected:
                        print(f"Test {i+1}: ✅ PASS")
                        passed_tests += 1
                    else:
                        print(f"Test {i+1}: ❌ FAIL")
                        print(f"   Input: {input_data}")
                        print(f"   Expected: {expected}")
                        print(f"   Got: {result}")
                else:
                    print(f"Test {i+1}: Result: {result}")
                    passed_tests += 1  # Count as pass if no expected result
            except Exception as e:
                print(f"Test {i+1}: ❌ ERROR")
                print(f"   Input: {input_data}")
                print(f"   Exception: {e}")
        print("-" * 50)

    print(f"\nTotal: {total_tests} | Passed: {passed_tests} | Failed: {total_tests - passed_tests}")

if __name__ == "__main__":
    test_advanced_problems()