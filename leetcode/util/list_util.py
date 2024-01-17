class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listnode(arr: list) -> ListNode:
    ret = ListNode()
    cur = ret
    for n in arr:
        cur.next = ListNode(n)
        cur = cur.next
    return ret.next


def listnode_to_list(node: ListNode) -> list:
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret
