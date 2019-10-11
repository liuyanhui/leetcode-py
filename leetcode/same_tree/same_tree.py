"""
https://leetcode.com/problems/same-tree/
100. Same Tree
Easy
------------------------------------------
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true
Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""

import leetcode.common_util.array_to_tree_util as array_to_tree


class Solution:
    def isSameTree(self, p, q):
        return self.isSameTree_1(p, q)

    def isSameTree_1(self, p, q):
        """
        递归版本
        1.root相等
        2.left相等,right相等
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree_1(p.left, q.left) and self.isSameTree_1(p.right, q.right)

    def isSameTree_2(self, p, q):
        """
        非递归版本,使用栈替代递归
        :param p:
        :param q:
        :return:
        """
        p_stack = [p]
        q_stack = [q]

        while len(p_stack) > 0 or len(q_stack) > 0:
            p_n = p_stack.pop()
            q_n = q_stack.pop()
            if not p_n and not q_n:
                continue
            if not p_n or not q_n:
                return False
            if p_n.val != q_n.val:
                return False
            p_stack.append(p_n.left)
            p_stack.append(p_n.right)
            q_stack.append(q_n.left)
            q_stack.append(q_n.right)
        return True

    def isSameTree_3(self, p, q):
        """
        不能采用遍历后比较遍历结果的方法,应用存在二叉树所有节点的val相同的情况,会是的遍历后的结果无法体现遍历顺序.
        除非是搜索二叉树.
        :param p:
        :param q:
        :return:
        """
        return False


def main():
    p = [1, 2, 3]
    q = [1, 2, 3]
    p_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(p)
    q_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(q)
    ret = Solution().isSameTree(p_t, q_t)
    print(ret)
    print("---------------")

    p = [1, 2]
    q = [1, None, 2]
    p_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(p)
    q_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(q)
    ret = Solution().isSameTree(p_t, q_t)
    print(ret)
    print("---------------")

    p = [1, 2, 1]
    q = [1, 1, 2]
    p_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(p)
    q_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(q)
    ret = Solution().isSameTree(p_t, q_t)
    print(ret)
    print("---------------")

    p = [10, 5, 15]
    q = [10, 5, None, None, 15]
    p_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(p)
    q_t = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(q)
    ret = Solution().isSameTree(p_t, q_t)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
