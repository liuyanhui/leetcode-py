class Solution:
    def findMinMoves(self, machines):
        """
        别人的方案,通过所有用例
        :param machines:
        :return:
        """
        if machines is None:
            return -1

        ret = 0
        sum_dress = sum(machines)
        # for mac in machines:
        #     sum_dress = sum_dress + mac

        if sum_dress % len(machines) != 0:
            return -1
        avg = int(sum_dress / len(machines))

        delta = []
        for i in range(len(machines)):
            delta.append(machines[i] - avg)
        print("delta(machines[i]-avg)=", delta)

        cur = 0
        for i in range(len(machines)):
            cur += machines[i] - avg
            ret = max(machines[i] - avg, ret, abs(cur))
            print("(machines[i]-avg)=", machines[i] - avg, ";ret=", ret, "cur=", cur)

        return ret

    def findMinMoves_2(self, machines):
        """
        自己的方案，未通过全部用例，原因:Time Limit Exceeded
        """
        if machines is None:
            return 0
        sum_dress = sum(machines)
        if sum_dress % len(machines) == 0:
            avg = sum_dress // len(machines)
        else:
            return -1
        max_ret = 0
        last_left_sum = 0
        last_right_sum = 0
        for i in range(len(machines)):
            left_sum = 0
            right_sum = 0
            j = 0
            while j < i:
                left_sum += machines[j] - avg
                j += 1
            j = i + 1
            while j < len(machines):
                right_sum += machines[j] - avg
                j += 1
            # print("-----i=",i,"-----")
            # print("max=%d,left_sum=%d,right_sum=%d"%(max_ret,left_sum,right_sum))
            if machines[i] == avg:
                max_ret = max(max_ret, abs(left_sum))
            elif left_sum < 0 and right_sum < 0:
                max_ret = max(max_ret, abs(machines[i] - avg))
            elif left_sum > 0 and right_sum > 0:
                max_ret = max(max_ret, left_sum, right_sum)
            else:
                max_ret = max(max_ret, abs(left_sum + machines[i] - avg), abs(right_sum + machines[i] - avg))
        return max_ret

    def findMinMoves_3(self, machines):
        """
        自己的改进后的方案， pass
        思路：某台washing machine的左右的衣服总和left_sum，右边的衣服总和right_sum，当前节点拥有的衣服self，这三个数作为计算依据。
        想要达到目标，衣服必须要经过当前节点中转，所以经过当前节点的衣服的最大值就是所需的答案。
        """
        if machines is None:
            return 0
        sum_dress = sum(machines)
        if sum_dress % len(machines) == 0:
            avg = sum_dress // len(machines)
        else:
            return -1
        max_ret = 0
        left_sum = 0
        right_sum = sum_dress - avg * len(machines)  # TODO 改进点 这里是0,因为left_sum+right_sum+(machines[i]-avg)=0
        for i in range(len(machines)):
            if i > 0:
                left_sum += machines[i - 1] - avg
            if i < len(machines):
                right_sum -= machines[i] - avg
            # print("-----i=",i,"-----")
            # print("max=%d,left_sum=%d,right_sum=%d"%(max_ret,left_sum,right_sum))
            if machines[i] == avg:  # todo 改进点 这里和最后一个判断可以合并
                max_ret = max(max_ret, abs(left_sum))
            elif left_sum < 0 and right_sum < 0:
                max_ret = max(max_ret, abs(machines[i] - avg))
            elif left_sum > 0 and right_sum > 0:
                max_ret = max(max_ret, left_sum, right_sum)
            else:
                max_ret = max(max_ret, abs(left_sum + machines[i] - avg), abs(right_sum + machines[i] - avg))
        return max_ret



def main():
    # ret = Solution().findMinMoves([9, 1, 8, 8, 9])
    ret = Solution().findMinMoves([0, 0, 11, 5])
    print("ret=", ret)


if __name__ == '__main__':
    main()
