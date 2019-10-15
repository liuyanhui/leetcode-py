"""
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
Question: Design a Data Structure SpecialStack that supports all the stack operations like
push(), pop(), isEmpty(), isFull() and an additional operation getMin()
which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1).
To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays,
list, .. etc.
----------------------------------

"""


class special_stack:
    """
    参考文档:https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
    普通思路:
    1.不是用两个数组+一个hashtable的方式,这种方式太普通了.没有技术含量

    真正有用的思路如下:
    Push(int x) // inserts an element x to Special Stack
    1) push x to the first stack (the stack with actual elements)
    2) compare x with the top element of the second stack (the auxiliary stack). Let the top element be y.
    …..a) If x is smaller than y then push x to the auxiliary stack.
    …..b) If x is greater than y then push y to the auxiliary stack.

    int Pop() // removes an element from Special Stack and return the removed element
    1) pop the top element from the auxiliary stack.
    2) pop the top element from the actual stack and return it.

    The step 1 is necessary to make sure that the auxiliary stack is also updated for future operations.

    int getMin() // returns the minimum element from Special Stack
    1) Return the top element of auxiliary stack.

    再次基础上还有一个优化版本,思路如下:
    Space Optimized Version
    The above approach can be optimized. We can limit the number of elements in auxiliary stack.
    We can push only when the incoming element of main stack is smaller than or equal to top of auxiliary stack.
    Similarly during pop, if the pop off element equal to top of auxiliary stack,
    remove the top element of auxiliary stack. Following is modified implementation of push() and pop().

    具体实现略
    """

    def push(self, e):
        pass

    def pop(self):
        pass

    def get_min(self):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass
