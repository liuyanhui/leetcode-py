class Solution:
    def addTwoNumbers(self, l1, l2):
        """https://leetcode.com/problems/add-two-numbers/"""
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        ret = cur = ListNode()
        carry = 0
        while l1 and l2:
            cur.next = ListNode()
            value = l1.val + l2.val + carry
            carry = value // 10
            cur.next.val = value % 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            cur.next = ListNode()
            value = l1.val + carry
            cur.next.val = value % 10
            carry = value // 10
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = ListNode()
            value = l2.val + carry
            cur.next.val = value % 10
            carry = value // 10
            l2 = l2.next
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(1)

        print(ret)
        return ret.next

    def addTwoNumbers2(self, l1, l2):
        """https://leetcode.com/problems/add-two-numbers/"""
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        ret = cur = ListNode()
        carry = 0
        while l1 or l2:
            l1_val = l2_val = 0
            cur.next = ListNode()
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            value = l1_val + l2_val + carry
            carry = value // 10
            cur.next.val = value % 10
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(1)

        print(ret)
        return ret.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


def main():
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    #
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    l1 = ListNode(9)
    l1.next = ListNode(8)

    l2 = ListNode(1)

    Solution().addTwoNumbers2(l1, l2)

    return


if __name__ == "__main__":
    main()
