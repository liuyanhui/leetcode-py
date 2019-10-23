"""
107. Binary Tree Level Order Traversal II
Easy
--------------------------------
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

import leetcode.common_util.array_to_tree_util as array_to_tree


class Solution:
    def levelOrderBottom(self, root):
        return self.levelOrderBottom_2(root)

    def levelOrderBottom_1(self, root):
        """
        dfs思路
        :param root:
        :return:
        """
        if not root:
            return []

        def dfs(node, level, ret):
            if not node:
                return
            if level >= len(ret):
                ret.insert(0, [])
            ret[len(ret) - level - 1].append(node.val)
            dfs(node.left, level + 1, ret)
            dfs(node.right, level + 1, ret)

        rs = []
        dfs(root, 0, rs)
        return rs

    def levelOrderBottom_2(self, root):
        """
        bfs思路
        :param root:
        :return:
        """
        if not root:
            return []
        ret = []
        q1, q2 = [root], []
        while q1:
            ret.insert(0, [])
            ret[0].extend([q.val for q in q1])
            q2 = [q for n in q1 for q in (n.left, n.right) if q]
            q1 = q2.copy()
        return ret


def main():
    a = [3, 9, 20, None, None, 15, 7]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().levelOrderBottom(r)
    print(ret)
    print("---------------")

    a = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().levelOrderBottom(r)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
