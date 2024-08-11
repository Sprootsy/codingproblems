import unittest

from leetcode.remove_element import Solution


class TestRemoveElement(unittest.TestCase):

    def test_remove_element(self):
        testcases = [
            {
                "nums": [3, 2, 2, 3],
                "val": 3,
                "expected": [2, 2],
            },
            {
                "nums": [0, 1, 2, 2, 3, 0, 4, 2],
                "val": 2,
                "expected": [0, 1, 4, 0, 3],
            },
        ]
        s = Solution()
        for i, tc in enumerate(testcases):
            k = s.removeElement(tc["nums"], tc["val"])
            if tc["nums"][:k] != tc["expected"]:
                self.fail(f"TC: {i} Want: {tc['expected']} Got: {tc['nums'][:k]} K: {k}")
