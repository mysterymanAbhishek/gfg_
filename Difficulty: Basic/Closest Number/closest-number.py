#User function Template for python3
class Solution:
    def closestNumber(self, N, M):
        # Candidate 1: Closest number <= N (rounding down)
        lower = (N // M) * M
        
        # Candidate 2: Closest number >= N (rounding up)
        if N % M == 0:
            higher = lower  # If N is already divisible by M, both are the same
        else:
            higher = (N // M + 1) * M
        
        # Compare the two candidates based on distance to N
        if abs(N - lower) < abs(N - higher):
            return lower
        elif abs(N - lower) > abs(N - higher):
            return higher
        else:
            # If both are equally close, return the one with the maximum absolute value
            if abs(lower) > abs(higher):
                return lower
            else:
                return higher

    
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))
# } Driver Code Ends