"""
https://leetcode.com/problems/find-k-closest-elements/
658. Find K Closest Elements
Medium
----------------------
Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers).
Please reload the code definition to get the latest changes.
"""


class Solution:
    def findClosestElements(self, arr, k, x):
        return self.findClosestElements_4(arr, k, x)

    def findClosestElements_1(self, arr, k, x):
        """
        滑动窗口思路
        1.如果x<=arr[0],return arr[0:k];如果x>=arr[-1],return arr[-4:]
        否则,
        2.找到arr中最近接x的元素,记为arr[i].注意:i可能是1个或者2个,当x不在arr中时可能存在i有两个情况.分别记为small_i,large_i
        2.1.大概思路:使用滑动窗口围绕i计算closest_value和sum().其中sum()的计算只需要减去上个sum的第一个元素,加上本次sum的最后一个元素即可.
        3.beg=max(0,small_i-k),end=min(len(arr),large_i+k).其中beg为所有窗口的开始下标,end为所有窗口的结束下标.所有窗口的计算范围为[beg,end]
        4.每次窗口计算结束时,取较小的closest_value,closest_value相等时去较小的sum对应的数组.
        ------
        优化:不需要计算small_i和large_i,直接使用滑动窗口遍历整个arr即可.
        ------
        验证通过,性能一般
        Runtime: 680 ms, faster than 5.20% of Python3 online submissions for Find K Closest Elements.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find K Closest Elements.
        :param arr:
        :param k:
        :param x:
        :return:
        """
        if k <= 0:
            return []
        if not arr and len(arr) == 0:
            return []
        if arr[0] >= x:
            return arr[0:k]
        if arr[-1] <= x:
            return arr[-k:]
        max_const = 999999999
        closest_x = max_const
        small_i, large_i = max_const, max_const
        # 找到small_i和large_i
        # tip:这一步是多余的,不需要计算small_i和large_i,直接使用滑动窗口遍历整个arr即可
        for m in range(len(arr)):
            if abs(arr[m] - x) < closest_x:
                closest_x = abs(arr[m] - x)
                large_i = small_i = m
            elif abs(arr[m] - x) == closest_x:
                # large_i = max(large_i, m)
                large_i = m
            else:
                break
        beg = max(0, small_i - k)
        end = min(len(arr), large_i + k)
        # 使用滑动窗口计算
        # 计算初始窗口
        last_sum = sum(arr[beg:beg + k])
        ret = arr[beg:beg + k]
        closest = sum([abs(arr[m] - x) for m in range(beg, beg + k)])
        # 跳过初始窗口
        for m in range(beg + 1, end - k + 1):
            # closest减去最先加入,加上将要加入的
            tmp_closest = closest - abs(arr[m - 1] - x) + abs(arr[m + k - 1] - x)
            if closest > tmp_closest:
                ret = arr[m:m + k]
                closest = tmp_closest
                last_sum = last_sum - arr[m] + arr[m + k - 1]
            elif closest == tmp_closest:
                tmp_sum = last_sum - arr[m] + arr[m + k - 1]
                if last_sum > tmp_sum:
                    ret = arr[m:m + k]
                    closest = tmp_closest
                    last_sum = tmp_sum

        return ret

    def findClosestElements_2(self, arr, k, x):
        """
        findClosestElements_2的代码简化版本,性能没有findClosestElements_1好,但是代码复杂度降低了.

        滑动窗口思路
        1.如果x<=arr[0],return arr[0:k];如果x>=arr[-1],return arr[-4:]
        否则,
        2.使用滑动窗口围绕i计算closest_value和sum().其中sum()的计算只需要减去上个sum的第一个元素,加上本次sum的最后一个元素即可.
        3.每次窗口计算结束时,取较小的closest_value,closest_value相等时去较小的sum对应的数组.
        ------
        验证通过,性能一般
        Runtime: 980 ms, faster than 5.20% of Python3 online submissions for Find K Closest Elements.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find K Closest Elements.
        :param arr:
        :param k:
        :param x:
        :return:
        """
        if k <= 0:
            return []
        if not arr and len(arr) == 0:
            return []
        if arr[0] >= x:
            return arr[0:k]
        if arr[-1] <= x:
            return arr[-k:]
        # 使用滑动窗口计算
        # 计算初始窗口
        last_sum = sum(arr[0: k])
        ret = arr[0: k]
        closest = sum([abs(arr[m] - x) for m in range(0, k)])
        # 跳过初始窗口
        for m in range(1, len(arr) - k + 1):
            # closest减去最先加入,加上将要加入的
            tmp_closest = closest - abs(arr[m - 1] - x) + abs(arr[m + k - 1] - x)
            if closest > tmp_closest:
                ret = arr[m:m + k]
                closest = tmp_closest
                last_sum = last_sum - arr[m] + arr[m + k - 1]
            elif closest == tmp_closest:
                tmp_sum = last_sum - arr[m] + arr[m + k - 1]
                if last_sum > tmp_sum:
                    ret = arr[m:m + k]
                    closest = tmp_closest
                    last_sum = tmp_sum
        return ret

    def findClosestElements_3(self, arr, k, x):
        """
        1.先找到arr中最接近x的数,记为arr[i]~arr[j].可能存在多个
        2.以i~j为中心向外扩张,如果abs(arr[i-1]-x)<=abs(arr[j+1]-x),那么i=i-1,否则j=j+1.注意:为了满足约束条件,必须先判断i后判断j
        3.循环步骤2,直到i+k=j
        -----
        验证失败,逻辑比较复杂,实现起来有难度
        :param arr:
        :param k:
        :param x:
        :return:
        """
        left, right = 0, len(arr) - 1
        # 二分查找获取最接近x的数
        # tip:这里有问题,这段代码并没有正确的得到最接近x的数
        while left < right:
            mid = (left + right) // 2
            if x > arr[mid]:
                left = mid + 1
            elif x < arr[mid]:
                right = mid - 1
            else:
                left = right = mid

        right = left = min(left, right)

        while min(right, len(arr)) - max(0, left) < k:
            if left < 0:
                right += 1
                continue
            elif right >= len(arr):
                left -= 1
                continue

            if abs(x - arr[left]) <= abs(x - arr[right]):
                left -= 1
            else:
                right += 1
        left = max(0, left)
        right = min(right, len(arr))

        return arr[left:right]

    def findClosestElements_4(self, arr, k, x):
        """
        滑动窗口+二分查找.这个思路可以用来优化findClosestElements_2
        参考思路:
        https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
        关键在于:
        If x - A[mid] > A[mid + k] - x,it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
        and we have mid smaller than the right i.
        So assign left = mid + 1.
        类似于滑动窗口,把首部(或者尾部)的数去掉,换成尾部+1(或者头部-1)的数,然后进行比较.
        不考虑正负的情况下,如果a+b+c+d-x>b+c+d+e-x,那么b/c/d/e是更优解;否则a/b/c/d是更优解.
        ----------
        验证通过,性能很好
        Runtime: 312 ms, faster than 85.33% of Python3 online submissions for Find K Closest Elements.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find K Closest Elements.
        :param arr:
        :param k:
        :param x:
        :return:
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # if x - arr[mid] > arr[mid + k] - x:#这个才是最正确的
            if abs(x - arr[mid]) > abs(arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid  # 这也比较重要,排除最右的数.不是mid-1
        return arr[left:left + k]


def main():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    ret = Solution().findClosestElements(arr, k, x)
    print(ret)
    print(ret == [1, 2, 3, 4])
    print("--------------------")

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    ret = Solution().findClosestElements(arr, k, x)
    print(ret)
    print(ret == [1, 2, 3, 4])
    print("--------------------")

    arr = [1, 2, 3, 4, 5, 500, 600, 602, 603, 700]
    k = 4
    x = 495
    ret = Solution().findClosestElements(arr, k, x)
    print(ret)
    print(ret == [500, 600, 602, 603])
    print("--------------------")

    arr = [1, 2, 3, 4, 5, 500, 600, 602, 603, 700]
    k = 4
    x = 600
    ret = Solution().findClosestElements(arr, k, x)
    print(ret)
    print(ret == [500, 600, 602, 603])
    print("--------------------")

    arr = [1, 2, 3, 4, 5, 500, 600, 602, 603, 700]
    k = 4
    x = 690
    ret = Solution().findClosestElements(arr, k, x)
    print(ret)
    print(ret == [600, 602, 603, 700])
    print("--------------------")


if __name__ == "__main__":
    main()
