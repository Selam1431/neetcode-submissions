class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if right_sum == left_sum:
                return i

            else:
                left_sum += num

        return -1

        
            


        
        