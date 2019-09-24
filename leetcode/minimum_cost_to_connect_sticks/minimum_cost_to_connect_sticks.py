"""
题目来源
https://leetcode.com/discuss/interview-question/344677
真实的题目来源
https://leetcode.com/problems/minimum-cost-to-connect-sticks
"""


class Solution:
    def find_minimum_cose(self, ropes):
        return self.find_minimum_cose_2(ropes)

    def find_minimum_cose_1(self, ropes):
        """
        1.最小的两个数字相加
        2.循环执行步骤1,知道只有一个数字
        3.每次计算结束,需要重新排序
        时间复杂度:N*N*logN
        空间复杂度:O(1)
        :param ropes:
        :return:
        """
        if ropes is None or len(ropes) == 0:
            return 0
        ret = 0
        while len(ropes) > 1:
            ropes.sort()
            tmp = ropes.pop(0) + ropes.pop(0)
            ret += tmp
            ropes.append(tmp)
        return ret

    def find_minimum_cose_2(self, ropes):
        """
        find_minimum_cose_1优化
        根据Best Conceivable Runtime（BCR)方法,时间复杂度可以优化为N*logN
        使用BUD思路,优化sort(),单次二分查找+插入的时间复杂度是logN

        :param ropes:
        :return:
        """
        if ropes is None or len(ropes) == 0:
            return 0
        ret = 0

        def insert_sort(d):
            mid = 0
            l, r = 0, len(ropes) - 1
            while 0 <= l < r < len(ropes):
                mid = (l + r) // 2
                if ropes[mid] > d:
                    # 跳过重复相等的值
                    while mid > 0 and ropes[mid] == ropes[mid - 1]:
                        mid -= 1
                    mid = r = (mid - 1) if mid > 0 else 0
                elif ropes[mid] < d:
                    # 跳过重复相等的值
                    while mid < len(ropes) - 1 and ropes[mid] == ropes[mid + 1]:
                        mid += 1
                    mid = l = mid + 1 if mid < len(ropes) else len(ropes)
                else:
                    break
            ropes.insert(mid, d)

        ropes.sort()
        while len(ropes) > 1:
            tmp = ropes.pop(0) + ropes.pop(0)
            ret += tmp
            insert_sort(tmp)
        return ret


def main():
    r = [8]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")

    r = [8, 4]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")

    r = [8, 4, 6, 12]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")

    r = [20, 4, 8, 2]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")

    r = [1, 2, 5, 10, 35, 89]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")

    r = [2, 2, 3, 3]
    ret = Solution().find_minimum_cose(r)
    print(ret)
    print("-----------")


if __name__ == "__main__":
    main()
