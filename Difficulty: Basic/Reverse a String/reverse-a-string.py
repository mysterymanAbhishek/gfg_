#User function Template for python3

class Solution:
    def reverseString(self, s):
        # Reverse the string using slicing
        return s[::-1]

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends