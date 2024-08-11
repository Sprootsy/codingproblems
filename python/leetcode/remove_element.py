# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1  # last index that is != val
        while end >= 0 and nums[end] == val:
            end -= 1

        i = 0
        while i <= end and end >= 0:
            if nums[i] == val:
                nums[i] = nums[end]
                nums[end] = val
                end -= 1
            else:
                i += 1

        return i
