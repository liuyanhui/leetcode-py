"""
https://leetcode.com/problems/course-schedule-ii/
210. Course Schedule II
Medium
----------------------------
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution:
    def findOrder(self, numCourses, prerequisites):
        return self.findOrder_2(numCourses, prerequisites)

    def findOrder_1(self, numCourses, prerequisites):
        """
        这是个有向无环图的bfs问题.
        该方法有很多问题,没有通过验证
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses <= 0:
            return []
        existed = set()
        ret = []
        if numCourses == 1:
            return [0]

        def findNextCourse(course):
            tmpCourses = []
            for pair in prerequisites:
                if pair[1] == course:
                    tmpCourses.append(pair[0])
            return tmpCourses

        for pair in prerequisites:
            existed.clear()
            ret.clear()

            existed.add(pair[1])
            existed.add(pair[0])
            ret.append(pair[1])
            ret.append(pair[0])
            i = 0
            while i < len(ret):
                nextCourses = findNextCourse(ret[i])
                i += 1
                for nc in nextCourses:
                    if nc not in existed:
                        existed.add(nc)
                        ret.append(nc)

            if len(ret) == numCourses:
                return ret
        return []

    def findOrder_2(self, numCourses, prerequisites):
        """
        参考思路:https://leetcode.com/articles/course-schedule-ii/
        采用DFS的思路
        1.使用stack保存遍历结果,最终stack to list即可
        2.DFS+后序遍历
        3.某个节点没有后继节点时入stack
        4.遍历得到该节点的所有前置节点
        5.需要考虑有向图中存在环的情况
        执行结果:
        通过,详情如下
        Runtime: 740 ms, faster than 5.24% of Python3 online submissions for Course Schedule II.
        Memory Usage: 16.7 MB, less than 17.86% of Python3 online submissions for Course Schedule II.
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        finishedCourse = set()  # 已经在ret中的course num
        recusivingCourse = set()  # 处理循环依赖的情况

        def dfs(num):
            """
            :param num:
            :return: False->存在循环依赖
            """
            # 判断是否循环依赖
            if num in recusivingCourse:
                ret.clear()
                return False
            recusivingCourse.add(num)
            # 如果已经出现过,直接返回
            if num not in finishedCourse:
                courseList = findSuccessorCourse(num)
                if len(courseList) == 0:  # 如果course num不在prerequisites中,表示跟其他课程没有依赖,直接入stack
                    if num not in finishedCourse:
                        ret.append(num)
                        finishedCourse.add(num)
                else:
                    for c in courseList:
                        if not dfs(c):
                            return False
                    if num not in finishedCourse:
                        ret.append(num)
                        finishedCourse.add(num)
            recusivingCourse.remove(num)
            return True

        def findSuccessorCourse(num):
            """
            查找num的后继课程
            :param num:
            :return:
            """
            c = []
            for pair in prerequisites:
                if num == pair[1]:
                    c.append(pair[0])
            return c

        for num in range(numCourses):
            if not dfs(num):
                return []

        # 反转list 为 stack
        ret.reverse()
        return ret


def main():
    n = 2
    p = [[1, 0]]
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")

    n = 4
    p = [[1, 0], [2, 0], [3, 1], [3, 2]]
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")

    n = 1
    p = []
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")

    n = 2
    p = []
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")

    n = 2
    p = [[0, 1], [1, 0]]
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
