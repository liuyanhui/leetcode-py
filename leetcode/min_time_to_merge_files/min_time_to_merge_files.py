"""
这不是leetcode题库中的题,是leetcode上发表的Amazon  Online Assessment 的题,连接如下:
https://leetcode.com/discuss/interview-question/340303/amazon-online-assessment-min-time-to-merge-files
---------------
Example 1:
Input: numOfSubFiles = 4, files = [20, 4, 8, 2]
Output: 54

Example 2:
Input: numOfSubFiles = 6, files = [1, 2, 5, 10, 35, 89]
Output: 224

Example 3:
Input: numOfSubFiles = 4, files = [2, 2, 3, 3]
Output: 20

int minimumTime(int numOfSubFiles, List<Integer> files) {
}

Similar problems:
https://leetcode.com/problems/last-stone-weight
"""
import heapq
import bisect


class Solution:
    def minimumTime(self, n, files):
        return self.minimumTime_bisect(n,files)

    def minimumTime_heapq(self, n, files):
        if files is None or len(files) <= 0:
            return 0
        heapq.heapify(files)
        ret = 0
        while len(files) > 1:
            tmp = heapq.heappop(files) + heapq.heappop(files)
            ret += tmp
            heapq.heappush(files, tmp)
        return ret

    def minimumTime_bisect(self, n, files):
        files.sort()
        ret = 0
        while len(files)>1:
            tmp = files.pop(0)+ files.pop(0)
            ret += tmp
            bisect.insort(files,tmp)
        return ret

def main():
    n = 4
    files = [20, 4, 8, 2]
    ret = Solution().minimumTime(n, files)
    print(ret)
    print("-----------")

    files = [1, 2, 5, 10, 35, 89]
    ret = Solution().minimumTime(n, files)
    print(ret)
    print("-----------")


if __name__ == "__main__":
    main()
