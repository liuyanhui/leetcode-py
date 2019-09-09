"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/
974. Subarray Sums Divisible by K
medium
"""


class Solution:
    def subarraysDivByK(self, A, K):
        # return self.brute_method(A, K)
        return self.prefix_method(A, K)

    def brute_method(self, A, K):
        """
        暴力法，时间复杂度N*N
        """
        if A is None or K == 0:
            return 0
        ret = 0
        for i in range(len(A)):
            tmp_sum = 0
            for j in range(i, len(A)):
                tmp_sum += A[j]
                if tmp_sum % K == 0:
                    ret += 1
        return ret

    def prefix_method(self, A, K):
        """
        prefix方法
        https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217980/Java-O(N)-with-HashMap-and-prefix-Sum
        """
        if A is None or K == 0:
            return 0
        # 计算P
        ret = 0
        mod_count = {}
        p = [A[0]]
        for i in range(1, len(A)):
            p.append(p[i - 1] + A[i])
        print("p=%s" % str(p))
        # 计算P中mod K相同的元素
        for p_val in p:
            tmp_mod = p_val % K
            if tmp_mod in mod_count:
                mod_count[tmp_mod] += 1
                ret += mod_count[tmp_mod]
            else:
                if tmp_mod == 0:
                    mod_count[tmp_mod] = 1
                    ret += 1
                else:
                    mod_count[tmp_mod] = 0
                    # print("ret=%d"%ret)
        return ret


def main():
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    ret = Solution().subarraysDivByK(A, K)
    print(ret)

    A = [4, 5, 0, -2, -3, 1]
    K = 0
    ret = Solution().subarraysDivByK(A, K)
    print(ret)

    A = [4, 5, 0, -2, -3, 1]
    K = -1
    ret = Solution().subarraysDivByK(A, K)
    print(ret)

    A = [0]
    K = -1
    ret = Solution().subarraysDivByK(A, K)
    print(ret)


if __name__ == "__main__":
    main()
