class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = {}
        for index , val in enumerate(nums):
            diff = target - val
            if diff in hash_map :
                return [index , hash_map[diff]]
            hash_map[val] = index
        