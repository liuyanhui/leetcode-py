"""
https://leetcode.com/problems/swap-nodes-in-pairs/
24. Swap Nodes in Pairs
Medium
-----------------------------------
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        return self.swapPairs_2(head)

    def swapPairs_1(self, head):
        final_h = t_h = ListNode(None)
        t_h.next = head
        while t_h and t_h.next and t_h.next.next:
            a, b, c = t_h.next, t_h.next.next, t_h.next.next.next
            t_h.next.next.next = a
            t_h.next.next = c
            t_h.next = b
            t_h = t_h.next.next
        return final_h.next

    def swapPairs_2(self, head):
        """
        简化代码
        :param head:
        :return:
        """
        final_h = t_h = ListNode(None)
        t_h.next = head
        while t_h and t_h.next and t_h.next.next:
            t_h.next.next.next, t_h.next.next, t_h.next = t_h.next, t_h.next.next.next, t_h.next.next
            t_h = t_h.next.next
        return final_h.next


def main():
    def generate_listnode(arr):
        tmp = head = ListNode(None)
        for val in arr:
            node = ListNode(val)
            tmp.next = node
            tmp = tmp.next
        return head.next

    a = [1, 2, 3, 4]
    list_node = generate_listnode(a)
    final_node = Solution().swapPairs(list_node)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    a = [1, 2, 3]
    list_node = generate_listnode(a)
    final_node = Solution().swapPairs(list_node)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    a = [1, 2]
    list_node = generate_listnode(a)
    final_node = Solution().swapPairs(list_node)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    a = [1]
    list_node = generate_listnode(a)
    final_node = Solution().swapPairs(list_node)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")


if __name__ == "__main__":
    main()
