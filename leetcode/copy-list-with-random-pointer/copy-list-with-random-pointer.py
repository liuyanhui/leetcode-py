"""
https://leetcode.com/problems/copy-list-with-random-pointer/
138. Copy List with Random Pointer
Medium
---------------------
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        return self.copyRandomList_2(head)

    def copyRandomList_1(self, head):
        """
        使用hashtable建立old->new 的映射关系,遍历两次old列表即可.
        第一次遍历生成不包含random的列表和hash映射关系,第二次遍历完成random属性
        :param head:
        :return:
        """
        if head is None:
            return Node()
        new = Node(0, None, None)
        cur_old = head
        cur_new = new
        hashtable = {}
        while cur_old:
            cur_new.next = Node(cur_old.val, None, None)
            hashtable[cur_old] = cur_new.next
            cur_new = cur_new.next
            cur_old = cur_old.next

        cur_old = head
        cur_new = new
        while cur_old:
            if cur_old.random in hashtable:
                cur_new.next.random = hashtable[cur_old.random]
            cur_new = cur_new.next
            cur_old = cur_old.next

        return new.next

    def copyRandomList_2(self, head):
        """
        参考思路:
        https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
        思路很简单:
        1.假设原始链为:A->B->C->D
        2.修改后的中间链为:A->A'->B->B'->C->C'->D->D',同时指定random属性
        3.然后再移除原始节点
        :param head:
        :return:
        """
        if head is None:
            return None
        # 复制节点,并插入在源队列中A->A'
        cur_node = head
        while cur_node:
            tmp_node = Node(cur_node.val, cur_node.next, None)
            cur_node.next = tmp_node
            cur_node = cur_node.next.next
        # 重新指定random
        cur_node = head
        while cur_node:
            if cur_node.random:
                cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next
        # 剥离原来的节点和新复制的节点
        new = head.next
        cur_old = head
        cur_new = head.next
        while cur_old:
            # cur_old, cur_new = cur_old.next.next, cur_new.next.next
            cur_old.next = cur_old.next.next
            cur_old = cur_old.next
            if cur_new.next:
                cur_new.next = cur_new.next.next
                cur_new = cur_new.next
        return new


def main():
    # a = [
    #     [0, 1, 0],
    #     [0, 0, 1],
    #     [1, 1, 1],
    #     [0, 0, 0]
    # ]
    a = Node(1, None, None)
    b = Node(2, None, None)
    a.next = b
    a.random = b
    b.random = b
    Solution().copyRandomList(a)
    # print(a)
    print("-----------------")


if __name__ == "__main__":
    main()
