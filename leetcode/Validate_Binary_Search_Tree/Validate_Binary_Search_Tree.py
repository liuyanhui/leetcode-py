"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
medium
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        if root is None:
            return True
        if root.left is None:
            left_val = -999999
        else:
            left_val = root.left.val

        if root.right is None:
            right_val = 999999
        else:
            right_val = root.right.val
        # print(left_val,right_val)

        if left_val < root.val < right_val:
            left = self.isValidBST(root.left)
            right = self.isValidBST(root.right)
            # print(left,right)
            if left and right:
                return True
        return False

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
        ret = self.isValidBST2(root)
        return ret

    list_root = []

    def isValidBST2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # 中序遍历
        self.traverse_bst(root)
        print(self.list_root)
        i = 0
        while i + 1 < len(self.list_root):
            if self.list_root[i] >= self.list_root[i + 1]:
                return False
            i += 1
        return True

    def traverse_bst(self, root):
        if root is None:
            return 0
        print(root.val)
        self.traverse_bst(root.left)
        self.list_root.append(root.val)
        self.traverse_bst(root.right)


def main():
    # a = [2, 1, 3]
    # ret = Solution().trans_to_treenode_then_calc(a)
    # print(ret)

    # a = [10, 5, 15, None, None, 6, 20]
    # ret = Solution().trans_to_treenode_then_calc(a)
    # print(ret)

    a = [0]
    ret = Solution().trans_to_treenode_then_calc(a)
    print(ret)

if __name__ == "__main__":
    main()
