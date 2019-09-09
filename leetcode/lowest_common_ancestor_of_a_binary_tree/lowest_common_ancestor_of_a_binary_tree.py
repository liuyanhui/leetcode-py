class TreeNode:
    def __init__(self, x=-1):
        self.val = x
        self.left = None
        self.right = None

    def generate_tree(self, node_list, index):
        """根据list生成tree"""
        if index >= len(node_list):
            return None

        if node_list[index] > 0:
            node = TreeNode(node_list[index])
        else:
            return None

        if 2 * index + 1 < len(node_list):
            node.left = self.generate_tree(node_list, 2 * index + 1)
        if 2 * index + 2 < len(node_list):
            node.right = self.generate_tree(node_list, 2 * index + 2)

        return node


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        if not p or not q:
            return
        if p == q:
            return p

        # DFS 找到节点,保存路径
        p_path = []
        q_path = []
        self.dfs_find(root, p, p_path)
        self.dfs_find(root, q, q_path)
        print(len(p_path))
        print(len(q_path))

        # 从头同时遍历两个路径,直到第一个不同的路径节点,返回该节点的上个节点
        last=TreeNode()
        min_len = min(len(p_path),len(q_path))
        for i in range(min_len):
            if p_path[i] == q_path[i]:
                last = q_path[i]
            else:
                break

        print(last)
        print(last.val)
        return last

    def dfs_find(self, node, target, path):
        path.append(node)
        if node.val == target.val:
            return True

        finded=False
        if node.left:
            finded = self.dfs_find(node.left, target, path)
            if finded:
                return True

        if node.right and not finded:
            finded = self.dfs_find(node.right, target, path)
            if finded:
                return True

        path.remove(node)


def main():
    node_list = [3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4]
    node_list = [2,-1,2]
    root = TreeNode().generate_tree(node_list, 0)

    p = TreeNode(5)
    q = TreeNode(1)

    Solution().lowestCommonAncestor(root, p, q)


if __name__ == "__main__":
    main()
