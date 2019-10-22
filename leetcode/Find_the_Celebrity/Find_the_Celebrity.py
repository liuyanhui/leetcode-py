"""
题目有多个来源:
1.https://www.geeksforgeeks.org/the-celebrity-problem/
2.leercode 227 Medium .premium problem.
-----------------
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b)which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.

Note:
The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.
"""
import collections


class Solution:
    """
    审题:
    1.系统提供一个knows(a,b)方法
    2.需要实现findCelebrity(n)方法
    3.不允许知道party中的关系图,所以不会提供gragh,只能通过knows()获取
    4.人通过编号确定,编号范围是0~n-1
    """
    __gragh = []

    def __init__(self, gragh):
        self.__gragh = gragh

    def __knows(self, a, b):
        # if a == b:
        #     return False
        return self.__gragh[a][b] == 1

    def findCelebrity(self, n):
        return self.findCelebrity_2(n)

    def findCelebrity_1(self, n):
        """
        思路:
        1.if i know someone 排除i,即不必再调用knows(x,i).(记录在已经排除的缓存列表中)
        2.保存记录每个i的celebrity指数
        --------------
        时间复杂度O(n*n)
        空间复杂度O(n)
        :param n:
        :return:
        """
        if n <= 0:
            return -1
        include_dict = collections.defaultdict(int)  # 未被排除的人和celebrity指数
        exclude_dict = set()  # 被排除的人
        for i in range(n):
            for j in range(n):
                if j in exclude_dict:
                    continue
                if i != j and self.__knows(i, j):
                    exclude_dict.add(i)
                    include_dict[i] = -1
                    include_dict[j] += 1

        for i in include_dict.keys():
            if include_dict[i] == n - 1:
                return i
        return -1

    def findCelebrity_2(self, n):
        """
        参考思路:
        https://www.geeksforgeeks.org/the-celebrity-problem/
        https://www.jianshu.com/p/563900327415
        https://www.cnblogs.com/easonliu/p/4785253.html
        https://www.cnblogs.com/grandyang/p/5310649.html
        很神奇的思路,佩服得很.
        时间复杂度O(n)
        空间复杂度O(1)
        :param n:
        :return:
        """
        candidate = 0
        # 初次筛选
        # candidate后面index肯定不会是celebrity, 为什么呢？ 因为有人不认识他们, 违背了celebrity的条件；
        # candidate前面的index也不会是celebrity，因为他们knows somebody才会有可能被update掉，也违背了celebrity的条件.
        for i in range(n):
            if self.__knows(candidate, i):
                candidate = i
        # 第二次确认candidate是否celerity
        for i in range(n):
            if candidate == i:
                continue
            if self.__knows(candidate, i) or not self.__knows(i, candidate):
                return -1
        return candidate


def main():
    gragh = [[1, 1, 0],
             [0, 1, 0],
             [1, 1, 1]]
    s = Solution(gragh)
    ret = s.findCelebrity(3)
    print(ret)
    print("---------------")

    gragh = [[1, 0, 1],
             [1, 1, 0],
             [0, 1, 1]]
    s = Solution(gragh)
    ret = s.findCelebrity(3)
    print(ret)
    print("---------------")

    gragh = [[1, 0, 1, 0],
             [1, 1, 0, 0],
             [0, 1, 1, 0],
             [1, 1, 1, 1]]
    s = Solution(gragh)
    ret = s.findCelebrity(4)
    print(ret)
    print("---------------")

    gragh = [[1, 0, 1, 0],
             [1, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 1, 1, 1]]
    s = Solution(gragh)
    ret = s.findCelebrity(4)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
