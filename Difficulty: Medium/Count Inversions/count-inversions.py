class Solution:
    def inversionCount(self, arr):
        # Helper function to count inversions and sort the array
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be sorted
            inv_count = 0
            
            # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    # There are mid - i inversions, because all elements left to i in the left subarray
                    # are greater than arr[j]
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            # Copy the remaining elements of left subarray, if any
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right subarray, if any
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into the original array
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
                
            return inv_count

        # Helper function to divide the array into halves and count inversions
        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
                inv_count += merge_and_count(arr, temp_arr, left, mid, right)

            return inv_count

        # Initialize temporary array and count inversions
        temp_arr = [0] * len(arr)
        return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # Your Code Here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends