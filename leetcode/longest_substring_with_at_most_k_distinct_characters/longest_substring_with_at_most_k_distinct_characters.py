import sys


# https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/description
# hard
# 未验证leetcode
class Solution:
    def find(self, s, k):
        """主要思想是slide window
            1.left前进1的条件
            2.right前进1的条件
        """
        if not s or k <= 0:
            return 0
        ret = 1

        left = 0
        right = 0
        exist_char_dict = {}  # 记录字符出现的次数
        while right < len(s):
            if exist_char_dict.get(s[right], -1) > 0:
                # 已经重复的字符,right前进1,记录字符出现的次数加1
                exist_char_dict[s[right]] += 1
                right += 1
            else:
                # 不重复的字符
                if len(exist_char_dict) < k:
                    # 额度未满,right前进1,记录字符出现的次数等于1
                    exist_char_dict[s[right]] = 1
                    right += 1
                else:
                    # 额度已满
                    # 记录字符出现的次数减一
                    exist_char_dict[s[left]] -= 1
                    # 字符清零时从exist_char_dict中清除
                    if exist_char_dict[s[left]] <= 0:
                        exist_char_dict.pop(s[left])
                    # left前进1
                    left += 1

            ret = max(ret, right - left)

        return ret


def main():
    s = 'eceba'
    k = 3
    ret = Solution().find(s, k)
    print("ret=", ret)
    s = 'WORLD'
    k = 4
    ret = Solution().find(s, k)
    print("ret=", ret)
    s = 'eccebeeeeeedeeeeeea'
    k = 2
    ret = Solution().find(s, k)
    print("ret=", ret)
    s = 'aaaaaaaaaa'
    k = 1
    ret = Solution().find(s, k)
    print("ret=", ret)


if __name__ == '__main__':
    main()
