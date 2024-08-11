# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
import math
from typing import List


class Solution:

    def binary_insert(self, nums: List[int], x: int, l: int) -> List[int]:
        low, high = 0, l
        while low < high:
            mid = int(math.floor((low + high) / 2))
            if nums[mid] <= x:
                low = mid + 1
            else:
                high = mid
        
        ins = x
        for i in range(low, l + 1):
            tmp = nums[i]
            nums[i] = ins
            ins = tmp

        return nums


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m
        for x in nums2:
            self.binary_insert(nums1, x, l)
            l += 1




        
