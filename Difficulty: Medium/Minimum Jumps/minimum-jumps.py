class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If there's only one element, no jumps are needed
        if n == 1:
            return 0
        
        # If the first element is 0, we can't move anywhere
        if arr[0] == 0:
            return -1
        
        jumps = 0
        current_jump_end = 0
        max_reachable = 0

        for i in range(n - 1):  # No need to check the last element
            # Update the maximum reachable index from this point
            max_reachable = max(max_reachable, i + arr[i])
            
            # If we can reach or exceed the last index, return the jump count
            if max_reachable >= n - 1:
                return jumps + 1
            
            # If we reach the end of the current jump range, increment jump count
            if i == current_jump_end:
                jumps += 1
                current_jump_end = max_reachable

            # If current_jump_end hasn't progressed, we can't reach the end
            if current_jump_end <= i:
                return -1
        
        return -1  # If we exit the loop, reaching the end was impossible




#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends