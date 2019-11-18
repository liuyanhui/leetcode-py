"""
https://leetcode.com/problems/largest-values-from-labels/
1090. Largest Values From Labels
Medium
-------------------
We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:
|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

Example 1:
Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.

Example 2:
Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.

Example 3:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.

Example 4:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.

Note:
1 <= values.length == labels.length <= 20000
0 <= values[i], labels[i] <= 20000
1 <= num_wanted, use_limit <= values.length
"""

import collections


class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        return self.largestValsFromLabels_2(values, labels, num_wanted, use_limit)

    def largestValsFromLabels_1(self, values, labels, num_wanted, use_limit):
        """
        理解题目是重点,这个题目描述的太难理解
        1.对values进行从大到小排序,对应的labels也需要根据values的排序结果进行变化
        2.从最大的values开始获取数字并计算,计算过程需要同时考虑num_wanted和use_limit的约束
        3.用一个dict缓存每个label出现的次数,用来针对use_limit约束;用一个int记录已经出现的数字的数量,用来针对num_wanted约束
        -------------------
        验证通过,性能不错:
        Runtime: 140 ms, faster than 98.53% of Python3 online submissions for Largest Values From Labels.
        Memory Usage: 17.7 MB, less than 100.00% of Python3 online submissions for Largest Values From Labels.
        :param values:
        :param labels:
        :param num_wanted:
        :param use_limit:
        :return:
        """
        if not values or not labels or num_wanted <= 0 or use_limit <= 0:
            return 0
        if len(values) != len(labels):
            return 0
        ret = 0
        num_appeated = 0
        appeared_lables_dict = collections.defaultdict(int)  # 记录value已经出现的次数,key是label,value是label对应的value已经出现的次数
        zip_list = list(zip(values, labels))
        zip_list.sort(reverse=True)  # 基于value倒序排序
        for v_l in zip_list:
            if num_appeated >= num_wanted:
                break
            # tmp_v = v_l[0]
            # tmp_l = v_l[1]
            # 上面被注释掉的语句也可以像下面这样写
            tmp_v, tmp_l = v_l
            if appeared_lables_dict[tmp_l] >= use_limit:
                continue
            ret += tmp_v
            appeared_lables_dict[tmp_l] += 1
            num_appeated += 1

        return ret

    def largestValsFromLabels_2(self, values, labels, num_wanted, use_limit):
        """
        largestValsFromLabels_1()代码简化版
        :param values:
        :param labels:
        :param num_wanted:
        :param use_limit:
        :return:
        """
        if not values or not labels or num_wanted <= 0 or use_limit <= 0:
            return 0
        if len(values) != len(labels):
            return 0
        ret = 0
        num_appeated = 0
        appeared_lables_dict = collections.defaultdict(int)  # 记录value已经出现的次数,key是label,value是label对应的value已经出现的次数
        for tmp_v, tmp_l in sorted(zip(values, labels), reverse=True):
            if num_appeated >= num_wanted:
                break
            if appeared_lables_dict[tmp_l] >= use_limit:
                continue
            ret += tmp_v
            appeared_lables_dict[tmp_l] += 1
            num_appeated += 1

        return ret


def main():
    values = [5, 4, 3, 2, 1]
    labels = [1, 1, 2, 2, 3]
    num_wanted = 3
    use_limit = 1
    ret = Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
    print(ret)
    print("--------------------")

    values = [5, 4, 3, 2, 1]
    labels = [1, 3, 3, 3, 2]
    num_wanted = 3
    use_limit = 2
    ret = Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
    print(ret)
    print("--------------------")

    values = [9, 8, 8, 7, 6]
    labels = [0, 0, 0, 1, 1]
    num_wanted = 3
    use_limit = 1
    ret = Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
    print(ret)
    print("--------------------")

    values = [9, 8, 8, 7, 6]
    labels = [0, 0, 0, 1, 1]
    num_wanted = 3
    use_limit = 2
    ret = Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
    print(ret)
    print("--------------------")

    values = [1, 2, 8, 7, 6]
    labels = [0, 1, 0, 1, 0]
    num_wanted = 3
    use_limit = 2
    ret = Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
