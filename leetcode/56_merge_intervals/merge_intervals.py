"""
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Medium
---------------------
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


# 与 495. Teemo Attacking类似
class Solution:
    def merge(self, intervals):
        return self.merge_2(intervals)

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


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    ret = Solution().merge(intervals)
    print(ret)
    print("--------------------")

    intervals = [[1, 4], [4, 5]]
    ret = Solution().merge(intervals)
    print(ret)
    print("--------------------")

    intervals = [[1, 4], [2, 3]]
    ret = Solution().merge(intervals)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
