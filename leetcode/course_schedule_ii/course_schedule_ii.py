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

import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        return self.findOrder_7(numCourses, prerequisites)

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
        6.如果numCourses>0, prerequisites为空是表示所有可能没有前置课程,直接返回0~n的数组即可
        执行结果:
        通过,详情如下
        Runtime: 740 ms, faster than 5.24% of Python3 online submissions for Course Schedule II.
        Memory Usage: 16.7 MB, less than 17.86% of Python3 online submissions for Course Schedule II.
        总结:
        这个实现有些复杂,逻辑复杂,难以理解.并且复杂的代码容易出错.需要找到一个更容易理解,代码清晰的实现.
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
                    # dfs 先遍历后继节点
                    for c in courseList:
                        if not dfs(c):
                            return False
                    # dfs 再处理自己节点
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

    def findOrder_3(self, numCourses, prerequisites):
        """
        findOrder_2的优化版本.是逻辑更清晰,实现更简单,容易理解
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        finishedDict = {}  # key:num,value:1表示正在遍历中;2表示已经处理完成

        def dfs(num):
            """
            :param num:
            :return: False->存在循环依赖
            """
            if num in finishedDict.keys():
                return finishedDict[num] == 2
            finishedDict[num] = 1
            # 遍历后继节点
            for pair in prerequisites:
                if num == pair[1] and not dfs(pair[0]):
                    return False
            # 加入当前节点
            ret.append(num)
            finishedDict[num] = 2
            return True

        for num in range(numCourses):
            if not dfs(num):
                return []

        # 反转list 为 stack
        ret.reverse()
        return ret

    def findOrder_4(self, numCourses, prerequisites):
        """
        参考思路:
        https://leetcode.com/articles/course-schedule-ii/
        参考其中的dfs方法
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        # key:num,value:0表示未开始;1表示正在遍历中;2表示已经处理完成
        finishedDict = {k: 0 for k in range(numCourses)}
        hasCircle = False

        def dfs(num):
            """
            :param num:
            :return:
            """
            nonlocal hasCircle
            if finishedDict[num] == 1:
                hasCircle = True
            if finishedDict[num] > 0:
                return
            finishedDict[num] = 1
            # 遍历后继节点
            for pair in prerequisites:
                if num == pair[1]:
                    dfs(pair[0])
            # 加入当前节点
            ret.append(num)
            finishedDict[num] = 2
            return True

        for num in range(numCourses):
            if finishedDict[num] == 0:
                dfs(num)

        return ret[::-1] if not hasCircle else []

    def findOrder_5(self, numCourses, prerequisites):
        """
        参考思路:
        https://leetcode.com/articles/course-schedule-ii/
        参考其中的dfs方法
        与参考思路中几乎完全一致的实现
        结果:
        Runtime: 120 ms, faster than 54.22% of Python3 online submissions for Course Schedule II.
        Memory Usage: 17.6 MB, less than 7.14% of Python3 online submissions for Course Schedule II.
        结论:
        性能有较大的提升,因为使用了adj_list = collections.defaultdict(list)来优化循环查找后继节点的耗时
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        adj_list = collections.defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)

        # key:num,value:0表示未开始;1表示正在遍历中;2表示已经处理完成
        finishedDict = {k: 0 for k in range(numCourses)}
        hasCircle = False

        def dfs(num):
            """
            :param num:
            :return:
            """
            nonlocal hasCircle
            finishedDict[num] = 1
            # 遍历后继节点
            if num in adj_list:
                for successor in adj_list[num]:
                    if finishedDict[successor] == 0:
                        dfs(successor)
                    elif finishedDict[successor] == 1:
                        hasCircle = True
            # 加入当前节点
            ret.append(num)
            finishedDict[num] = 2
            return True

        for num in range(numCourses):
            if finishedDict[num] == 0:
                dfs(num)

        return ret[::-1] if not hasCircle else []

    def findOrder_6(self, numCourses, prerequisites):
        """
        参考思路:
        https://leetcode.com/articles/course-schedule-ii/
        参考其中的in-degree方法
        1.计算in-degree
        2.in-degree=0的入队
        3.在gragh中去掉入队的点,重复1,2步骤
        4.如果没有in-dgree=0的点,表示存在环
        结果:
        Runtime: 216 ms, faster than 9.95% of Python3 online submissions for Course Schedule II.
        Memory Usage: 15.1 MB, less than 60.71% of Python3 online submissions for Course Schedule II.
        结论:
        性能一般,有优化空间
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        indegree_dict = {}
        outdegree_dict = {}
        for n in range(numCourses):
            indegree_dict[n] = []
            outdegree_dict[n] = []
        for dest, src in prerequisites:
            indegree_dict[dest].append(src)
            outdegree_dict[src].append(dest)

        while len(indegree_dict) > 0:
            has_circle = True
            # 注意此处不能写为for s in indegree_dict.keys(): 会报错误:dictionary changed size during iteration
            for s in list(indegree_dict.keys()):
                if len(indegree_dict[s]) == 0:
                    has_circle = False
                    # indegree=0的先入队
                    ret.append(s)
                    # 重新计算indegee
                    for d1 in outdegree_dict[s]:
                        indegree_dict[d1].remove(s)
                    # 清理
                    indegree_dict.pop(s)
                    outdegree_dict.pop(s)
            if has_circle:
                return []
        return ret

    def findOrder_7(self, numCourses, prerequisites):
        """
        参考思路:
        https://leetcode.com/articles/course-schedule-ii/
        参考其中的in-degree方法
        与参考思路中几乎完全一致的实现
        结果:
        Runtime: 120 ms, faster than 54.22% of Python3 online submissions for Course Schedule II.
        Memory Usage: 15.3 MB, less than 60.71% of Python3 online submissions for Course Schedule II.
        结论:性能相对较好
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses is None or numCourses <= 0:
            return []
        ret = []
        adj_list = collections.defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree_list = [n for n in range(numCourses) if n not in indegree]

        while zero_indegree_list:
            n = zero_indegree_list.pop()
            ret.append(n)
            if n in adj_list:
                for d in adj_list[n]:
                    indegree[d] -= 1
                    if indegree[d] == 0:
                        zero_indegree_list.append(d)

        return ret if len(ret) == numCourses else []


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

    n = 3
    p = [[0, 2], [1, 2], [2, 0]]
    ret = Solution().findOrder(n, p)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
