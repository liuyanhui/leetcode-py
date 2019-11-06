"""
https://leetcode.com/problems/course-schedule/
207. Course Schedule
Medium
------------------------
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
import collections


class Solution:
    def canFinish(self, numCourses, prerequisites):
        return self.canFinish_3(numCourses, prerequisites)

    def canFinish_1(self, numCourses, prerequisites):
        """
        采用course-schedule-ii的思路,根据in-degree进行计算得出
        1.找出in-degree是0的节点,即找出没有前置课程的节点
        2.删除in-degree是0的节点,并将这些节点记录到已访问hashtable中
        3.重复步骤1和2,直到没有in-degree是0的节点
        4.最终所有节点都被删除,返回True;否则返回False
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses <= 0:
            return []
        # 初始化adjacent list
        adjacent_list = [[] for i in range(numCourses)]
        for p in prerequisites:
            adjacent_list[p[1]].append(p[0])

        # 初始化in-degree数组
        zero_in_degree_index = []
        in_degree = [0 for i in range(numCourses)]
        for p in prerequisites:
            in_degree[p[0]] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                zero_in_degree_index.append(i)
        while zero_in_degree_index:
            tmp = []
            for i in zero_in_degree_index:
                for j in adjacent_list[i]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        tmp.append(j)
            zero_in_degree_index = tmp
        return sum(in_degree) == 0

    def canFinish_2(self, numCourses, prerequisites):
        """
        canFinish_1()的简化版本
        -----------
        执行结果:
        Runtime: 96 ms
        Memory Usage: 13.8 MB
        性能非常好
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses <= 0:
            return False
        # 初始化adjacent list
        adjacent_list = [[] for i in range(numCourses)]
        # 初始化in-degree数组
        in_degree = [0 for i in range(numCourses)]
        for p in prerequisites:
            in_degree[p[0]] += 1
            adjacent_list[p[1]].append(p[0])

        # 初始化in-degree为0的节点列表
        zero_in_degree_index = [n for n in range(len(in_degree)) if in_degree[n] == 0]

        while zero_in_degree_index:
            tmp = []
            for i in zero_in_degree_index:
                for j in adjacent_list[i]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        tmp.append(j)
            zero_in_degree_index = tmp
        return sum(in_degree) == 0

    def canFinish_3(self, numCourses, prerequisites):
        """
        采用遍历法,如果gragh中存在环,返回false
        -----------
        执行结果:
        Runtime: 880 ms, faster than 8.15% of Python3 online submissions for Course Schedule.
        Memory Usage: 15.8 MB, less than 61.22% of Python3 online submissions for Course Schedule.
        性能较差
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if numCourses <= 0:
            return False
        adajcent_list = collections.defaultdict(list)
        for p in prerequisites:
            adajcent_list[p[1]].append(p[0])

        def dfs(c, c_path=set()):
            if c in c_path:
                return False
            c_path.add(c)
            for t_c in adajcent_list[c]:
                if not dfs(t_c, c_path):
                    return False
            c_path.remove(c)
            return True

        for n in range(numCourses):
            n_path = set()
            if not dfs(n, n_path):
                return False
        return True


def main():
    n = 2
    p = [[1, 0]]
    ret = Solution().canFinish(n, p)
    print(ret)
    print("--------------------")

    n = 2
    p = [[1, 0], [0, 1]]
    ret = Solution().canFinish(n, p)
    print(ret)
    print("--------------------")

    n = 2
    p = []
    ret = Solution().canFinish(n, p)
    print(ret)
    print("--------------------")

    n = 20
    p = [[1, 0]]
    ret = Solution().canFinish(n, p)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
