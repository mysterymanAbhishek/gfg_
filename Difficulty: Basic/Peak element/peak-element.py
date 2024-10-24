# your task is to complete this function
# function should return index to the any valid peak element
class Solution:
    def peakElement(self, arr, n):
        left = 0
        right = n - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with its next element
            if arr[mid] < arr[mid + 1]:
                left = mid + 1  # Move to the right half
            else:
                right = mid  # Move to the left half

        # When left == right, it must be the peak element
        return left

        # Code here



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends