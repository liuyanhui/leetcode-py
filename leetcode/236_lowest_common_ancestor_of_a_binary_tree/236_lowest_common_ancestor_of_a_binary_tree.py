"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
236. Lowest Common Ancestor of a Binary Tree
Medium
------------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""


class TreeNode:
    def __init__(self, x=-1):
        self.val = x
        self.left = None
        self.right = None

    def generate_tree(self, node_list, index):
        """根据list生成tree"""
        if index >= len(node_list):
            return None

        if node_list[index] > 0:
            node = TreeNode(node_list[index])
        else:
            return None

        if 2 * index + 1 < len(node_list):
            node.left = self.generate_tree(node_list, 2 * index + 1)
        if 2 * index + 2 < len(node_list):
            node.right = self.generate_tree(node_list, 2 * index + 2)

        return node


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestor_3(root, p, q)

    def lowestCommonAncestor_1(self, root, p, q):
        """
        普通思路
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root:
            return
        if not p or not q:
            return
        if p == q:
            return p

        # DFS 找到节点,保存路径
        p_path = []
        q_path = []
        self.dfs_find(root, p, p_path)
        self.dfs_find(root, q, q_path)
        print(len(p_path))
        print(len(q_path))

        # 从头同时遍历两个路径,直到第一个不同的路径节点,返回该节点的上个节点
        last = TreeNode()
        min_len = min(len(p_path), len(q_path))
        for i in range(min_len):
            if p_path[i] == q_path[i]:
                last = q_path[i]
            else:
                break

        print(last)
        print(last.val)
        return last

    def dfs_find(self, node, target, path):
        path.append(node)
        if node.val == target.val:
            return True

        finded = False
        if node.left:
            finded = self.dfs_find(node.left, target, path)
            if finded:
                return True

        if node.right and not finded:
            finded = self.dfs_find(node.right, target, path)
            if finded:
                return True

        path.remove(node)

    def lowestCommonAncestor_recusive(self, root, p, q):
        """
        递归思路:
        https://leetcode.com/articles/lowest-common-ancestor-of-a-binary-tree/
        1.如果(左子树包含p且右子树包含q) or (左子树包含q且右子树包含p),那么当前节点就是公共最小ancestor
        2.两个方法,一个负责递归遍历,一个负责查找是否包含目标节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or not q or not q:
            return 0
        ret = None

        def dfs(node):
            nonlocal ret
            if not node:
                return False
            mid = node.val == p.val or node.val == q.val
            left = dfs(node.left)
            right = dfs(node.right)
            # python 特点,bool数据可以相加
            if mid + left + right >= 2:
                ret = node
            return mid or left or right

        dfs(root)
        print(ret)
        return ret


def main():
    node_list = [3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4]
    # node_list = [2, -1, 2]
    root = TreeNode().generate_tree(node_list, 0)

    p = TreeNode(5)
    q = TreeNode(1)

    Solution().lowestCommonAncestor(root, p, q)


if __name__ == "__main__":
    main()
