"""
本题在leetcode和geeksforgeeks上都有.
---------------------------
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
987. Vertical Order Traversal of a Binary Tree
Medium
---------------------------
Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.

Note:
The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
---------------------------
https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
---------------------------
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.
           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9

The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
"""
import leetcode.common_util.array_to_tree_util as array_to_tree
import collections;


class Solution:
    def verticalTraversal(self, root):
        return self.verticalTraversal_4(root)

    def verticalTraversal_1(self, root):
        """
        leetcode中的题干已经给出了解题思路.
        思路总结如下:
        如果把tree看成二维象限的话,根节点就是原点,其坐标是x=0/y=0,根节点的做孩子坐标是x=-1/y=-1,依次类推.
        根据本题要求,只需要考虑x轴即可.在遍历过程中通过x坐标的增减修改结果集.
        --------------
        审题错误!
        本方法解决的是geeksforgeeks的问题,没有解决leetcode的问题,因为它只考虑了x坐标没有考虑y坐标.
        :return:
        """
        if not root:
            return []
        ret_m = []
        ret_l = []
        ret_r = []

        def do_traverse(node, x):
            """
            采用dfs遍历,先序遍历
            """
            if not node:
                return
            if x == 0:
                if len(ret_m) == 0:
                    ret_m.append([node.val])
                else:
                    # 需要排序插入
                    insert_sort(ret_m[0], node.val)
            elif x > 0:
                tmp_x = x - 1
                if tmp_x < len(ret_r):
                    # 需要排序插入
                    insert_sort(ret_r[tmp_x], node.val)
                else:
                    ret_r.append([node.val])
            elif x < 0:
                tmp_x = abs(x) - 1
                if tmp_x < len(ret_l):
                    # 需要排序插入
                    insert_sort(ret_l[tmp_x], node.val)
                else:
                    ret_l.append([node.val])

            do_traverse(node.left, x - 1)
            do_traverse(node.right, x + 1)

        def insert_sort(sorted_list, item):
            sorted_list.append(item)
            sorted_list.sort()

        do_traverse(root, 0)
        ret_l.reverse()
        return ret_l + ret_m + ret_r

    def verticalTraversal_2(self, root):
        """
        1.采用dfs+先序遍历
        2.用两个队列暂存遍历结果(分别是x=0,x>0,x<0),每个队列先根据y的值排序,y值相同时从小到大排序
        3.与verticalTraversal_1()思路大体一致
        --------------
        审题有误!
        该方法没有解决从上到下遍历的顺序问题,必须严格按照从上到下的顺序进行输出.如:x相同时,y离跟越近,输出时越靠前
        :param root:
        :return:
        """
        if not root:
            return []
        # 以下分别对应x=0,x>0,x<0;
        # ret_m格式为二维数组,第一维下标表示y,第二维下标表示y相同时根据大小排序的val数组
        # ret_r, ret_l格式为三位数组,在第一维下标表示x坐标,第二维下标表示y,第三维下标表示y相同时根据大小排序的val数组
        ret_m, ret_r, ret_l = [], [], []

        def do_traverse(node, x, y):
            if not node:
                return
            tmp_y = abs(y) - 1
            tmp_x = abs(x) - 1
            if x == 0:
                do_the_same_y(abs(y), ret_m, node)
            elif x > 0:
                if tmp_x < len(ret_r):
                    do_the_same_y(tmp_y, ret_r[tmp_x], node)
                else:
                    ret_r.append([node.val])
            else:
                if tmp_x < len(ret_l):
                    do_the_same_y(tmp_y, ret_l[tmp_x], node)
                else:
                    ret_l.append([node.val])

            do_traverse(node.left, x - 1, y - 1)
            do_traverse(node.right, x + 1, y - 1)

        def do_the_same_y(y, ret, node):
            if y < len(ret):
                insert_sort(ret[y], node.val)
            else:
                ret.append(node.val)

        def insert_sort(sorted_list, item):
            sorted_list.append(item)
            sorted_list.sort()

        do_traverse(root, 0, 0)

        ret_final = []
        for i in range(len(ret_l), 0, -1):
            ret_final.append(ret_l[i - 1])
        ret_final.append(ret_m)
        for i in range(len(ret_r)):
            ret_final.append(ret_r[i])

        return ret_final

    def verticalTraversal_3(self, root):
        """
        使用矩阵保存遍历结果,矩阵的下标[x][y]表示节点在tree中的坐标.坐标相同时,从小到大排列.
        逻辑如下:
        1.遍历tree,按照上诉规则将遍历结果保存在矩阵中
        2.遍历矩阵,输出为list
        3.矩阵中dict表示
        :param root:
        :return:
        """
        # 定义仿二维矩阵
        location_order_dict = collections.defaultdict(lambda: collections.defaultdict(list))

        def do_traverse(node, x, y):
            if not node:
                return
            # 以下注释的代码可优化,排序部分可以推后到生产ret的时候,以优化时间复杂度
            # if location_order_dict[x][y]:
            #     location_order_dict[x][y].append(node.val)
            #     location_order_dict[x][y].sort()
            # else:
            #     location_order_dict[x][y] = [node.val]
            # 简化后的代码
            location_order_dict[x][y].append(node.val)
            do_traverse(node.left, x - 1, y + 1)
            do_traverse(node.right, x + 1, y + 1)

        do_traverse(root, 0, 0)

        ret = []
        # 代码比较复杂,可以简化
        x_sorted_key_list = list(location_order_dict.keys())
        x_sorted_key_list.sort()
        for x in x_sorted_key_list:
            y_sorted_key_list = list(location_order_dict[x])
            y_sorted_key_list.sort()
            tmp_list = []
            for y in y_sorted_key_list:
                location_order_dict[x][y].sort()
                for t in location_order_dict[x][y]:
                    tmp_list.append(t)
            ret.append(tmp_list)
        return ret

    def verticalTraversal_4(self, root):
        """
        verticalTraversal_3()的代码优化版本.
        参考思路:
        https://leetcode.com/articles/vertical-order-traversal-of-a-binary-tree/
        :param root:
        :return:
        """
        # 定义仿二维矩阵
        location_order_dict = collections.defaultdict(lambda: collections.defaultdict(list))

        def do_traverse(node, x, y):
            if not node:
                return
            location_order_dict[x][y].append(node.val)
            do_traverse(node.left, x - 1, y + 1)
            do_traverse(node.right, x + 1, y + 1)

        do_traverse(root, 0, 0)

        ret = []
        # sort 与 sorted 区别：
        # 1.sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
        # 2.list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
        for x in sorted(location_order_dict):
            tmp_list = []
            for y in sorted(location_order_dict[x]):
                tmp_list.extend(sorted(val for val in location_order_dict[x][y]))
            ret.append(tmp_list)
        return ret


def main():
    a = [3, 9, 20, None, None, 15, 7]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")

    a = [1, 2, 3, 4, 5, 6, 7]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")

    a = [0, None, 1, 2, 3, None, None, 4, 5]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")

    a = [0, 1, None, None, 2, 6, 3, None, None, None, 4, None, 5]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")

    a = [0, 5, 1, 9, None, 2, None, None, None, None, 3, 4, 8, 6, None, None, None, 7]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")

    a = [0, 8, 1, None, None, 3, 2, None, 4, 5, None, None, 7, 6]
    r = array_to_tree.ArrayToTreeUtil().trans_array_to_treenode_2(a)
    ret = Solution().verticalTraversal(r)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
