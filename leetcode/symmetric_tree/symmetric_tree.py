"""
https://leetcode.com/problems/symmetric-tree/description/
101. Symmetric Tree
Easy
---------------------
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
import leetcode.common_util.array_to_tree_util as array_to_tree


class Solution:
    def isSymmetric(self, root):
        return self.isSymmetric_2(root)

    def isSymmetric_1(self, root):
        """
        1.中序遍历
        2.判断中序遍历的结果是否回文
        3.遍历时需要填充子节点为空的情况,规则为:如果left和right其中有一个为空,那么用null填充为空的节点;如果left和right全部为空,那么不填充
        运行结果:
        失败.部分用例不能通过.说明遍历法基本是行不通的.
        :param root:
        :return:
        """
        tra_l = []

        def inorder_traverse(node):
            if not node:
                tra_l.append("null")
                return
            if node.left or node.right:
                inorder_traverse(node.left)
            tra_l.append(str(node.val))
            if node.left or node.right:
                inorder_traverse(node.right)

        inorder_traverse(root)
        l, r = 0, len(tra_l) - 1
        while l < r:
            if tra_l[l] != tra_l[r]:
                return False
            l += 1
            r -= 1
        return True

    def isSymmetric_2(self, root):
        """
        采用递归思路
        1.根节点相等
        2.left.left==right.right and left.right==right.left
        3.递归执行1,2
        执行结果:
        Runtime: 36 ms, faster than 93.28% of Python3 online submissions for Symmetric Tree.
        Memory Usage: 13.6 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.
        :param root:
        :return:
        """
        if not root:
            return True

        def symmetric_l_r(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and symmetric_l_r(l.left, r.right) and symmetric_l_r(l.right, r.left)

        return symmetric_l_r(root.left, root.right)

    def isSymmetric_3(self, root):
        """
        另一种思路的遍历法,参考下文中的方法2:
        https://leetcode.com/articles/symmetric-tree/
        是递归思路的另一种实现,只不过没有使用递归实现而已.使用栈保存遍历过程.
        :param root:
        :return:
        """
        stack_l = [root]
        stack_r = [root]

        while len(stack_l) > 0 or len(stack_r) > 0:
            l = stack_l.pop()
            r = stack_r.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack_l.append(l.left)
            stack_r.append(r.right)
            stack_l.append(l.right)
            stack_r.append(r.left)
        return True


def main():
    a = [1, 2, 2, 3, 4, 4, 3]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")

    a = [1, 2, 2, None, 3, None, 3]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")

    a = []
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")

    a = [1]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")

    a = [1, 2, 2, 2, None, 2]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")

    a = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().isSymmetric(r)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
