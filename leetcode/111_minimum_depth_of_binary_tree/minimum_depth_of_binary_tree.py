"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
111. Minimum Depth of Binary Tree
Easy
---------------------
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
import leetcode.common_util.array_to_tree_util as array_2_tree


# Amazon的面试题之一
class Solution:
    def minDepth(self, root):
        return self.minDepth_1(root)

    def minDepth_1(self, root):
        """
        What's the fuck going on?
        :param root:
        :return:
        """
        if not root:
            return 0
        ret = 999999

        def dfs(node, depth=0):
            nonlocal ret
            if not node.left and not node.right:
                ret = min(ret, depth)
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return ret


def main():
    a = [3, 9, 20, None, None, 15, 7]
    util = array_2_tree.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(a)
    ret = Solution().minDepth(s)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
