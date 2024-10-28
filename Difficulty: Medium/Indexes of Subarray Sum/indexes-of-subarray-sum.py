#User function Template for python3
class Solution:
    def subArraySum(self, arr, target):
        left = 0
        current_sum = 0
        
        for right in range(len(arr)):
            # Add the current element to the current_sum
            current_sum += arr[right]
            
            # Adjust the left pointer until current_sum <= target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            # Check if we found the target sum
            if current_sum == target:
                return [left + 1, right + 1]  # 1-based index

        # If we finish the loop without finding the subarray
        return [-1]  # Return list containing -1 to ensure consistency in output format

        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subArraySum(arr, d)
        print(" ".join(map(str,
                           result)))  # Print the result in the desired format
        tc -= 1
        print("~")

# } Driver Code Ends