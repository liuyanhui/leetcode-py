"""
https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/
Swap Kth node from beginning with Kth node from end in a Linked List
Given a singly linked list, swap kth node from beginning with kth node from end. Swapping of data is not allowed, only pointers should be changed. This requirement may be logical in many situations where the linked list data part is huge (For example student details line Name, RollNo, Address, ..etc). The pointers are always fixed (4 bytes for most of the compilers).
"""


class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class Solution:
    def swap_kth(self, node, k):
        """
        咋一看很简单,其实有坑.如下所示:
        The problem seems simple at first look, but it has many interesting cases.
        Let X be the kth node from beginning and Y be the kth node from end. Following are the interesting cases that must be handled.
        1) Y is next to X
        2) X is next to Y
        3) X and Y are same
        4) X and Y don’t exist (k is more than number of nodes in linked list)
        尤其是1和2隐藏的很深
        :param head:
        :return:
        """
        if not node or k <= 0:
            return node
        head = Node()
        head.next = node
        step = 0
        cur_node = head
        swap_b, swap_e = head, head

        while cur_node.next:
            if step + 1 == k:
                swap_b = cur_node
            cur_node = cur_node.next
            if step + 1 > k:
                swap_e = swap_e.next
            step += 1

        # 判断是否超界
        if step < k:
            pass
        else:
            if swap_e == swap_b:
                pass
            elif swap_b.next == swap_e:
                # 特殊情况1
                # 另,对于引用传递,连续赋值语句需要注意变量的顺序
                swap_b.next, swap_b.next.next, swap_e.next = swap_e.next, swap_e, swap_e.next.next
                # 如果替换上面的代码就会报错的
                # swap_b.next.next, swap_b.next, swap_e.next = swap_e.next.next, swap_e.next, swap_e
            elif swap_e.next == swap_b:
                # 特殊情况2
                swap_e.next, swap_e.next.next, swap_b.next = swap_b.next, swap_b, swap_b.next.next
            else:
                swap_b.next.next, swap_e.next.next, swap_b.next, swap_e.next \
                    = swap_e.next.next, swap_b.next.next, swap_e.next, swap_b.next
        return head.next


def main():
    def generate_node_list(n=0):
        head = Node()
        tmp = head
        for i in range(n):
            node = Node(i + 1)
            tmp.next = node
            tmp = tmp.next
        return head.next

    # node = generate_node_list(10)
    # final_node = Solution().swap_kth(node, 1)
    # ret = []
    # n = final_node
    # while n:
    #     ret.append(n.val)
    #     n = n.next
    # print(ret)
    # print("------------------------")
    #
    # node = generate_node_list(10)
    # final_node = Solution().swap_kth(node, 2)
    # ret = []
    # n = final_node
    # while n:
    #     ret.append(n.val)
    #     n = n.next
    # print(ret)
    # print("------------------------")

    node = generate_node_list(10)
    final_node = Solution().swap_kth(node, 5)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(10)
    final_node = Solution().swap_kth(node, 6)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(10)
    final_node = Solution().swap_kth(node, 9)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(10)
    final_node = Solution().swap_kth(node, 10)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(10)
    final_node = Solution().swap_kth(node, 11)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(5)
    final_node = Solution().swap_kth(node, 1)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")
    node = generate_node_list(5)
    final_node = Solution().swap_kth(node, 2)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")

    node = generate_node_list(5)
    final_node = Solution().swap_kth(node, 3)
    ret = []
    n = final_node
    while n:
        ret.append(n.val)
        n = n.next
    print(ret)
    print("------------------------")


if __name__ == "__main__":
    main()
