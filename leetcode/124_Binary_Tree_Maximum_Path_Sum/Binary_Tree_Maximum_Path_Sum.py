"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
hard
"""
import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    max_sum_ret = -9999999

    def maxPathSum(self, root):
        if not root:
            return 0

        if root.left is None and root.right is None:
            return root.val

        self.find_clild_max_sum(root)

        return self.max_sum_ret

    def find_clild_max_sum(self, node):
        """
        返回最大的branch 的sum
        :param node:
        :return:
        """
        if node is None:
            return 0

        left = self.find_clild_max_sum(node.left)
        right = self.find_clild_max_sum(node.right)

        node_max_sum = max(left + node.val, right + node.val, node.val)
        self.max_sum_ret = max(left + node.val, right + node.val,
                               left + right + node.val, node.val, self.max_sum_ret)
        return node_max_sum

    @staticmethod
    def trans_array_to_treenode(arr, beg=0):
        if arr is None or len(arr) == 0 or beg >= len(arr) or arr[beg] is None:
            return None
        root = TreeNode(arr[beg])
        if root is None:
            return None
        root.left = Solution.trans_array_to_treenode(arr, 2 * beg + 1)
        root.right = Solution.trans_array_to_treenode(arr, 2 * beg + 2)

        return root

    def trans_to_treenode_then_calc(self, arr):
        root = Solution.trans_array_to_treenode(arr)
        ret = self.maxPathSum(root)
        return ret


def main():
    a = [1, 2, 3]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [-10, 9, 20, None, None, 15, 7]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [-10]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [1, -2, -3, 1, 3, -2, None, -1]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [-2, -1]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

    a = [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)


if __name__ == "__main__":
    main()
