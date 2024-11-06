#User function Template for python3

class Solution:
    def getPairs(self, arr):
        arr.sort()  # Sort the array first
        seen = set()  # To track elements we've encountered
        pairs = set()  # To store unique pairs

        for num in arr:
            if -num in seen:
                # Add the pair in sorted order to ensure uniqueness
                pairs.add((min(num, -num), max(num, -num)))
            seen.add(num)

        # Convert the set of pairs to a sorted list of lists
        return sorted([list(pair) for pair in pairs])


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends