"""
82. Remove Duplicates from Sorted List II
Medium
-------------------------------
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

from util.list_util import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteDuplicates_2(head)

    def deleteDuplicates_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        review
        """
        if not head:
            return head

        def helper(node: ListNode, prev: int) -> ListNode:
            if not node:
                return node
            if node.val == prev:
                return helper(node.next, prev)
            if node.next and node.val == node.next.val:
                return helper(node.next, node.val)
            node.next = helper(node.next, node.val)
            return node

        return helper(head, 9999)

    def deleteDuplicates_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：review
        1. 分段+分步思路。
        分段：分为已计算部分和待计算部分。
        分步：先标记，再移除。
        2. 递归思路。
        helper(head:ListNode,val:int)

        验证通过：
        Runtime 34 ms Beats 88.63%
        Memory 16.62 MB Beats 22.38%
        """
        ret = ListNode()
        tail = ret
        sign = False
        while head:
            # 先标记
            if head.next and head.val == head.next.val:
                sign = True
            else:
                if sign:  # 再移除重复节点
                    # do nothing
                    pass
                else:  # 正常处理非重复节点
                    tail.next = head
                    tail = head
                # 重置标记
                sign = False
            head = head.next
        # 边界处理
        tail.next = head
        return ret.next


def do_func(arr: list, expect: list):
    head = list_to_listnode(arr)
    ret = Solution().deleteDuplicates(head)
    ret_list = listnode_to_list(ret)
    print(ret_list)
    print(ret_list == expect)
    assert ret_list == expect
    print("---------------------")


def main():
    do_func([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
    do_func([1, 1, 1, 2, 3], [2, 3])
    do_func([1, 2, 3], [1, 2, 3])
    do_func([1, 1, 1, 1, 1], [])
    do_func([1, 1, 1, 2, 3, 3, 3, 3], [2])

    print('----Done----')


if __name__ == "__main__":
    main()
