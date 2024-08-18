from typing import List


class Solution:

    def binarySearch(self, numbers: List[int], search: int, start: int) -> int:
        l = len(numbers)
        low, high = start, l - 1
        while low <= high:
            mid = (low + high) >> 1
            cur = numbers[mid] 
            if cur < search:
                low = mid + 1
            elif cur == search:
                return mid
            else:
                high = mid - 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            need = (target - n)
            found = self.binarySearch(numbers, need, i + 1)
            if found > -1:
                return [i + 1, found + 1]
        return []