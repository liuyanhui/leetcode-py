class Solution:
    """
    https://leetcode.com/problems/hamming-distance/submissions/
    461. Hamming Distance
    Easy
    """

    def hammingDistance(self, x: int, y: int) -> int:
        return self.hammingDistance_2(x, y)

    def hammingDistance_1(self, x, y):
        ret = 0
        xor = x ^ y
        while xor > 0:
            ret += xor & 1
            xor = xor >> 1
        return ret

    def hammingDistance_2(self, x, y):
        return bin(x ^ y).count('1')


def main():
    ret = Solution().hammingDistance(1, 4)
    print(ret)
    print("----------")


if __name__ == "__main__":
    main()
