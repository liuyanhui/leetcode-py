"""
https://leetcode.com/problems/generate-parentheses/
22. Generate Parentheses
Medium
--------------------
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
import collections


class Solution:
    def generateParenthesis(self, n):
        return self.generateParenthesis_2(n)

    def generateParenthesis_1(self, n):
        """
        思路:递归法,
        考虑以下情况:1+(n-1),2+(n-2),3+(n-3),...,n-1+(1)
        特殊情况:(n-1)
        验证通过,
        Runtime: 28 ms, faster than 93.76% of Python3 online submissions for Generate Parentheses.
        Memory Usage: 14.9 MB, less than 9.24% of Python3 online submissions for Generate Parentheses.
        :param n:
        :return:
        """
        if not n or n > 8 or n < 1:
            return []
        cache = collections.defaultdict(set)

        def do_recursive(num):
            nonlocal cache
            if num == 0:
                return ""
            if num == 1:
                cache[num].add("()")
                return cache[num]
            child_ret = set()
            # 缓存存在直接返回
            if cache[num]:
                return cache[num]
            # 处理(n-1)这种特殊情况
            for i in range(1, num + 1):
                tmp = do_recursive(num - 1)
                for t in tmp:
                    child_ret.add("(" + t + ")")
            # 遍历,递归
            for i in range(1, num):
                rs1 = do_recursive(i)
                rs2 = do_recursive(num - i)
                # 合并rs1和rs2,笛卡尔积
                for t1 in rs1:
                    for t2 in rs2:
                        child_ret.add(t1 + t2)
            cache[num] = child_ret
            return child_ret

        do_recursive(n)
        return list(cache[n])
        # return sorted(list(cache[n]))


    def generateParenthesis_2(self, N):
        """
        参考思路:
        https://leetcode.com/problems/generate-parentheses/solution/
        中的Solution2
        通过控制(和)数量进行递归,当字符串长度==2N时返回.
        :param n:
        :return:
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


    def generateParenthesis_error(self, n):
        if not n or n > 8 or n < 1:
            return []
        ret = set()

        def do_recursive(head, tail, left, rs):
            if left == 1:
                rs.add(head + "()" + tail)
                return
            do_recursive(head, "()" + tail, left - 1, rs)
            do_recursive(head + "(", ")" + tail, left - 1, rs)
            do_recursive(head + "()", tail, left - 1, rs)

        do_recursive("", "", n, ret)
        return sorted(list(ret))


def main():
    n = 3
    ret = Solution().generateParenthesis(n)
    print(ret)
    print(ret == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]))
    print("---------------------")

    n = 1
    ret = Solution().generateParenthesis(n)
    print(ret)
    print(ret == ["()"])
    print("---------------------")

    n = 4
    ret = Solution().generateParenthesis(n)
    print(ret)
    print(ret == sorted(
            ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
             "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]))
    print("---------------------")


if __name__ == "__main__":
    main()
