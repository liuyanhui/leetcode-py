"""
83. Remove Duplicates from Sorted List
Easy
-------------------------------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

from leetcode.util.list_util import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteDuplicates_1(head)

    def deleteDuplicates_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Round 3
        Score[5] Lower is harder

        验证通过：

        """
        tail = head
        while tail and tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next

        return head


def do_func(arr: list, expect: list):
    head = list_to_listnode(arr)
    ret = Solution().deleteDuplicates(head)
    ret_list = listnode_to_list(ret)
    print(ret_list)
    print(ret_list == expect)
    assert ret_list == expect
    print("---------------------")


def main():
    do_func([1, 1, 2], [1, 2])
    do_func([1, 1, 2, 3, 3], [1, 2, 3])
    do_func([1, 2, 3], [1, 2, 3])
    do_func([1, 1, 1, 1, 1], [1])
    do_func([1, 1, 1, 2, 3, 3, 3, 3], [1, 2, 3])
    do_func([], [])

    print('----Done----')


if __name__ == "__main__":
    main()
