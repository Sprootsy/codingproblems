# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    """ Sliding window technique with variable window size.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Returns the length of the longest substring of non repeating chars.
        """
        l, ans, cur = 0, 0, ""
        chars = {}
        for r, c in enumerate(len(s)):
            cur += c
            if c not in chars or chars[c] < 1:
                chars[c] = 1
                ans = max(ans, r - l + 1)
            else:
                chars[c] += 1
                while chars[c] > 1 and l <= r:
                    chars[s[l]] -= 1
                    l += 1

        return ans

