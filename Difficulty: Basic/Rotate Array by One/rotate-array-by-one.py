#User function Template for python3

class Solution:
    def rotate(self, arr):
        # Check if the array has more than one element
        if len(arr) > 1:
            # Move the last element to the front
            last_element = arr[-1]
            # Shift elements from right to left
            for i in range(len(arr) - 1, 0, -1):
                arr[i] = arr[i - 1]
            arr[0] = last_element

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends