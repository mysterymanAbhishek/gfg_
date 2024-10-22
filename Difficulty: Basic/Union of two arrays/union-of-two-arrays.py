#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        #code here
        union_set = set(a).union(set(b))
        return len(union_set)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))

# } Driver Code Ends