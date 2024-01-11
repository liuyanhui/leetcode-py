"""
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Medium
---------------------
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""


# 与 495. Teemo Attacking类似
class Solution:
    def merge(self, intervals):
        return self.merge_3(intervals)

    def merge_3(self, intervals: list) -> list:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. 两个区间[i1,j1][i2,j2]可以merge有几种情况：
        1.1. 假设 i1<=i2
        1.2. '交叉'。[i1,i2,j1,j2] ==> [min(i1,i2),max(j1,j2)]
        1.3. '包含'。[i1,i2,j2,j1] ==> [min(i1,i2),max(j1,j2)]
        1.4. '恰好相连'。[i1,j1==i2,j2] ==> [min(i1,i2),max(j1,j2)]
        2. 先排序再依次合并。根据第一个数字排序。
        2.1. 比较的规则是从右向左，由远及近。


        验证通过:
        Runtime 130 ms Beats 73.98%
        Memory 21.36 MB Beats 44.44%
        """
        intervals.sort()
        ret = [intervals[0]]
        for item in intervals:
            # 从右向左，由远及近的方式
            if ret[-1][1] + 1 <= item[0]:  # 不合并
                ret.append(item)
            else:
                ret[-1][1] = max(ret[-1][1], item[1])
        return ret

    def merge_1(self, intervals):
        """
        1.排序,根据第0个元素进行排序
        2.如果intervals[i][1]<intervals[i+1][0],没有发生重叠
        3.如果intervals[i][1]>=intervals[i+1][0],发生重叠,合并intervals[i]和intervals[i+1]
        时间复杂度是排序的复杂度
        -------------------
        验证通过,性能还可以,如果修改排序方法为intervals.sort()会降低内存使用量:
        Runtime: 84 ms, faster than 98.95% of Python3 online submissions for Merge Intervals.
        Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
        :param intervals:
        :return:
        """
        if not intervals:
            return []
        ret = []
        sorted_intervals = sorted(intervals)
        tmp_merged = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            if tmp_merged[1] >= sorted_intervals[i][0]:
                tmp_merged[1] = max(sorted_intervals[i][1], tmp_merged[1])
            else:
                ret.append(tmp_merged.copy())
                tmp_merged = sorted_intervals[i]
        ret.append(tmp_merged.copy())
        return ret

    def merge_2(self, intervals):
        """
        merge_1()的代码优化版本
        -------------------
        验证通过,性能还可以,但是内存使用量并没有下降:
        Runtime: 84 ms, faster than 98.95% of Python3 online submissions for Merge Intervals.
        Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
        :param intervals:
        :return:
        """
        if not intervals:
            return []
        intervals.sort()
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            if ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(intervals[i][1], ret[-1][1])
            else:
                ret.append(intervals[i])
        return ret


def do_func(intervals: list, expect: list):
    ret = Solution().merge(intervals)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
    do_func([[1, 4], [4, 5]], [[1, 5]])
    do_func([[1, 4], [2, 3]], [[1, 4]])
    do_func([[1, 4], [5, 6]], [[1, 4], [5, 6]])


if __name__ == "__main__":
    main()
