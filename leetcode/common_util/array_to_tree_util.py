"""
数组到树的转换类
example1:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

注意:leetcode中的array-->tree,并不是严格意义上的广度搜索生产的数组,它会忽略null节点

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ArrayToTreeUtil:
    # @staticmethod
    def trans_array_to_treenode_1(self, arr, beg=0):
        """
        满二叉树式的转换方法
        :param arr:
        :param beg:
        :return:
        """
        if arr is None or len(arr) == 0 or beg >= len(arr) or arr[beg] is None:
            return None
        root = TreeNode(arr[beg])
        if root is None:
            return None
        root.left = ArrayToTreeUtil().trans_array_to_treenode_1(arr, 2 * beg + 1)
        root.right = ArrayToTreeUtil().trans_array_to_treenode_1(arr, 2 * beg + 2)

        return root

    def trans_array_to_treenode_2(self, arr, rank1=[], rank2=[]):
        """
        leetcode中的转换方法,跳过空节点
        :param arr:
        :param rank1:
        :param rank2:
        :return:
        """
        if arr is None or len(arr) == 0:
            return None
        root = TreeNode(arr[0])
        rank1.append(root)
        i = 1
        while i < len(arr):
            for rank1_node in rank1:
                if rank1_node:
                    if i >= len(arr):
                        break
                    rank1_node.left = TreeNode(arr[i])
                    rank2.append(rank1_node.left)
                    i += 1
                    if i >= len(arr):
                        break
                    rank1_node.right = TreeNode(arr[i])
                    rank2.append(rank1_node.right)
                    i += 1
            rank1 = rank2
            rank2 = []

        return root

    def preorder(self, root, ret_list=[]):
        if root is None:
            return
        ret_list.append(root.val)
        self.preorder(root.left, ret_list)
        self.preorder(root.right, ret_list)
        return ret_list

    def bfs_traverse(self, root):
        """
        广度优先遍历
        :param root:
        :return:
        """
        if root is None:
            return
        ret_list = [root.val]
        ret_node_list = [root]
        i = 0
        while i < len(ret_list):
            root = ret_node_list[i]
            if root:
                if root.left:
                    ret_list.append(root.left.val)
                    ret_node_list.append(root.left)
                if root.right:
                    ret_list.append(root.right.val)
                    ret_node_list.append(root.right)
            i += 1

        return ret_list


def main():
    a = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    # ret1 = ArrayToTreeUtil().trans_array_to_treenode_1(a)
    # print(ret1)
    ret2 = ArrayToTreeUtil().trans_array_to_treenode_2(a, [], [])
    list_1 = ArrayToTreeUtil().bfs_traverse(ret2)
    print(str(list_1))

    a = [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6]
    # ret1 = ArrayToTreeUtil().trans_array_to_treenode_1(a)
    # print(ret1)
    ret_2 = ArrayToTreeUtil().trans_array_to_treenode_2(a, [], [])
    print(ret_2)
    list_2 = ArrayToTreeUtil().bfs_traverse(ret_2)
    print(str(list_2))


if __name__ == "__main__":
    main()
