class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in nums:
            complement = target - n
            if complement in nums:
                if complement == n:
                    if nums.count(n) > 1:
                        return [nums.index(n), nums.index(n, nums.index(n) + 1)]
                else:
                    return [nums.index(n), nums.index(complement)]
