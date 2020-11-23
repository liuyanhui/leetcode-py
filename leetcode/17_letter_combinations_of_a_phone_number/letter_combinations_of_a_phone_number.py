"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
17. Letter Combinations of a Phone Number
Medium
----------------------
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        验证通过:
        Runtime: 24 ms, faster than 94.05% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 14.3 MB, less than 9.19% of Python3 online submissions for Letter Combinations of a Phone Number.
        :param digits:
        :return:
        """
        if not digits or len(digits) > 4:
            return []

        def do_combinate(head, beg, chars_list, rs):
            if beg >= len(chars_list):
                if len(head) == beg:
                    rs.append(head)
                return
            for i in range(beg, len(chars_list)):
                for c in chars_list[i]:
                    do_combinate(head + c, i + 1, chars_list, rs)

            # if len(head) == len(chars_list):
            #     rs.append(head)

        c_list = []
        for d in digits:
            if d == "2":
                c_list.append("abc")
            elif d == '3':
                c_list.append("def")
            elif d == '4':
                c_list.append("ghi")
            elif d == '5':
                c_list.append("jkl")
            elif d == '6':
                c_list.append("mno")
            elif d == '7':
                c_list.append("pqrs")
            elif d == '8':
                c_list.append("tuv")
            elif d == '9':
                c_list.append("wxyz")
            else:
                pass

        exist_str = ""
        ret = []
        do_combinate(exist_str, 0, c_list, ret)
        return ret


def main():
    digits = "23"
    ret = Solution().letterCombinations(digits)
    print(ret)
    print(ret == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    print("---------------------")

    digits = ""
    ret = Solution().letterCombinations(digits)
    print(ret)
    print(ret == [])
    print("---------------------")

    digits = "2"
    ret = Solution().letterCombinations(digits)
    print(ret)
    print(ret == ["a", "b", "c"])
    print("---------------------")

    digits = "234"
    ret = Solution().letterCombinations(digits)
    print(ret)
    print(ret == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])
    print("---------------------")

if __name__ == "__main__":
    main()
