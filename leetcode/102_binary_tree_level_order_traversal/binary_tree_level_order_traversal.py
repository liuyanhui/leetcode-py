"""
https://www.geeksforgeeks.org/level-order-tree-traversal/

https://leetcode.com/problems/binary-tree-level-order-traversal/
102. Binary Tree Level Order Traversal
Medium
--------------------------------
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import leetcode.common_util.array_to_tree_util as array_to_tree


class Solution:
    def levelOrder(self, root):
        return self.levelOrder_3(root)

    def levelOrder_1(self, root):
        """
        bfs思路
        用两个队列存储数据,队列1保存当前level节点,队列2保存下一level节点
        :param root:
        :return:
        """
        if not root:
            return []
        ret = []
        q1 = [root]
        q2 = []
        while q1:
            tmp_ret = []
            for q in q1:
                tmp_ret.append(q.val)
                if q.left:
                    q2.append(q.left)
                if q.right:
                    q2.append(q.right)
            ret.append(tmp_ret)
            q1.clear()
            q1 = q2.copy()
            q2.clear()
        return ret

    def levelOrder_2(self, root):
        """
        bfs思路
        代码简化版本,更符合python风格的代码.精简代码量.
        参考思路:
        https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
        :param root:
        :return:
        """
        if not root:
            return []
        ret = []
        q1, q2 = [root], []
        while q1:
            ret.append([t.val for t in q1])
            q2 = [t for n in q1 for t in [n.left, n.right] if t]
            q1 = q2.copy()
            q2.clear()
        return ret

    def levelOrder_3(self, root):
        """
        dfs思路
        :param root:
        :return:
        """
        def dfs(node, level, ret):
            if not node:
                return
            if level > len(ret) - 1:
                ret.append([])
            ret[level].append(node.val)
            dfs(node.left, level + 1, ret)
            dfs(node.right, level + 1, ret)

        rs = []
        dfs(root, 0, rs)
        return rs


def main():
    a = [3, 9, 20, None, None, 15, 7]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().levelOrder(r)
    print(ret)
    print("---------------")

    a = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().levelOrder(r)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
