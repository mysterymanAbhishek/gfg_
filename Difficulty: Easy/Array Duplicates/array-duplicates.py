from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        # Create a list to keep track of occurrences
        count = [0] * n
        result = []
        
        # Count the occurrences of each element
        for num in arr:
            count[num] += 1
        
        # Find the elements that occur more than once
        for i in range(n):
            if count[i] > 1:
                result.append(i)
        
        # If no duplicates found, return [-1]
        if len(result) == 0:
            return [-1]
        
        return result

        # code here
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends