"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
1026. Maximum Difference Between Node and Ancestor
Medium
-----------------------
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
import leetcode.common_util.array_to_tree_util as array_to_tree


class Solution:
    def maxAncestorDiff(self, root):
        return self.maxAncestorDiff_2(root)

    def maxAncestorDiff_1(self, root):
        """
        只是普通的binary tree,没有经过排序等处理
        采用dfs+先序遍历结合的思路,
        节点入栈时,计算跟所有ancestor的差,然后保存当前最小值
        ------------------
        执行结果:
        Runtime: 2776 ms, faster than 5.06% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
        Memory Usage: 20.8 MB, less than 11.11% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
        ------------------
        结果分析:
        时间复杂度:O(N*logN)
        性能较差,使用BUD方法进行优化,计算max部分可以优化
        :param root:
        :return:
        """
        if not root:
            return 0
        ret = 0
        stack = []

        def dfs_calc(node):
            nonlocal ret
            if not node:
                return
            for s in stack:
                ret = max(abs(s - node.val), ret)
            stack.append(node.val)
            dfs_calc(node.left)
            dfs_calc(node.right)
            stack.pop()

        dfs_calc(root)
        return ret

    def maxAncestorDiff_2(self, root):
        """
        基于maxAncestorDiff_1()的性能优化版本,
        参考思路:
        https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274610/JavaC%2B%2BPython-Top-Down
        -------------
        运行结果:
        Runtime: 44 ms, faster than 86.05% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
        Memory Usage: 20.9 MB, less than 11.11% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
        ------------------
        结果分析:
        性能有很大提升
        是假复杂度O(N)
        :param root:
        :return:
        """

        def dfs(node, mx, mn):
            if not node:
                return mx - mn
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            return max(dfs(node.left, mx, mn), dfs(node.right, mx, mn))

        return dfs(root, root.val, root.val)


def main():
    a = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().maxAncestorDiff(r)
    print(ret)
    print("---------------")

    a = [8]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().maxAncestorDiff(r)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
