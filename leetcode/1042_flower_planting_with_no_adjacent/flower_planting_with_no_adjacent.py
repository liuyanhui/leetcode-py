"""
https://leetcode.com/problems/flower-planting-with-no-adjacent/
1042. Flower Planting With No Adjacent
Easy
-----------------------
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
Also, there is no garden that has more than 3 paths coming into or leaving it.
Your task is to choose a flower type for each garden such that, for any two gardens connected by a path,
they have different types of flowers.
Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.
The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:
Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]

Example 2:
Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

Note:
1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
"""
import collections


class Solution:
    def gardenNoAdj(self, N, paths):
        return self.gardenNoAdj_1(N, paths)

    def gardenNoAdj_1(self, N, paths):
        """
        采用adjacent list保存图数据
        1.从1~N依次遍历每个garden的adjacent list
        2.对于garden i,先排除相邻节点已经种植的flower type,然后选择未被排除最小的type为i的flower type
        -------------
        验证通过,性能不错
        Runtime: 448 ms, faster than 91.40% of Python3 online submissions for Flower Planting With No Adjacent.
        Memory Usage: 19.4 MB, less than 100.00% of Python3 online submissions for Flower Planting With No Adjacent.
        :param N:
        :param paths:
        :return:
        """
        if not N or N <= 0:
            return []

        ret = [0 for i in range(N + 1)]
        adjacent_list = collections.defaultdict(list)
        for p in paths:
            adjacent_list[p[0]].append(p[1])
            adjacent_list[p[1]].append(p[0])

        for i in range(1, N + 1):
            neighbors = adjacent_list[i]
            if neighbors:
                types = [0, 1, 2, 3, 4]
                for n in neighbors:
                    if ret[n] > 0:
                        types[ret[n]] = -1
                for t in types:
                    if t > 0:
                        ret[i] = t
                        break
            else:
                ret[i] = 1

        return ret[1:]


def main():
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    ret = Solution().gardenNoAdj(N, paths)
    print(ret)
    print(ret == [1, 2, 3])
    print("--------------------")

    N = 4
    paths = [[1, 2], [3, 4]]
    ret = Solution().gardenNoAdj(N, paths)
    print(ret)
    print(ret == [1, 2, 1, 2])
    print("--------------------")

    N = 4
    paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
    ret = Solution().gardenNoAdj(N, paths)
    print(ret)
    print(ret == [1, 2, 3, 4])
    print("--------------------")


if __name__ == "__main__":
    main()
