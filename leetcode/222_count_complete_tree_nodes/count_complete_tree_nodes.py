"""
https://leetcode.com/problems/count-complete-tree-nodes/
222. Count Complete Tree Nodes
Medium
------------------
Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:
Input:
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right - right


class Solution:
    def countNodes(self, root):
        self.countNodes_brute_recusive_preorder(root)

    def countNodes_1(self, root):
        """
        利用完全二叉树的特点.
        1.通过中序遍历,遍历最左侧的子树,得到树的最大深度n
        2.从最右侧的子树开始,最后一个深度为n-1的子树,记序号为m.
        3.2**N-1-m
        时间复杂度为:O(logN)
        :param root:
        :return:
        """
        if not root:
            return 0
        tmp_node = root
        depth = 0
        # 计算树的深度
        while tmp_node:
            depth += 1
            tmp_node = tmp_node.left

        # 从最右侧子树开始,计算最后一个深度为depth-1的子树的序号
        def do_recursive_preorder_right_first(node, cur_depth, max_depth, serial):
            if not node:
                if cur_depth == max_depth:
                    return serial
                else:
                    serial += 1
            do_recursive_preorder_right_first(node.right, cur_depth + 1, max_depth, serial)
            do_recursive_preorder_right_first(node.left, cur_depth + 1, max_depth, serial)

    def countNodes_2(self, root):
        """
        参考思路:
        https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/wan-quan-er-cha-shu-de-jie-dian-ge-shu-by-leetcode/
        :param root:
        :return:
        """
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0

    def countNodes_brute_recusive_preorder(self, root):
        """
        使用普通的遍历的树的方式即可,时间复杂度为O(N).
        但是对于完全二叉树应该有比较其他高效的办法,可以从完全二叉树的特点进行思考.
        -----------
        验证通过:
        Runtime: 172 ms, faster than 5.31% of Python3 online submissions for Count Complete Tree Nodes.
        Memory Usage: 21.1 MB, less than 87.05% of Python3 online submissions for Count Complete Tree Nodes.
        :param root:
        :return:
        """
        if not root:
            return 0
        count = 0

        def do_recursive_preorder(node):
            if not node:
                return
            nonlocal count
            count += 1
            do_recursive_preorder(node.left)
            do_recursive_preorder(node.right)

        do_recursive_preorder(root)
        return count


def main():
    root = TreeNode(1, None, None)
    ret = Solution().countNodes(root)
    print(ret)
    print(ret == 6)
    print('--------------------')


if __name__ == "__main__":
    main()
