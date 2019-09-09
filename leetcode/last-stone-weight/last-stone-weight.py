import bisect
import heapq


class Solution:
    """
    https://leetcode.com/problems/last-stone-weight/
    1046. Last Stone Weight
    Easy
    ----------------------------
    We have a collection of rocks, each rock has a positive integer weight.
    Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
    At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

    Example 1:
    Input: [2,7,4,1,8,1]
    Output: 1
    Explanation:
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

    Note:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
    ----------------------------
    similar problems:
    https://leetcode.com/discuss/interview-question/340303/amazon-online-assessment-min-time-to-merge-files
    """

    def lastStoneWeight(self, stones):
        return self.lastStoneWeight_heap(stones)

    def lastStoneWeight_hashtable(self, stones):
        """
        1.使用hashtable记录stones,其中key:weight,value:times(该重量出现的次数)
        2.在生成hashtable的过程中找到max_weight
        3.从max_weight开始每次递减1开始循环,显示相同weight的stone进行smash,然后与weight-1(如果存在的话)进行smash
        4.直到hashtable只有一个元素,并且value=1或0时结束,key就是所求
        --------
        这个方法有些复杂,应该存在非常简单和巧妙的方法
        :param stones:
        :return:
        """
        if stones is None or len(stones) == 0:
            return 0

        hashtable = {}
        max_weight = 0
        for s in stones:
            max_weight = max(max_weight, s)
            if s in hashtable:
                hashtable[s] += 1
            else:
                hashtable[s] = 1
        while True:
            if max_weight <= 0:
                break

            if hashtable[max_weight] > 1:  # 相同重量石头smash
                hashtable[max_weight] %= 2
            elif hashtable[max_weight] == 0:  # 重量为0时跳过
                max_weight = self.findNextMaxWeight(hashtable, max_weight)
            else:  # weight重量只有一块儿时
                second_max_weight = self.findNextMaxWeight(hashtable, max_weight)
                if second_max_weight == 0:
                    break
                tmp_weight = max_weight - second_max_weight
                hashtable[max_weight] -= 1
                hashtable[second_max_weight] -= 1
                if tmp_weight in hashtable:
                    hashtable[tmp_weight] += 1
                else:
                    hashtable[tmp_weight] = 1
                # 取较大值作为新的max_weight
                max_weight = max(second_max_weight, tmp_weight)
        return max_weight

    def findNextMaxWeight(self, hashtable, max_weight):
        """
        获取基于max_weight之下第二大的重量
        :param hashtable:
        :param max_weight:
        :return:
        """
        tmp_weight = max_weight - 1
        while tmp_weight > 0:
            if tmp_weight in hashtable and hashtable[tmp_weight] > 0:
                break
            else:
                tmp_weight -= 1
        return tmp_weight

    def lastStoneWeight_brute(self, stones):
        """
        暴力法:1.排序;2.找最大的两个进行smash;3.重复执行1,直到只剩下一个元素
        时间复杂度O(N*N)
        参考思路:https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaPython-O(nlogn)
        也可以使用PriorityQueue进行计算.python和java都有PriorityQueue这样的封装好的数据结构.
        :param stones:

        :return:
        """
        stones = sorted(stones)
        for i in range(len(stones) - 1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))
        return stones.pop()

    def lastStoneWeight_heap(self, A):
        # 很巧妙,通过负号把大变小,小变大,以满足小顶堆按照大顶堆保存的需要
        pq = [-x for x in A]
        heapq.heapify(pq)
        for i in range(len(A) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]


def main():
    a = [2, 2, 3, 2]
    ret = Solution().lastStoneWeight(a)
    print(ret)
    print("-----------------")

    a = [2, 7, 4, 1, 8, 1]
    ret = Solution().lastStoneWeight(a)
    print(ret)
    print("-----------------")

    a = [1, 1, 1, 1, 1, 99]
    ret = Solution().lastStoneWeight(a)
    print(ret)
    print("-----------------")


if __name__ == "__main__":
    main()
