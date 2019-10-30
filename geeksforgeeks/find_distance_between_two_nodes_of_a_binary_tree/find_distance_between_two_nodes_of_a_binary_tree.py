"""
https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
Find the distance between two keys in a binary tree, no parent pointers are given. Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.
"""
import leetcode.common_util.array_to_tree_util as array_to_tree


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Solution:
    def distance(self, root, data1, data2):
        return self.distance_1(root, data1, data2)

    def distance_1(self, root, data1, data2):
        """
        普通思路:
        1.dfs先序遍历从root到data,分别记录过程节点到两个list中
        2.对两个list进行计算得出distance
        ----------
        时间复杂度:O(N)
        :param root:
        :param data1:
        :param data2:
        :return:
        """
        if not root or not data1 or not data1:
            return 0
        list1, list2 = [], []

        def dfs(node, data, rs_list):
            if not node:
                return False
            rs_list.append(node.data)
            if node.data == data:
                return True
            return dfs(node.left, data, rs_list) or dfs(node.right, data, rs_list)

        dfs(root, data1, list1)
        dfs(root, data2, list2)
        index = 0
        while index < len(list1) and index < len(list2):
            if list1[index] == list2[index]:
                index += 1
            else:
                break
        return len(list1) - 1 + len(list2) - 1 - index


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.left.right = Node(5)
    root.right.left.right = Node(8)

    dist = Solution().distance(root, 4, 5)
    print("Distance between node {} & {}: {}".format(4, 5, dist))

    dist = Solution().distance(root, 4, 6)
    print("Distance between node {} & {}: {}".format(4, 6, dist))

    dist = Solution().distance(root, 3, 4)
    print("Distance between node {} & {}: {}".format(3, 4, dist))

    dist = Solution().distance(root, 2, 4)
    print("Distance between node {} & {}: {}".format(2, 4, dist))

    dist = Solution().distance(root, 8, 5)
    print("Distance between node {} & {}: {}".format(8, 5, dist))


if __name__ == "__main__":
    main()
