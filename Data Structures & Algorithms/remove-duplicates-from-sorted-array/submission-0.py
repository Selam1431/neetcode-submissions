class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k= len(nums)
        if k <= 1:
            return k
        slow = 0
        for fast in range(1,k):
            if nums[fast] != nums[slow]:
                slow +=1
                nums[slow] = nums[fast]

        return slow + 1

        