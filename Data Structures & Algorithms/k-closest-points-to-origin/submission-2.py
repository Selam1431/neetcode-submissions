class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []

        for x, y in points:
            distances = x**2 + y**2
            temp.append([distances, x, y])

        temp.sort()

        ans = []

        for i in range(k):
            distances, x, y = temp[i]
            ans.append([x,y])

        return ans