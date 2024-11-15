#User function Template for python3

import math

class Solution:
    def lcmAndGcd(self, a, b):
        gcd_val = math.gcd(a, b)
        lcm_val = (a * b) // gcd_val  # Use the GCD to calculate LCM
        return [lcm_val, gcd_val]

        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
        print("~")

# } Driver Code Ends