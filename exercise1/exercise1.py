from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, item in enumerate(nums):
            if target - item in hashtable:
                return[i, hashtable[target - item]]
            else:
                hashtable[item] = i
        return []
