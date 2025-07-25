from Stack import Stack
class StackProblems:
    def __init__(self):
        self.stack = Stack()
    
    def clear_stack(self):
        """Clear the stack for next problem"""
        self.stack = Stack()
    
    def reverse_string(self, input_str):
        """Problem 1: Reverse a string using stack"""
        self.clear_stack()
        for i in input_str:
            self.stack.push(i)
        inp_arr = list(input_str)
        for i in range(len(input_str)):
            inp_arr[i] = self.stack.pop()
        return ''.join(inp_arr)
    
    def balanced_parentheses(self, s):
        """Problem 2: Check if parentheses ()[]{} are balanced"""
        self.clear_stack()
        bracketMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in range(len(s)):
            if s[i] not in  bracketMap:
                self.stack.push(s[i])
            else:
                if self.stack.is_empty() or self.stack.peek() != bracketMap[s[i]]:
                    return False
                else:
                    self.stack.pop()
        return self.stack.is_empty()
   
    def remove_adjacent_duplicates(self, s):
        """Problem 3: Remove adjacent duplicate characters"""
        self.clear_stack()
        for i in range(len(s)):
            if not self.stack.is_empty() and s[i] == self.stack.peek():
                self.stack.pop()
            else:
                self.stack.push(s[i])
        return ''.join(self.stack.array)
    
    def next_greater_element(self, nums):
        """Problem 4: Find next greater element for each number"""
        self.clear_stack()
        # TODO: Implement next greater element logic
        # Hint: Use stack to store indices, not values
        # Process array left to right, pop indices when current element is greater
        res = [-1] * len(nums)
        
        numToIdx = { n:i for i,n in enumerate(nums)}
        for i  in range(len(nums)):
            while not self.stack.is_empty() and (self.stack.peek() < nums[i]):
                ele = self.stack.pop()
                idx = numToIdx[ele]
                res[idx] = nums[i]
            self.stack.push(nums[i])
        return res
  
    def evaluate_postfix(self, expression):
        """Problem 5: Evaluate postfix expression like '2 3 + 4 *'"""
        self.clear_stack()

        def calc(op,num1,num2):
            res = {
                '+' : int(num1)+ int(num2),
                '-' : int(num1)- int(num2),
                '*' : int(num1)* int(num2),
                '/' : int(num1) // int(num2)
            }
            return res[op]

        for i in expression.split():
            if i.isdigit():
                self.stack.push(i)
            else:
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.push(calc(i,op1,op2))

        return int(self.stack.peek())
                 
    def daily_temperatures(self, temperatures):
        """Problem 6: Days until warmer temperature"""
        self.clear_stack()
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while not self.stack.is_empty() and self.stack.peek()[0] < temp:
                stackTemp, stackIdx = self.stack.pop()
                days  = i - stackIdx
                res[stackIdx] = days
            self.stack.push([temp,i])
        return res            
            
               
    def valid_parentheses_simple(self, s):
        """Problem 7: Check if string has valid parentheses (only '(' and ')')"""
        self.clear_stack()
        map = { '(':1}
        
        for i in s:
            if i in map:
                self.stack.push(i)
        return (self.stack.size() * 2 ) == len(s)
   
    def baseball_game(self, operations):
        """Problem 8: Calculate baseball game score"""
        self.clear_stack()
        for op in operations:
            if op == '+':
                self.stack.push(self.stack.peekFromEnd(1)+self.stack.peekFromEnd(2))
            elif op == "D":
                res = self.stack.peek() * 2
                self.stack.push(res)
            elif op == "C":
                self.stack.pop()
            else:
                self.stack.push(int(op))
            
        return sum(self.stack.getArray())


    
    def remove_k_digits(self, num, k):
        """Problem 9: Remove k digits to make smallest number"""
        self.clear_stack()
        # TODO: Implement k digits removal
        for digit in num:
            while not self.stack.is_empty() and k>0 and self.stack.peek() > digit :
                self.stack.pop()
                k-=1
            self.stack.push(digit)
        while k>0:
            self.stack.pop()
            k -=1 
        result = ''.join(self.stack.getArray()).lstrip("0")
        return result if result else "0"



    
    def largest_rectangle_histogram(self, heights):
        """Problem 10: Find largest rectangle area in histogram"""
        self.clear_stack()
        # TODO: Implement largest rectangle logic
        pass


def test_problems():
    solver = StackProblems()

    # Test data with optional expected outputs (if known)
    test_cases = {
        "reverse_string": [
            ("hello", "olleh"),
            ("world", "dlrow"),
            ("stack", "kcats")
        ],
        "balanced_parentheses": [
            ("(())", True),
            ("()[]{}", True),
            ("([)]", False),
            ("{[()]}", True),
            ("(((", False)
        ],
        "remove_adjacent_duplicates": [
            ("abbaca", "ca"),
            ("azxxzy", "ay"),
            ("aabbcc", "")
        ],
        "next_greater_element": [
            ([1, 3, 2, 4], [3, 4, 4, -1]),
            ([2, 1, 3, 4, 5], [3, 3, 4, 5, -1]),
            ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1])
        ],
        "evaluate_postfix": [
            ("2 3 +", 5),
            ("2 3 + 4 *", 20),
            ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5)
        ],
        "daily_temperatures": [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0])
        ],
        "valid_parentheses_simple": [
            ("()", True),
            ("(()", False),
            ("())", False),
            ("(())", True)
        ],
        "baseball_game": [
            (["5", "2", "C", "D", "+"], 30),
            (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
            (["1", "C"], 0)
        ],
        "remove_k_digits": [
            (("1432219", 3), "1219"),
            (("10200", 1), "200"),
            (("10", 2), "0")
        ],
        "largest_rectangle_histogram": [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([1, 2, 3, 4, 5], 9)
        ]
    }

    # Run all test cases
    total_tests = 0
    passed_tests = 0

    for problem_name, test_data in test_cases.items():
        print(f"\n=== Testing: {problem_name} ===")
        method = getattr(solver, problem_name)

        for i, test in enumerate(test_data):
            total_tests += 1
            input_data, expected = test if isinstance(test, tuple) and not isinstance(test[0], (list, str, tuple)) else (test[0], test[1])
            test_args = input_data if isinstance(input_data, tuple) else (input_data,)

            try:
                result = method(*test_args)
                if result == expected:
                    print(f"Test {i+1}: ✅ PASS")
                else:
                    print(f"Test {i+1}: ❌ FAIL")
                    print(f"   Input: {input_data}")
                    print(f"   Expected: {expected}")
                    print(f"   Got: {result}")
                passed_tests += (result == expected)
            except Exception as e:
                print(f"Test {i+1}: ❌ ERROR")
                print(f"   Input: {input_data}")
                print(f"   Exception: {e}")
        print("-" * 50)

    
   
    print(f"\nTotal: {total_tests} | Passed: {passed_tests} | Failed: {total_tests - passed_tests}")

if __name__ == "__main__":
    test_problems()
