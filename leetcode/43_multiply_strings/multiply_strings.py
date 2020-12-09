"""
https://leetcode.com/problems/multiply-strings/
43. Multiply Strings
Medium
--------------------
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1, num2):
        return self.multiply_2(num1, num2)

    def multiply_2(self, num1, num2):
        """
        参考思路:https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
        验证通过,性能一般:
        Runtime: 196 ms, faster than 15.10% of Python3 online submissions for Multiply Strings.
        Memory Usage: 14.4 MB, less than 10.51% of Python3 online submissions for Multiply Strings.
        :param num1:
        :param num2:
        :return:
        """
        if not num1 or not num2:
            return ""
        if num1 == "0" or num2 == "0":
            return "0"

        input1 = num1[::-1]
        input2 = num2[::-1]
        ret = ""
        ret_arr = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(input1)):
            for j in range(len(input2)):
                tmp = int(input1[i]) * int(input2[j])
                #个位
                tmp0 = tmp % 10 + ret_arr[i + j]
                ret_arr[i + j] = tmp0 % 10
                #十位
                tmp1 = tmp // 10 + ret_arr[i + j + 1] + tmp0 // 10
                ret_arr[i + j + 1] = tmp1 % 10
                #百位
                if tmp1 // 10 > 0:
                    ret_arr[i + j + 2] += tmp1 // 10
        for i in range(len(ret_arr) - 1, -1, -1):
            ret += str(ret_arr[i])
        return ret.lstrip("0")

    def multiply_1(self, num1, num2):
        """
        思路:模拟多位数相乘的办法,先依次计算出乘数和被乘数的乘积(补零),然后所有乘积相加.
        验证通过,性能一般
        Runtime: 280 ms, faster than 6.31% of Python3 online submissions for Multiply Strings.
        Memory Usage: 14.5 MB, less than 6.19% of Python3 online submissions for Multiply Strings.
        :param num1:
        :param num2:
        :return:
        """
        if not num1 or not num2:
            return ""
        # 特殊情况处理
        if num1 == "0" or num2 == "0":
            return "0"
        cache = [[] for i in range(len(num1))]
        outflow = 0
        input1 = num1[::-1]
        input2 = num2[::-1]
        for i in range(len(input1)):
            # 多位数乘法补零
            for k in range(i):
                cache[i].append(0)
            for j in range(len(input2)):
                tmp = int(input1[i]) * int(input2[j])
                tmp += outflow
                cache[i].append(tmp % 10)
                outflow = tmp // 10
            # 处理循环结束后outflow剩余的情况
            while outflow > 0:
                cache[i].append(outflow)
                outflow = outflow // 10
        # cache中依次相加,注意：此时cache中是低位在前，高位在后
        ret_1 = [0]
        ret_2 = []
        outflow = 0
        for i in range(len(cache)):
            index = 0
            while index < len(ret_1) and index < len(cache[i]):
                tmp = ret_1[index] + cache[i][index] + outflow
                ret_2.append(tmp % 10)
                outflow = tmp // 10
                index += 1
            for j in range(index, len(ret_1)):
                tmp = ret_1[j] + outflow
                ret_2.append(tmp % 10)
                outflow = tmp // 10
            for j in range(index, len(cache[i])):
                tmp = cache[i][j] + outflow
                ret_2.append(tmp % 10)
                outflow = tmp // 10
            # 处理循环结束后outflow剩余的情况
            while outflow > 0:
                ret_2.append(outflow % 10)
                outflow = outflow // 10
            ret_1 = ret_2.copy()
            ret_2 = []

        ret_1.reverse()
        return "".join(list(map(str, ret_1)))


def main():
    num1 = "2"
    num2 = "3"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "6")
    print("---------------------")

    num1 = "123"
    num2 = "456"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "56088")
    print("---------------------")

    num1 = "88989"
    num2 = "0"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "0")
    print("---------------------")

    num1 = "88989"
    num2 = "1000"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "88989000")
    print("---------------------")

    num1 = "99999"
    num2 = "99"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "99899001")
    print("---------------------")

    num1 = "99999"
    num2 = "999"
    ret = Solution().multiply(num1, num2)
    print(ret)
    print(ret == "99899001")
    print("---------------------")


if __name__ == "__main__":
    main()
