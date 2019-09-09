class Solution:
    """
    https://leetcode.com/problems/permutation-sequence/
    60. Permutation Sequence
    Medium

    The set [1,2,3,...,n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.
    Note:
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
    Example 1:
    Input: n = 3, k = 3
    Output: "213"
    Example 2:
    Input: n = 4, k = 9
    Output: "2314"
    """

    def getPermutation(self, n, k):
        """
        1.首先不能使用brute方式暴力求解,因为必然会超时
        :param n:
        :param k:
        :return:
        """
        if n < 0 or 0 > k > self.calc_factorial(n):
            return 0
        # nums = [i + 1 for i in range(n)]
        # ret = []
        # self.getPermutation_recursive(nums, k, ret)
        # return "".join(ret)
        return self.getPermutation_loop(n, k)

    def getPermutation_recursive(self, nums, k, ret):
        """
        采用递归的思路,分治法.也可以通过循环实现
        通过计算i=(k-1)/n=(n-1)!可以确定第一个数字,之后n=n-1,重新计算k,清除已经计算过的nums[i],然后通过递归可以求解.如:
        n=3,k=3
        第一轮:n=3,k=3 -> (k-1)/(n-1)! -> (3-1)/(3-1)!=1 -> ret=num[1]  -> ret="2"  -> k=k-(i+1)*(n-1)! -> n=n-1
        第二轮:n=2,k=1 -> (k-1)/(n-1)! -> (1-1)/(2-1)!=0 -> ret+=num[0] -> ret="21" -> k=k-(i+1)*(n-1)! -> n=n-1
        第三轮:n=1     -> ret+=num[0]  -> ret="213"
        :param nums:
        :param k:
        :param ret:
        :return:
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            ret.append(str(nums[0]))
            return
        n = len(nums)
        factorial = self.calc_factorial(n - 1)
        i = (k - 1) // factorial
        ret.append(str(nums[i]))
        nums.remove(nums[i])
        self.getPermutation_recursive(nums, k - (i + 1) * factorial, ret)

    def getPermutation_loop(self, n, k):
        """
        方法getPermutation_recursive的非递归实现,采用循环的方式
        """
        ret=""
        ret_list = []
        tmp_n, tmp_k = n, k
        nums = [i + 1 for i in range(n)]
        while len(nums) > 0:
            factorial = self.calc_factorial(tmp_n - 1)
            i = (tmp_k - 1) // factorial
            ret_list.append(nums[i])
            tmp_n -= 1
            tmp_k -= (i + 1) * factorial
            nums.remove(nums[i])
        for r in ret_list:
            ret+=str(r)
        return ret

    def calc_factorial(self, n):
        """
        计算阶乘
        :param n:
        :return:
        """
        if n < 0:
            return 0
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret


def main():
    n = 3
    k = 3
    ret = Solution().getPermutation(n, k)
    print(ret)
    print("--------------")

    n = 4
    k = 9
    ret = Solution().getPermutation(n, k)
    print(ret)
    print("--------------")

    # print(Solution().calc_factorial(0))


if __name__ == "__main__":
    main()
