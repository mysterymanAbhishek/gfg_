#User function Template for python3

class Solution:
    def isParenthesisBalanced(self, s):
        stack = []
        # Dictionary to match opening and closing brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the string s
        for char in s:
            # If it's an opening bracket, push to stack
            if char in matching_bracket.values():
                stack.append(char)
            # If it's a closing bracket, check for matching opening bracket
            elif char in matching_bracket:
                # Check if stack is not empty and if top element matches
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
        # Return True if stack is empty (balanced), False otherwise
        return len(stack) == 0

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.isParenthesisBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends