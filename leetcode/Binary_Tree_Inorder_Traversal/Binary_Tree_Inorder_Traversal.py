"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/\
medium
"""

class TreeNode:

    def __init__(self,val):
        self.val  = val
        self.left=val
        self.right=val

class Solution:
    ret_list=[]
    #递归方式
    def inorderTraversal_old(self, root: TreeNode) -> List[int]:
        self.ret_list=[]
        if root is None:
            return self.ret_list
        self.do_inorder_traversal(root)
        return self.ret_list

    #使用递归
    def do_inorder_traversal(self,root):
        if root is None:
            return 0
        self.do_inorder_traversal(root.left)
        self.ret_list.append(root.val)
        self.do_inorder_traversal(root.right)

    #非递归方式
    def inorderTraversal(self,root):
        ret=[]
        if root is None:
            return ret
        stack=[]

        while root is not None or len(stack)>0:
            #入栈
            while root is not None:
                stack.append(root)
                root=root.left
            #出栈
            root=stack.pop()
            ret.append(root.val)
            root=root.right
        return ret


