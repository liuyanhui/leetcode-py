"""
58. Length of Last Word
Easy
---------------------------
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return self.lengthOfLastWord_1(s)

    def lengthOfLastWord_1(self, s: str) -> int:
        """
        Round 3
        Score[5] Lower is harder

        Args:
            s:

        Returns:

        """
        # print(s.split()[-1])
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                break
            i -= 1
        j = i
        while j >= 0:
            if s[j] == ' ':
                break
            j -= 1
        return i - j


def do_func(s: str, expect: int):
    ret = Solution().lengthOfLastWord(s)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func('Hello World', 5)
    do_func('   fly me   to   the moon  ', 4)
    do_func('luffy is still joyboy', 6)
    do_func('joyboy', 6)
    do_func(' ', 0)


if __name__ == "__main__":
    main()
