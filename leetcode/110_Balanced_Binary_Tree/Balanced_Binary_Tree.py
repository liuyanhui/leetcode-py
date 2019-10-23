"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
Easy
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        # 下面的函数只是跟类名一样的普通方法,不是构造函数
        # def TreeNode(self, x):
        #     self.val = x
        #     self.left = None
        #     self.right = None


class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        # 左子树height,右子树height,相差1
        balance = self.tree_height(root)

        return balance != -1

    def tree_height(self, root):
        if not root:
            return 0
        left = self.tree_height(root.left)
        right = self.tree_height(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        return max(left, right) + 1

    def arrary_to_tree(self, arr, beg=0):
        """
        数组转化为二叉树
        :param arr:
        :return:
        """
        if not arr or len(arr) == 0 or beg >= len(arr):
            return None
        if arr[beg] is None:
            return None

        root = TreeNode(arr[beg])
        root.left = self.arrary_to_tree(arr, 2 * beg + 1)
        root.right = self.arrary_to_tree(arr, 2 * beg + 2)
        return root

    def convert_then_ops(self, arr):
        root = self.arrary_to_tree(arr, 0)
        ret = self.isBalanced(root)
        return ret


def main():
    a = [3, 9, 20, None, None, 15, 7]
    ret = Solution().convert_then_ops(a)
    print(ret)

    a = [1, 2, 2, 3, 3, None, None, 4, 4]
    ret = Solution().convert_then_ops(a)
    print(ret)

    a = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    ret = Solution().convert_then_ops(a)
    print(ret)


if __name__ == "__main__":
    main()
