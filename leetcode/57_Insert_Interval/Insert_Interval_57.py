"""
57. Insert Interval
Medium
---------------------------------
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        return self.insert_1(intervals, newInterval)

    def insert_1(self, intervals: list, newInterval: list) -> list:
        """
        Round 3
        Score[1] Lower is harder

        以下方案更优:
        https://leetcode.com/problems/insert-interval/solutions/21602/short-and-straight-forward-java-solution/

        验证通过:
        Runtime 81 ms Beats 59.39%
        Memory 20.74 MB Beats 19.44%

        Args:
            intervals:
            newInterval:

        Returns:

        """
        ret = []
        intervals.sort()
        # 特殊情况处理
        if len(intervals) == 0:
            return [newInterval]

        i = 0
        # 1.先计算不想交的左边的部分
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                i += 1
            else:
                break
        ret += intervals[0:i]
        # 2.处理可能相交的部分
        j = i
        # 2.1 先查找定位右侧区间
        while j < len(intervals):
            if intervals[j][0] <= newInterval[1]:
                j += 1
            else:
                break
        # 2.2. 判断,合并
        # review 下面的代码,把ret.append()逻辑放在while循环中会简化实现
        if i == len(intervals):
            ret.append([newInterval[0], max(intervals[j - 1][1], newInterval[1])])
        elif j == 0:
            ret.append([min(intervals[i][0], newInterval[0]), newInterval[1]])
        else:
            ret.append([min(intervals[i][0], newInterval[0]), max(intervals[j - 1][1], newInterval[1])])

        # 3.处理右侧不相交的部分
        ret += intervals[j:]

        return ret


def do_func(intervals: list, newInterval: list, expect: list):
    ret = Solution().insert(intervals, newInterval)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
    do_func([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
    do_func([], [2, 5], [[2, 5]])
    do_func([[10, 30], [60, 90]], [2, 5], [[2, 5], [10, 30], [60, 90]])
    do_func([[1, 3], [6, 9]], [12, 15], [[1, 3], [6, 9], [12, 15]])


if __name__ == "__main__":
    main()
