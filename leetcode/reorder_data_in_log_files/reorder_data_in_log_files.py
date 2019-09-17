"""
https://leetcode.com/problems/reorder-data-in-log-files/
937. Reorder Data in Log Files
Easy
--------------------------
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:
0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""


class Solution:
    def reorderLogFiles(self, logs):
        return self.reorderLogFiles_3(logs)

    def reorderLogFiles_1(self, logs):
        if logs is None or len(logs) == 0:
            return []
        ret = []
        letter_logs_content = []
        letter_logs_dict = {}
        digit_logs = []
        # 分拣letter-logs和digit-logs
        for log_str in logs:
            log_arr = log_str.split(' ', 1)
            if log_arr[1][0].isdigit():
                digit_logs.append(log_str)
            else:
                letter_logs_content.append(log_arr[1])
                letter_logs_dict.setdefault(log_arr[1], [])
                letter_logs_dict[log_arr[1]].append(log_arr[0])
        # letter-logs根据第一段内容排序
        letter_logs_content.sort()
        for l in letter_logs_content:
            ret.append(letter_logs_dict[l].pop() + " " + l)
        # 附加digit-logs
        return ret + digit_logs

    def reorderLogFiles_2(self, logs):
        """
        https://leetcode.com/problems/reorder-data-in-log-files/discuss/198197/simple-Python3-solution-beats-99
        这是Discuss区的代码,非常简洁,python style的代码
        :param logs:
        :return:
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split()[1])  # when suffix is tie, sort by identifier
        letters.sort(key=lambda x: x.split()[1:])  # sort by suffix

        result = letters + digits  # put digit logs after letter logs
        return result

    def reorderLogFiles_3(self, logs):
        """
        https://leetcode.com/problems/reorder-data-in-log-files/solution/
        Solution区的代码
        :param logs:
        :return:
        """
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)


def main():
    logs = []
    ret = Solution().reorderLogFiles(logs)
    print(ret)
    print("-----------------------")

    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    ret = Solution().reorderLogFiles(logs)
    print(ret)
    print("-----------------------")

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
    ret = Solution().reorderLogFiles(logs)
    print(ret)
    print("-----------------------")


if __name__ == '__main__':
    main()
