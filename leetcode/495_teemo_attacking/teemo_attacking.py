"""
https://leetcode.com/problems/teemo-attacking/
495. Teemo Attacking
Medium
-------------------
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately.
This poisoned status will last 2 seconds until the end of time point 2.
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds.
So you finally need to output 4.

Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned.
This poisoned status will last 2 seconds until the end of time point 2.
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status.
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3.
So you finally need to output 3.

Note:
You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.
"""


class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        return self.findPoisonedDuration_1(timeSeries, duration)

    def findPoisonedDuration_1(self, timeSeries, duration):
        """
        分析:公有两种情况:每次攻击后中毒时间重叠和不重叠.
        设T(i)为每次攻击的时刻,那么T(i)+d就是中毒的持续时间
        定义变量,l和r,l表示中毒开始时刻,r表示中毒消失时刻
        1.如果T(i)+k>T(i+1),表示前后两次中毒持续时间重叠,那么r=T(i+1)+k
        2.如果Ti+k<Ti+1,表示不重叠,那么累加上一个耗时,并设置l=T(i),r=T(i)+k
        3.注意循环结束后还需要累加一次
        -----------------
        验证通过,性能不错,代码可以简化:
        Runtime: 264 ms, faster than 99.45% of Python3 online submissions for Teemo Attacking.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Teemo Attacking.
        :param timeSeries:
        :param duration:
        :return:
        """
        if not timeSeries or duration <= 0:
            return 0
        l, r = timeSeries[0], timeSeries[0] + duration - 1
        ret = 0
        for i in range(1, len(timeSeries)):
            if r >= timeSeries[i]:
                r = timeSeries[i] + duration - 1
            else:
                ret += r - l + 1
                l = timeSeries[i]
                r = l + duration - 1
        ret += r - l + 1
        return ret

    def findPoisonedDuration_2(self, timeSeries, duration):
        """
        代码简化
        参考思路:https://leetcode.com/problems/teemo-attacking/solution/
        :param timeSeries:
        :param duration:
        :return:
        """
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration


def main():
    timeSeries = [1, 4]
    duration = 2
    ret = Solution().findPoisonedDuration(timeSeries, duration)
    print(ret)
    print("--------------------")

    timeSeries = [1, 2]
    duration = 2
    ret = Solution().findPoisonedDuration(timeSeries, duration)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
