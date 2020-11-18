"""
https://leetcode.com/problems/zigzag-conversion/
6. ZigZag Conversion
Medium
----------------------------
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

"""


class Solution:
    def convert(self, s, numRows):
        """
        验证通过:性能不错
        Runtime: 48 ms, faster than 93.79% of Python3 online submissions for ZigZag Conversion.
        Memory Usage: 14.3 MB, less than 24.53% of Python3 online submissions for ZigZag Conversion.
        :param s:
        :param numRows:
        :return:
        """
        if not s or not numRows:
            return ""
        ret_list=["" for i in range(numRows)]
        direction = 0 #0:down;1:up
        row = 0
        for c in s:
            ret_list[row]+=c
            if direction == 0:
                row+=1
            else:
                row-=1
            if row == -1:
                direction = 0
                row = 1
                if row > numRows-1:#防止越界
                    row = 0
            elif row==numRows:
                direction = 1
                row = numRows-2
                if row < 0:#防止越界
                    row = 0
        ret = ""
        for rowstr in ret_list:
            ret += rowstr
        return ret


def main():
    s = "PAYPALISHIRING"
    numRows = 3
    ret = Solution().convert(s, numRows)
    print(ret)
    print(ret == "PAHNAPLSIIGYIR")
    print('--------------------')

    s = "PAYPALISHIRING"
    numRows = 4
    ret = Solution().convert(s, numRows)
    print(ret)
    print(ret == "PINALSIGYAHRPI")
    print('--------------------')

    s = "A"
    numRows = 1
    ret = Solution().convert(s, numRows)
    print(ret)
    print(ret == "A")
    print('--------------------')


    s = "ABC"
    numRows = 1
    ret = Solution().convert(s, numRows)
    print(ret)
    print(ret == "ABC")
    print('--------------------')


if __name__ == "__main__":
    main();
