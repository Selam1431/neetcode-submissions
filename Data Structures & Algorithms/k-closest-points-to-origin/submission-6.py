class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []

        for x, y in points:
            distance = x*x + y*y
            temp.append([distance, x, y])

        temp.sort()

        ans = []

        for i in range(k):
            distance, x , y = temp[i]
            ans.append([x, y])

        return ans
