"""
https://leetcode.com/problems/minimum-height-trees/
310. Minimum Height Trees
Medium
---------------------
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
import collections


class Solution:
    def findMinHeightTrees(self, n, edges):
        return self.findMinHeightTrees_6(n, edges)

    def findMinHeightTrees_1(self, n, edges):
        """
        思路:
        1.遍历所有的节点作为root的数,并计算height,结果缓存在list中
        2.list中最小值即为所求
        tip:树的height是最大子树的height
        ---------------------
        验证不通过,原因:Time Limit Exceeded
        逻辑正确,但是性能很差
        time complexity:O(N*N)
        :param n:
        :param edges:
        :return:
        """
        if n <= 0:
            return []
        adjacent_list = collections.defaultdict(list)
        for e in edges:
            adjacent_list[e[0]].append(e[1])
            adjacent_list[e[1]].append(e[0])

        def dfs_height(num, visited=set()):
            visited.add(num)
            tmp_ret_list = [len(visited)]
            for t_n in adjacent_list[num]:
                if t_n in visited:
                    continue
                tmp_ret_list.append(dfs_height(t_n, visited))
            visited.remove(num)
            return max(tmp_ret_list)

        height_list = [dfs_height(i, set()) for i in range(n)]
        mht_hegith = min(height_list)
        ret = [i for i in range(len(height_list)) if height_list[i] == mht_hegith]
        return ret

    def findMinHeightTrees_2(self, n, edges):
        """
        findMinHeightTrees_1()的优化,使用BUD办法.
        1.findMinHeightTrees_1()中的Bottleneck是每个节点都需要遍历,这其中必然存在D的重复计算,
        2.可以把遍历过的height先缓存起来,避免重复计算.
        核心思路如下如下:
        a.从i到j方向的height可以缓存起来,即为height["i-j"]=h.
        b.每个节点的树深度就是1+max(子节点height)
        ---------------
        验证通过,性能很差
        Runtime: 444 ms
        Memory Usage: 25.2 MB
        time complexity:O(N)
        :param n:
        :param edges:
        :return:
        """
        if n <= 0:
            return []
        adjacent_list = collections.defaultdict(list)
        for e in edges:
            adjacent_list[e[0]].append(e[1])
            adjacent_list[e[1]].append(e[0])
        # 缓存从i到子节点j的height
        height_dict_cache = collections.defaultdict(int)

        def recursive_height(num, visited=set()):
            visited.add(num)
            tmp_max_height = 0
            for t_n in adjacent_list[num]:
                # 跳过,不访问父节点
                if t_n in visited:
                    continue
                key = str(num) + '-' + str(t_n)
                if height_dict_cache[key] == 0:
                    # tip:关键点,需要明确递归的本质
                    height_dict_cache[key] = 1 + recursive_height(t_n, visited)
                tmp_max_height = max(tmp_max_height, height_dict_cache[key])
            visited.remove(num)
            return tmp_max_height

        height_list = [recursive_height(i, set()) for i in range(n)]
        min_height = min(height_list)
        ret = [i for i in range(len(height_list)) if height_list[i] == min_height]
        return ret

    def findMinHeightTrees_3(self, n, edges):
        """
        findMinHeightTrees_3()代码优化,针对结果部分进行优化.
        执行结果没有太大变化,这个优化意义不大
        ---------------
        验证通过,性能很差
        Runtime: 448 ms
        Memory Usage: 25.1 MB
        time complexity:O(N)
        :param n:
        :param edges:
        :return:
        """
        if n <= 0:
            return []
        adjacent_list = collections.defaultdict(list)
        for e in edges:
            adjacent_list[e[0]].append(e[1])
            adjacent_list[e[1]].append(e[0])
        # 缓存从i到子节点j的height
        height_dict_cache = collections.defaultdict(int)

        def recursive_height(num, visited=set()):
            visited.add(num)
            tmp_max_height = 0
            for t_n in adjacent_list[num]:
                # 跳过,不访问父节点
                if t_n in visited:
                    continue
                key = str(num) + '-' + str(t_n)
                if height_dict_cache[key] == 0:
                    height_dict_cache[key] = 1 + recursive_height(t_n, visited)
                tmp_max_height = max(tmp_max_height, height_dict_cache[key])
            visited.remove(num)
            return tmp_max_height

        ret = []
        min_height = 99999999
        for i in range(n):
            tmp = recursive_height(i, set())
            if min_height >= tmp:
                if min_height > tmp:
                    min_height = tmp
                    ret.clear()
                ret.append(i)
        return ret

    def findMinHeightTrees_4(self, n, edges):
        """
        参考思路:https://leetcode.com/problems/minimum-height-trees/discuss/76052/Two-O(n)-solutions
        参考上面的思路1
        思路:
        1.从随机一个节点i开始,找到他的最大深度的叶子节点j
        2.从节点j开始重复一次步骤1,得到节点k,并记录从j到k的过程为longest_list
        3.longest_list中最中间的一个或者两个节点就是所求
        ----------------
        验证通过,性能有较大提升
        Runtime: 280 ms, faster than 58.97% of Python3 online submissions for Minimum Height Trees.
        Memory Usage: 21.1 MB, less than 12.50% of Python3 online submissions for Minimum Height Trees.
        :param n:
        :param edges:
        :return:
        """
        if n < 2:
            return [i for i in range(n)]
        # 初始化邻接列表
        adjacent_list = collections.defaultdict(list)
        for e in edges:
            adjacent_list[e[0]].append(e[1])
            adjacent_list[e[1]].append(e[0])

        path = []

        def find_max_path(m, visited_list=[]):
            nonlocal path
            # 跳过父节点
            if len(visited_list) > 1 and m == visited_list[-2]:
                return
            visited_list.append(m)
            for i in adjacent_list[m]:
                find_max_path(i, visited_list)
            if len(visited_list) > len(path):
                path = visited_list.copy()
            visited_list.pop()

        # 从随机一个节点i开始,找到他的最大深度的叶子节点j
        find_max_path(0, [])
        # 从节点j开始重复一次步骤1,得到节点k,并记录从j到k的过程为longest_list
        find_max_path(path[-1], [])
        k = len(path)
        # longest_list中最中间的一个或者两个节点就是所求
        return path[(k - 1) // 2: k // 2 + 1]
        # 返回结果的另一种实现方式,虽然啰嗦但是易懂
        # if k % 2 == 0:
        #     return [path[k // 2 - 1], path[k // 2]]
        # else:
        #     return [path[k // 2]]

    def findMinHeightTrees_5(self, n, edges):
        """
        参考思路:https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
        与findMinHeightTrees_4的原理一样,但是实现却截然不同,并且更加简单
        1.去掉graph(注意不是tree,而是graph)中所有的叶子节点,生成新的graph
        2.重复步骤1,直到graph中只剩下1个或者2个节点
        3.最后剩下的节点就是所求
        --------------
        验证通过:性能一般,但是实现非常简单.性能一般,优化见findMinHeightTrees_6().
        Runtime: 788 ms, faster than 16.70% of Python3 online submissions for Minimum Height Trees.
        Memory Usage: 16.6 MB, less than 75.00% of Python3 online submissions for Minimum Height Trees.
        :param n:
        :param edges:
        :return:
        """
        if n < 2:
            return [i for i in range(n)]
        adajcent_list = collections.defaultdict(list)
        for e in edges:
            adajcent_list[e[0]].append(e[1])
            adajcent_list[e[1]].append(e[0])

        leafs = []
        while len(adajcent_list) > 2:
            for k in adajcent_list.keys():  # 这段代码可能是bottleneck
                if len(adajcent_list[k]) == 1:
                    leafs.append(k)
            for l in leafs:
                tmp = adajcent_list[l].pop()
                adajcent_list[tmp].remove(l)  # 经验证(将adajcent_list替换为collections.defaultdict(set)),这段代码不是bottleneck
                adajcent_list.pop(l)
            leafs.clear()

        return [i for i in adajcent_list.keys()]

    def findMinHeightTrees_6(self, n, edges):
        """
        findMinHeightTrees_5()的优化版本
        -----------
        验证通过,性能还不错:
        Runtime: 248 ms, faster than 98.61% of Python3 online submissions for Minimum Height Trees.
        Memory Usage: 17.3 MB, less than 75.00% of Python3 online submissions for Minimum Height Trees.
        :param n:
        :param edges:
        :return:
        """
        if n == 1: return [0]
        adajcent_list = collections.defaultdict(set)
        for e in edges:
            adajcent_list[e[0]].add(e[1])
            adajcent_list[e[1]].add(e[0])

        leafs = [i for i in adajcent_list.keys() if len(adajcent_list[i]) == 1]
        while len(adajcent_list) > 2:
            tmp_leafs = []
            for l in leafs:
                tmp = adajcent_list[l].pop()
                adajcent_list[tmp].remove(l)
                adajcent_list.pop(l)
                if len(adajcent_list[tmp]) == 1:
                    tmp_leafs.append(tmp)
            leafs = tmp_leafs

        return leafs

    def findMinHeightTrees_error_1(self, n, edges):
        """
        暴力法,采用dfs方法遍历每个节点,记录每个节点的MHT,最终通过得到最小MHT得到节点列表
        ========================
        审题错误,没有理解MHT的含义.
        :param n:
        :param edges:
        :return:
        """
        if n <= 0:
            return []

        adjacent_list = collections.defaultdict(list)
        for e in edges:
            adjacent_list[e[0]].append(e[1])
            adjacent_list[e[1]].append(e[0])

        def dfs(num, visited=set()):
            visited.add(num)
            tmp_dfs_list = []
            for t_n in adjacent_list[num]:
                if t_n in visited:
                    continue
                tmp_dfs_list.append(dfs(t_n, visited))
            if tmp_dfs_list:
                tmp_ret = min(tmp_dfs_list)
            else:
                tmp_ret = len(visited)
            visited.remove(num)
            return tmp_ret

        mht_ret = [dfs(i, set()) for i in range(n)]
        min_mht_ret = min(mht_ret)
        ret = []
        for i in range(len(mht_ret)):
            if min_mht_ret == mht_ret[i]:
                ret.append(i)
        return ret


def main():
    n = 1
    edges = []
    ret = Solution().findMinHeightTrees(n, edges)
    print(ret)
    print("--------------------")

    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    ret = Solution().findMinHeightTrees(n, edges)
    print(ret)
    print("--------------------")

    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    ret = Solution().findMinHeightTrees(n, edges)
    print(ret)
    print("--------------------")

    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    ret = Solution().findMinHeightTrees(n, edges)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
