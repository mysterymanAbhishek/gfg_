#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        # Step 1: Find a candidate for majority element
        candidate = None
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Step 2: Verify if the candidate is the majority element
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        else:
            return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends