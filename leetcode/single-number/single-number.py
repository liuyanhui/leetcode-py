class Solution:
    """
    https://leetcode.com/problems/single-number/
    136. Single Number
    easy
    """

    def singleNumber(self, nums):
        return self.singleNumber_1(nums)

    def singleNumber_1(self, nums):
        """
        用hashtable记录出现次数，出现2次后从hashtable中删除，最后剩下的就是所求
        """
        h = {}
        for n in nums:
            if n in h:
                h.pop(n)
            else:
                h[n] = 1
        return list(h.keys())[0]

    def singleNumber_2(self, nums):
        """
        用数学的方法，公式为：2∗(a+b+c)−(a+a+b+b+c)=c
        """
        h = {}
        sum_list = 0
        sum_hash = 0
        for n in nums:
            sum_list += n
            if n not in h:
                h[n] = 1
        for n in h:
            sum_hash += n
        return 2 * sum_hash - sum_list

    def singleNumber_3(self, nums):
        """
        方法singleNumber_2的python简化版
        参考Approach 3: Math
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_4(self, nums):
        """
        Approach 4: Bit Manipulation
        思路如下:
        a XOR 0 = a; a XOR a = 0
        a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        """
        a = 0
        for i in nums:
            a ^= i
        return a

def main():
    a = [2, 3, 2]
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")

    a = [0, 1, 0, 1, 99]
    # print("a=", a)
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")


if __name__ == "__main__":
    main()
