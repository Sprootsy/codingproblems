import unittest

from leetcode.merge_sorted import Solution


class TestMergeSorted(unittest.TestCase):

    def test_merge_sorted(self):
        testcases = [
            {
                "nums1": [1, 2, 3, 0, 0, 0],
                "m": 3,
                "nums2": [2, 5, 6],
                "n": 3,
                "expected": [1, 2, 2, 3, 5, 6],
            },
            {
                "nums1": [0],
                "m": 0,
                "nums2": [1],
                "n": 1,
                "expected": [1],
            },
        ]
        s = Solution()
        for i, tc in enumerate(testcases):
            s.merge(tc["nums1"], tc["m"], tc["nums2"], tc["n"])
            if tc["nums1"] != tc["expected"]:
                self.fail(f"TC: {i} Want: {tc['expected']} Got: {tc['nums1']}")
