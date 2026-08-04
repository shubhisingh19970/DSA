class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        min_num = min(nums)
        max_num = max(nums)
        
        missing = []
        for i in range(min_num, max_num + 1):
            if i not in num_set:
                missing.append(i)
        
        return missing