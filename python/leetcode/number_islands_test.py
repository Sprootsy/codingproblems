import unittest

from leetcode.number_islands import Solution


class TestNumberIslands(unittest.TestCase):

    def test_number_islands(self):
        testcases = [
            {
                "grid": [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ],
                "expected": 1,
            },
            {
                "grid": [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ],
                "expected": 3,
            },
        ]
        s = Solution()
        for i, tc in enumerate(testcases):
            k = s.numIslands(tc["grid"])
            if k != tc["expected"]:
                self.fail(f"TC: {i} Want: {tc['expected']} Got: {k} ")
