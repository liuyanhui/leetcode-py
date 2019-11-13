"""
https://leetcode.com/problems/can-place-flowers/
605. Can Place Flowers
Easy
--------------------
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        return self.canPlaceFlowers_1(flowerbed, n)

    def canPlaceFlowers_1(self, flowerbed, n):
        """
        思路:
        1.只有连续出现的0才能种植 flower
        2.连续出现的0的个数和可以种植flower的数量的关系为:(i+1)/2
        3.需要考虑起止边界
        ------
        验证通过,性能很好:
        Runtime: 164 ms, faster than 99.85% of Python3 online submissions for Can Place Flowers.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.
        :param flowerbed:
        :param n:
        :return:
        """
        if not flowerbed or n < 1:
            return True
        empty_count = 1  # 这里是关键之一,用于处理最左侧连续是0的情况
        for f in flowerbed:
            if f == 0:
                empty_count += 1
            else:
                n -= (empty_count - 1) // 2
                empty_count = 0
        if empty_count > 0:  # 这里处理最右侧连续是0的情况
            n -= empty_count // 2
        return n <= 0


def main():
    flowerbed = [0, 0, 0]
    n = 1
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")

    flowerbed = [0, 0, 1, 0, 0]
    n = 1
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")

    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")

    flowerbed = [0, 0, 1, 0, 0, 0, 1]
    n = 2
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")

    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
