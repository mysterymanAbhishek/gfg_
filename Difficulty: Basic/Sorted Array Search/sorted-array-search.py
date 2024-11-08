#User function Template for python3

class Solution:
    def searchInSorted(self, arr, k):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends