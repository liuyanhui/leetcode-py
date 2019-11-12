"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104. Maximum Depth of Binary Tree
Easy
-----------
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
import leetcode.common_util.array_to_tree_util as array_2_tree


class Solution:
    def maxDepth(self, root):
        return self.maxDepth_1(root)

    def maxDepth_1(self, root):
        if not root:
            return 0
        ret = 0

        def calc_max_depth(node, height):
            nonlocal ret
            if not node.left and not node.right:
                ret = max(ret, height)
                return
            if node.left:
                calc_max_depth(node.left, height + 1)
            if node.right:
                calc_max_depth(node.right, height + 1)

        calc_max_depth(root, 1)
        return ret

    def maxDepth_2(self, root):
        if not root:
            return 0
        if root is None:
            return 0
        left = self.maxDepth_2(root.left)
        right = self.maxDepth_2(root.right)
        return max(left, right) + 1


def main():
    a = [3]
    util = array_2_tree.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(a)
    ret = Solution().maxDepth(s)
    print(ret)
    print("--------------------")

    a = [3, 9, 20, None, None, 15, 7]
    util = array_2_tree.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(a)
    ret = Solution().maxDepth(s)
    print(ret)
    print("--------------------")

    a = [1, 2, 3, 4, None, None, 5]
    util = array_2_tree.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(a)
    ret = Solution().maxDepth(s)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
