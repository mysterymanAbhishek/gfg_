#User function Template for python3

class Solution:
    def printFibb(self, N: int) -> list:
        # Handle edge cases
        if N <= 0:
            return []
        elif N == 1:
            return [1]
        elif N == 2:
            return [1, 1]

        # Initialize the Fibonacci list
        fib = [1, 1]  # Start with the first two Fibonacci numbers

        # Generate Fibonacci numbers up to N
        for i in range(2, N):
            next_fib = fib[i - 1] + fib[i - 2]  # Calculate the next Fibonacci number
            fib.append(next_fib)  # Append to the list

        return fib





#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends