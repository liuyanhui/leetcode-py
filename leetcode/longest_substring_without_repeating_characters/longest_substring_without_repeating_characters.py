class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        ret = 1
        start = 0
        end = 1
        while end < len(s):
            index = s.find(s[end], start, end);
            if index >= 0:
                start = index + 1
            # else:
            ret = max(ret, end - start + 1)
            end += 1

        return ret


def main():
    s = "abcabcbb"
    s = 'bbbbbbbbbbb'
    s = 'pwwkew'
    s = 'au'
    ret = Solution().lengthOfLongestSubstring(s)
    print(ret)


if __name__ == "__main__":
    main()
