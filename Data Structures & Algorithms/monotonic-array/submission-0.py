class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 0
        j = i + 1
        
        increasing = True
        decreasing = True

        while j < len(nums):
            if nums[i] > nums[j]:
                increasing = False

            if nums[i] < nums[j]:
                decreasing = False

            if not increasing and not decreasing:
                return False

            i += 1
            j += 1

        return True
            