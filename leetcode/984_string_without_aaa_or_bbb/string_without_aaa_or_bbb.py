"""
https://leetcode.com/problems/string-without-aaa-or-bbb/
984. String Without AAA or BBB
Medium
----------------
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:
Input: A = 4, B = 1
Output: "aabaa"

Note:
0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""


class Solution:
    def strWithout3a3b(self, A, B):
        return self.strWithout3a3b_2(A, B)

    def strWithout3a3b_1(self, A, B):
        """
        1.数据校验,large=max(A,B),small=min(A,B),必须满足0<large<=2*small+2
        2.如果A>B>0,那么结果集追加aab,同时A=A-2,B=B-1;
        3.如果0<A<B,那么结果集追加abb,同时A=A-1,B=B-2;
        5.如果A=B>0,那么结果集追加ab,同时A=A-1,B=B-1;
        6.如果存在A=0且B>0或B=0且A>0,输出非零的对应的字母;
        7.循环步骤2/3/4/5/6,直到A=0 or B=0
        -------------
        验证通过,性能不错:
        Runtime: 24 ms, faster than 98.79% of Python3 online submissions for String Without AAA or BBB.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for String Without AAA or BBB.
        :param A:
        :param B:
        :return:
        """
        if A <= 0 or B <= 0:
            return ""
        if A > 2 * B + 2 or B > 2 * A + 2:
            return ""
        ret = ""
        while A > 0 or B > 0:
            if A <= 0 and B > 0:
                ret += "b" * B
                B = 0
            elif A > 0 and B <= 0:
                ret += "a" * A
                A = 0
            elif A > B:
                ret += "aab"
                A -= 2
                B -= 1
            elif A < B:
                ret += "bba"
                A -= 1
                B -= 2
            elif A == B:
                ret += "ab"
                A -= 1
                B -= 1
        return ret

    def strWithout3a3b_2(self, A, B):
        """
        strWithout3a3b_1()的另一种版本
        :param A:
        :param B:
        :return:
        """
        if A <= 0 or B <= 0:
            return ""
        if A > 2 * B + 2 or B > 2 * A + 2:
            return ""
        ret = ""
        if A > B:
            n1, n2 = A, B
            l1, l2 = "a", "b"
        else:
            n1, n2 = B, A
            l1, l2 = "b", "a"

        while n1 > 0 or n2 > 0:
            if n1 > n2 > 0:
                ret += l1 * 2 + l2
                n1 -= 2
                n2 -= 1
            elif n1 == n2:
                ret += l1 + l2
                n1 -= 1
                n2 -= 1
            elif n1 * n2 == 0:
                ret += l1 * n1
                n1 = 0
        return ret

    def strWithout3a3b_recursive(self, A, B):
        """
        leetcode上的其他解决方案:https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/226740/Clean-C%2B%2Bpython-solution
        :param A:
        :param B:
        :return:
        """
        if A == 0:
            return 'b' * B
        elif B == 0:
            return 'a' * A
        elif A == B:
            return 'ab' * A
        elif A > B:
            return 'aab' + self.strWithout3a3b_recursive(A - 2, B - 1)
        else:
            return self.strWithout3a3b_recursive(A - 1, B - 2) + 'abb'

    def strWithout3a3b_solution(self, A, B):
        """
        solution解决方案
        策略和执行分离
        https://leetcode.com/articles/string-without-aaa-or-bbb/
        :param A:
        :param B:
        :return:
        """
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)


def main():
    A = 1
    B = 2
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 4
    B = 1
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 4
    B = 3
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 20
    B = 9
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 9
    B = 20
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 1
    B = 3
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 1
    B = 4
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")

    A = 2
    B = 6
    ret = Solution().strWithout3a3b(A, B)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
