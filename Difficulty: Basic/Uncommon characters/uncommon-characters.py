#User function Template for py
class Solution:
    def UncommonChars(self, A: str, B: str) -> str:
        # Use sets to store unique characters in A and B
        set_A = set(A)
        set_B = set(B)
        
        # Find characters that are in either set_A or set_B but not both
        uncommon = (set_A ^ set_B)  # Symmetric difference

        # If there are no uncommon characters, return "-1"
        if not uncommon:
            return "-1"

        # Return the sorted result as a string
        return ''.join(sorted(uncommon))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

        print("~")
# } Driver Code Ends