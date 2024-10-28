class Solution:
    def leaders(self, arr):
        # Initialize variables
        n = len(arr)
        leaders = []
        
        # Start with the rightmost element as a leader
        max_from_right = arr[-1]
        leaders.append(max_from_right)
        
        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders.append(arr[i])
                max_from_right = arr[i]
        
        # Return reversed list to maintain left-to-right order
        return leaders[::-1]

        # code here


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

# } Driver Code Ends