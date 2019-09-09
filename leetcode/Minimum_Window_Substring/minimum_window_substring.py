class Solution:
    """
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
     https://leetcode.com/problems/minimum-window-substring
     76. Minimum Window Substring
    """

    def minWindow(self, s, t):
        ret = ""
        if not s.strip() or not t.strip():
            return ret

        # right前进1
        # left前进1

        dict_char_counter = {}
        for c in t:
            dict_char_counter[c] = dict_char_counter.get(c, 0) + 1
        # print("dict_char_counter=", str(dict_char_counter))
        count = len(dict_char_counter)

        left = 0
        right = 0
        while right < len(s):
            tmp_r = s[right]
            if tmp_r in dict_char_counter:
                dict_char_counter[tmp_r] -= 1
                if dict_char_counter[tmp_r] == 0:
                    count -= 1
            right += 1

            while count == 0:
                tmp_l = s[left]
                if tmp_l in dict_char_counter:
                    if dict_char_counter[tmp_l] == 0:
                        count += 1
                    dict_char_counter[tmp_l] += 1

                if len(ret) == 0 or len(ret) > right - left:
                    ret = s[left:right]
                left += 1

        return ret


def main():
    s = ""
    t = ""
    ret = Solution().minWindow(s, t)
    print(ret)

    s = "ADOBECODEBANC"
    t = "ABC"
    ret = Solution().minWindow(s, t)
    print(ret)


if __name__ == "__main__":
    main()
