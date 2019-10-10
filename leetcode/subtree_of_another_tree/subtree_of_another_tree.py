"""
https://leetcode.com/problems/subtree-of-another-tree/
572. Subtree of Another Tree
Easy
------------------------------
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

import leetcode.common_util.array_to_tree_util as ArrayToTreeUtil


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s, t):
        return self.isSubtree_5(s, t)

    def isSubtree_1(self, s, t):
        """
        思路1
        先对s和t进行遍历,再对遍历后的字符串进行比较
        1.分别对s和t进行先序,中序,后序遍历,遍历结果记为s1,t2;s2,t3;s3,t3
        2.如果所有的si包含ti,那么t是s的子树
        存在的问题:
        该方法无法处理t只有一个节点的情况.需要单独处理t只有一个节点的逻辑.
        :param s:
        :param t:
        :return:
        """

        def inorder_traverse(root, output):
            """
            中序遍历
            """
            if root is None:
                return
            inorder_traverse(root.left, output)
            output.append(root.val)
            inorder_traverse(root.right, output)

        def preorder_traverse(root, output):
            """
            先序遍历
            """
            if root is None:
                return
            output.append(root.val)
            preorder_traverse(root.left, output)
            preorder_traverse(root.right, output)

        def postorder_traverse(root, output):
            """
            后序遍历
            """
            if root is None:
                return
            postorder_traverse(root.left, output)
            postorder_traverse(root.right, output)
            output.append(root.val)

        inorder_s, inorder_t = [], []
        inorder_traverse(s, inorder_s)
        inorder_traverse(t, inorder_t)
        inorder_s = str(inorder_s)[1:-1]
        inorder_t = str(inorder_t)[1:-1]
        preorder_s, preorder_t = [], []
        preorder_traverse(s, preorder_s)
        preorder_traverse(t, preorder_t)
        preorder_s = str(preorder_s)[1:-1]
        preorder_t = str(preorder_t)[1:-1]
        postorder_s, postorder_t = [], []
        postorder_traverse(s, postorder_s)
        postorder_traverse(t, postorder_t)
        postorder_s = str(postorder_s)[1:-1]
        postorder_t = str(postorder_t)[1:-1]
        if inorder_s.find(inorder_t) >= 0 and preorder_s.find(preorder_t) >= 0 and postorder_s.find(
                postorder_t) >= 0:
            return True
        else:
            return False

    def isSubtree_2(self, s, t):
        """
        方法isSubtree_1()略微复杂,采用BUD (Bottlenecks,Unnecessary Work,Duplicated Work)的思路分析如下:
        1.分别做三次遍历是Duplicated work,可以精简
        优化思路如下:
        1.选择任意一种遍历方式
        2.遍历时,遇到叶子节点增加左子树和右子树分别为null
        3.只需要一种遍历方式即可解决问题
        运行结果:
        Runtime: 84 ms, faster than 91.62% of Python3 online submissions for Subtree of Another Tree.
        Memory Usage: 15.2 MB, less than 10.00% of Python3 online submissions for Subtree of Another Tree.
        运行结果分析:
        运行耗时尚可,但是内存使用率偏高.有优化的空间
        :param s:
        :param t:
        :return:
        """
        s_ret, t_ret = [], []

        def preorder_traverse(node, output):
            # 遇到叶子节点,补null
            if node is None:
                output.append("null")
                return
            output.append(str(node.val))
            preorder_traverse(node.left, output)
            preorder_traverse(node.right, output)

        preorder_traverse(s, s_ret)
        preorder_traverse(t, t_ret)

        if str(s_ret)[1:-1].find(str(t_ret)[1:-1]) >= 0:
            return True
        else:
            return False

    def isSubtree_3(self, s, t):
        """
        方法isSubtree_2()的优化版本,针对字符串是值传递而不是引用传递的一种方法
        :param s:
        :param t:
        :return:
        """
        s_ret, t_ret = [""], [""]

        def preorder_traverse(node, output):
            # 遇到叶子节点,补null
            if node is None:
                output[0] += ",null"
                return
            output[0] += "," + str(node.val)
            preorder_traverse(node.left, output)
            preorder_traverse(node.right, output)

        preorder_traverse(s, s_ret)
        preorder_traverse(t, t_ret)

        if s_ret[0].find(t_ret[0]) >= 0:
            return True
        else:
            return False

    def isSubtree_4(self, s, t):
        """
        思路2
        该问题核心退化为两个tree是否相同的问题
        结果Time Limit Exceeded
        :param s:
        :param t:
        :return:
        """

        def real_sub_tree(s1, t1):
            if s1 is None and t1 is None:
                return True
            if (s1 is None and t1 is not None) or (s1 is not None and t1 is None):
                return False
            # 出现Time Limit Exceeded的原因在这里:
            # 方法real_sub_tree()的责任不清晰,包含了额外的任务.如果把完全匹配的逻辑抽离出去,单独是一个函数,那么就会清晰很多,更容易理解和编码.
            # 参见isSubtree_5()
            if s1.val != t1.val:
                return real_sub_tree(s1.left, t) or real_sub_tree(s1.right, t)
            else:
                return (real_sub_tree(s1.left, t1.left) and real_sub_tree(s1.right, t1.right)) or (
                    real_sub_tree(s1.left, t)) or (real_sub_tree(s1.right, t))

        return real_sub_tree(s, t)

    def isSubtree_5(self, s, t):
        """
        isSubtree_4方法的优化版本
        参考思路:
        https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
        :param s:
        :param t:
        :return:
        """

        def isMatch(s1, t1):
            # 另外一种方式1
            # if not (s1 and t1):
            #     return s1 is t1
            # 另外一种方式2
            if not s1 and not t1:
                return True
            if not s1 or not t1:
                return False
            return (s1.val == t1.val and
                    isMatch(s1.left, t1.left) and
                    isMatch(s1.right, t1.right))

        if isMatch(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

def main():
    s_array = [3, 4, 5, 1, 2]
    t_array = [4, 1, 2]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [3, 4, 5, 1, 2, None, None, 0]
    t_array = [4, 1, 2]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [4, -9, 5, None, -1, None, 8, -6, 0, 7, None, None, -2, None, None, None, None, -3]
    t_array = [5]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [4]
    t_array = [4]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [14]
    t_array = [4]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [1, 1]
    t_array = [1]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")

    s_array = [3, 4, 5, 1, None, 2]
    t_array = [3, 1, 2]
    util = ArrayToTreeUtil.ArrayToTreeUtil()
    s = util.trans_array_to_treenode_2(s_array)
    t = util.trans_array_to_treenode_2(t_array)
    ret = Solution().isSubtree(s, t)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
