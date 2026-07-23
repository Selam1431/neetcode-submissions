class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        now= 0
        maximum = 0
        for num in nums:
            if num ==1:
                now += 1
                maximum =max(maximum,now)
            else:
                now = 0
        return maximum
