#User function Template for python3

class Solution:
    def search(self, arr, x):
        # Traverse the array
        for i in range(len(arr)):
            if arr[i] == x:
                return i  # Return the index if found
        
        return -1  # Return -1 if not found



        #Your code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input().strip())
    while T > 0:
        A = [int(x) for x in input().strip().split()]
        x = int(input().strip())
        ob = Solution()
        print(ob.search(A, x))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends