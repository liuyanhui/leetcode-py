"""
76. Minimum Window Substring
Hard
------------------------------------
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.minWindow_1(s, t)

    def minWindow_1(self, s: str, t: str) -> str:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：
        1. naive solution
        穷举法。
        1.1. 设r[i]为以s[i]开头的，满足条件（包含t）的最小子串。
        1.2. 遍历s，即依次计算s[i]
        1.2.1. 顺序计算s[i:j]是否满足s[i:j]包含t的条件，其中：i<=j<len(s)
        1.2.2. 第一个满足条件的子串s[i:j]，就是s[i]开头的最优解，记为r[i]。
        1.3. 最小长度的r[i]就是所求。
        1.4 时间复杂度：O(N*M)
        2. slide window solution
        2.1. 思路：[i,j]，j右移表示与t匹配的过程中；当[i,j]包含t时，i开始右移，i右移的同时计算并更新全局最优解。存在当[i,j]包含t时，[i,j]中的某些字母数量大于t中的字母数的情况。
        2.1.1 遍历s，i=j=0
        IF s[j] not in t THEN
            j++
        IF s[j] in t THEN
            cnt[s[j]]++
            WHILE s[i:j]包含t THEN
                # 确保s[i]在t内
                WHILE s[i] not in t THEN
                    i++
                # 更新全局最优解
                IF j-i+1<len(ret) THEN
                    ret=s[i:j]
                cnt[s[i]]--
                i++ # i右移
            j++
        2.2. s[i:j]是否包含t的思路
        约束：对字母顺序没有限制，每个字母的出现次数匹配即可；只有小写字母。
        cnt和stat分别为s[i:j]的字母计数和t的字母计数
        FOR i IN [a..z]:
            IF cnt[i]!=stat[i] THEN 返回不包含
        2.3. 时间复杂度O(M+N)

        Runtime 406 ms Beats 13.48%
        Memory 17.23 MB Beats 81.93%
        """
        if not s or not t:
            return ""
        if len(s) < len(t):
            return ""

        def contains(expect: dict, cnt: dict) -> bool:
            if len(expect) != len(cnt):
                return False
            for s in expect:
                if expect[s] > cnt[s]:
                    return False
            return True

        ret = ''
        expect, cnt = {}, {}
        # 根据ascii码初始化
        for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            expect[c] = 0
            cnt[c] = 0
        for c in t:
            expect[c] += 1
        i = 0
        for j in range(len(s)):
            if s[j] in t:
                cnt[s[j]] += 1
                while contains(expect, cnt):
                    while i < len(s) and s[i] not in t:
                        i += 1
                    if not ret or len(ret) > j - i + 1:
                        ret = s[i:j + 1]
                    cnt[s[i]] -= 1
                    i += 1

        return ret


def do_func(s: str, t: str, expect: list):
    ret = Solution().minWindow(s, t)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func("ADOBECODEBANC", "ABC", "BANC")
    do_func(s="a", t="a", expect="a")
    do_func(s="a", t="aa", expect="")
    do_func(s="aaaaaaa", t="aa", expect="aa")


if __name__ == "__main__":
    main()
