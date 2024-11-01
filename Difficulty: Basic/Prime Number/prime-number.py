#User function Template for python3

class Solution:
    def isPrime(self, n: int) -> int:
        # Handle base cases
        if n <= 1:
            return 0  # 0 and 1 are not prime numbers
        if n <= 3:
            return 1  # 2 and 3 are prime numbers
        
        # Check for even numbers and multiples of 3
        if n % 2 == 0 or n % 3 == 0:
            return 0  # Not prime if divisible by 2 or 3
        
        # Check for factors from 5 to sqrt(n)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return 0  # Not prime if divisible by any number
            i += 6  # Check only numbers of the form 6k ± 1
        
        return 1  # n is prime

# This class should be tested in a competitive programming environment
# where the input is given, and the output is checked automatically.

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
        print("~")
# } Driver Code Ends