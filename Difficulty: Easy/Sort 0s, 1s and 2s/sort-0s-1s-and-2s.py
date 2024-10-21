class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr)
        c0 = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)
        
        for i in range(n):
            if c0 != 0:
                arr[i] = 0
                c0 -= 1
            elif c1 != 0:
                arr[i] = 1
                c1 -= 1
            else:
                arr[i] = 2
        return arr

        # code here


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends