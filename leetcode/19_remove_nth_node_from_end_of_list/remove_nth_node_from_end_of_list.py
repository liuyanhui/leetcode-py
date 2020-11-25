"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
19. Remove Nth Node From End of List
Medium
----------------------
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        思路:快慢指针法,第一个指针出发n+1后,第二个出发.当第一个指针到达队尾时,第二指针指向的就是待删除的节点.
        Time Complexity:O(N)
        验证通过:
        Runtime: 32 ms, faster than 71.96% of Python3 online submissions for Remove Nth Node From End of List.
        Memory Usage: 14.4 MB, less than 8.18% of Python3 online submissions for Remove Nth Node From End of List.
        :param head:
        :param n:
        :return:
        """
        if not head:
            return None
        first = ListNode()
        first.next = head
        left = right = first
        i = 0
        while right.next:
            if i >= n:
                left = left.next
            i += 1
            right = right.next
        if left.next:
            left.next = left.next.next
        else:
            left.next = None
        return first.next


def main():
    head = [1, 2, 3, 4, 5]
    n = 2
    ret = Solution().removeNthFromEnd(head, n)
    print(ret)
    print(ret == [1, 2, 3, 5])
    print("---------------------")

    head = [1]
    n = 2
    ret = Solution().removeNthFromEnd(head, n)
    print(ret)
    print(ret == [])
    print("---------------------")

    head = [1, 2]
    n = 2
    ret = Solution().removeNthFromEnd(head, n)
    print(ret)
    print(ret == [1])
    print("---------------------")


if __name__ == "__main__":
    main()
