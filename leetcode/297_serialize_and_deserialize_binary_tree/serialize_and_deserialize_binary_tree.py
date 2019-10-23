"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
297. Serialize and Deserialize Binary Tree
Hard
-------------------
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        return self.serialize_not_recursive(root)

    def deserialize(self, data):
        return self.deserialize_not_recursive(data)


    def serialize_2(self, root):
        return self.serialize_recursive(root)

    def deserialize_2(self, data):
        return self.deserialize_recursive(data)

    def serialize_not_recursive(self, root):
        """Encodes a tree to a single string.
        非递归办法
        采用leetcode的序列化格式
        1.使用广度优先遍历bfs把树转化为数组
        2.遍历数组,将数组转化为字符串

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ret = []
        root2List = [root]
        curIndex = 0
        while curIndex < len(root2List):
            if root2List[curIndex]:
                root2List.append(root2List[curIndex].left)
                root2List.append(root2List[curIndex].right)
            curIndex += 1

        for i in range(len(root2List)):
            if root2List[i]:
                ret.append(str(root2List[i].val))
                # 防止1,2,3,n,n,4,5,n,n,n,n这种情况的发生
                lastNormalIndex = i
            else:
                ret.append("null")

        return ",".join(ret[0:lastNormalIndex + 1])

    def deserialize_not_recursive(self, data):
        """Decodes your encoded data to tree.
        非递归办法
        采用逆BFS的思路
        1.使用队列和游标记录已处理和未处理的node
        2.由于采用的leetcode格式,需要考虑父节点是None时的特殊情况
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        data2List = data.split(",")
        ret = TreeNode(data2List[0])
        list2Tree = [ret]  # 保存node为list,需要记录遍历过程
        parentIndex = 0
        childIndex = 1
        while childIndex < len(data2List):
            # 跳过null节点
            while parentIndex < len(data2List) and list2Tree[parentIndex] is None:
                parentIndex += 1

            # 处理left子节点
            if data2List[childIndex] == 'null':
                node = None
            else:
                node = TreeNode(data2List[childIndex])
            list2Tree.append(node)
            list2Tree[parentIndex].left = node
            childIndex += 1

            # 处理right子节点
            if childIndex < len(data2List):
                if data2List[childIndex] == 'null':
                    node = None
                else:
                    node = TreeNode(data2List[childIndex])
                list2Tree.append(node)
                list2Tree[parentIndex].right = node
                childIndex += 1

            parentIndex += 1
        return ret

    def serialize_recursive(self, root):
        """
        递归办法,采用dfs思路
        :param root:
        :return:
        """
        if root is None:
            return ""

        def do_serialize_recursive(node):
            if node:
                ret.append(str(node.val))
                do_serialize_recursive(node.left)
                do_serialize_recursive(node.right)
            else:
                ret.append("null")

        ret = []
        do_serialize_recursive(root)
        return ",".join(ret)

    def deserialize_recursive(self, data):
        """
        递归办法,采用dfs思路
        :param data:
        :return:
        """
        if data is None or len(data) == 0:
            return None

        valList = data.split(",")

        def do_deserialize_recursive(valList):
            if valList is None or len(valList) == 0:
                return None
            if valList[0] == "null":
                valList.pop(0)
                return None
            else:
                n = TreeNode(valList[0])
                valList.pop(0)
                n.left = do_deserialize_recursive(valList)
                n.right = do_deserialize_recursive(valList)
                return n

        return do_deserialize_recursive(valList)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def main():
    print("===========思路1=============")
    rawStr = "1,2,3,null,null,4,5"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize(rawStr)
    s = coded.serialize(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    rawStr = "1,2,3,null,null,4,5,6"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize(rawStr)
    s = coded.serialize(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    rawStr = "1,2,3,null,null,4,5,6,null,null,null,7"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize(rawStr)
    s = coded.serialize(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    rawStr = "-1,0,1"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize(rawStr)
    s = coded.serialize(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    print("===========思路2=============")

    rawStr = "1,2,null,null,3,4,null,null,5,null,null"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize_2(rawStr)
    s = coded.serialize_2(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    rawStr = "1,2,null,null,3,4,6,null,null,null,5,null,null"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize_2(rawStr)
    s = coded.serialize_2(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")

    rawStr = "-1,0,1,null,null,null,null"
    print("rawStr=", rawStr)
    coded = Codec()
    root = coded.deserialize_2(rawStr)
    s = coded.serialize_2(root)
    print("s=", s)
    print("结果:", s == rawStr)
    print("---------------------")


if __name__ == "__main__":
    main()
