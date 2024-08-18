# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        s = {}
        for i, n in enumerate(numbers):
            s[n] = i

        for i, n in enumerate(numbers):
            if (target - n) in s:
                return [s[n], s[target - n]]
        
