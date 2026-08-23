class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        for num in nums:
            new_subset = []

            for subset in result:
                new_subset.append(subset + [num])

            result += new_subset

        return result
