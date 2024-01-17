"""
61. Rotate List
Medium
------------------------
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""
from leetcode.util.list_util import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        return self.rotateRight_1(head, k)

    def rotateRight_1(self, head: ListNode, k: int) -> ListNode:
        """
        Round 3
        Score[4] Lower is harder

        Thinking：
        1. 双指针法。先定位到第n-k个节点（从0开始），然后把[n-k:]整个加到链表头部。

        验证通过:
        Runtime 33 ms Beats 94.35%
        Memory 17.42 MB Beats 6.83%

        Args:
            head:
            k:

        Returns:

        """
        if not head:
            return head
        # 先计算链表的长度
        len_node = 0
        cur = head
        while cur:
            len_node += 1
            cur = cur.next
        # 确保k小于链表的长度
        k %= len_node

        first = second = ListNode(0, head)
        # 先定位到需要断开的节点
        while first.next:
            if k <= 0:
                second = second.next
            first = first.next
            k -= 1

        # 重新构建链表
        first.next = head
        ret = second.next
        second.next = None
        return ret


def do_func(arr: list, k: int, expect: list):
    head = list_to_listnode(arr)
    ret = Solution().rotateRight(head, k)
    ret_list = listnode_to_list(ret)
    print(ret_list)
    print(ret_list == expect)
    print("---------------------")


def main():
    do_func([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
    do_func([0, 1, 2], 4, [2, 0, 1])
    do_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16], 200,
            [12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
    do_func([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5])
    do_func([], 10, [])


if __name__ == "__main__":
    main()
