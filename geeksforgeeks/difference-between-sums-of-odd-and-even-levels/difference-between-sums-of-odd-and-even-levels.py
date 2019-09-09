"""
https://www.geeksforgeeks.org/difference-between-sums-of-odd-and-even-levels/
Given a a Binary Tree, find the difference between the sum of nodes at odd level and the sum of nodes at even level. Consider root as level 1, left and right children of root as level 2 and so on.
For example, in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18. And sum of nodes at even level is (2 + 6 + 3 + 7 + 9) which is 27. The output for following tree should be 18 – 27 which is -9.
      5
    /   \
   2     6
 /  \     \
1    4     8
    /     / \
   3     7   9
"""


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def differenceSum(self, n):
        """
        bfs和dfs都可以实现
        bfs:由于binary tree不是满二叉树或者完全二叉树,所以用bfs方法时,需要补全缺失的节点或记录缺失的节点
        dfs:通过在dfs过程中记录level进行sum计算即可,使用前序遍历,中序遍历都可以
        :param n:
        :return:
        """
        # self.odd_sum = 0
        # self.even_sum = 0
        # self.dfs(n)
        # return self.odd_sum - self.even_sum

        # return self.bfs(n)

        return self.dfs_2(n)

    def bfs(self, n):
        """
        用两个列表分别记录当前level节点和下一个level节点,通过travelsal
        :param n:
        :return:
        """
        odd_sum = 0
        even_sum = 0
        level = 1
        list1 = [n]
        list2 = []
        while list1 or list2:
            for l in list1:
                if l.left:
                    list2.append(l.left)
                if l.right:
                    list2.append(l.right)
                if level % 2 == 0:
                    even_sum += l.val
                else:
                    odd_sum += l.val
            list1, list2 = list2, []
            level += 1
        return odd_sum - even_sum

    def dfs(self, n, level=1):
        """
        深度优先
        :param n:
        :param level:
        :return:
        """
        if n is None or level <= 0:
            return
        if level % 2 == 0:
            self.even_sum += n.val
        else:
            self.odd_sum += n.val
        # 递归sum
        if n.left:
            self.dfs(n.left, level + 1)
        if n.right:
            self.dfs(n.right, level + 1)

    def dfs_2(self, n):
        """
        深度优先,一个巧妙的方法,代码及其简洁.
        推导公式为:
        o1+o3+o5-e2-e4-d6
        =o1-e2+o3-e4+o5-e6
        =o1-(e2-(o3-(e4-(o5-e6))))
        """
        if n is None:
            return 0
        return n.val - (self.dfs_2(n.left) + self.dfs_2(n.right))


if __name__ == '__main__':
    """
    Let us create Binary Tree shown
    in above example """
    root = Node(5)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.right.right = Node(8)
    root.right.right.right = Node(9)
    root.right.right.left = Node(7)

    result = Solution().differenceSum(root)
    print("Diffence between sums is", result)
