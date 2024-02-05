"""
68. Text Justification
Hard
-------------------------
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""


class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        return self.fullJustify_1(words, maxWidth)

    def fullJustify_1(self, words: list, maxWidth: int) -> list:
        """
        Round 3
        Score[2] Lower is harder

        review 复杂问题分解为简单问题,各个击破

        Thinking：
        1. 分步法
        1.1. 先计算每行能放几个word，并收集words
        1.1.1. 遍历words 为 word[i]
        1.1.2. 累加len(words[i])+1，直到大于maxWidth，作为每行可以放置的内容
        1.1.3. 计算下一行
        1.2. 按行组装words，补充空格。
        1.2.1. 计算word之间空格数量，最后一个单词不需要参加计算。
        假设m个单词，总空格为n。单词间的空格数是m/n+1 ，其中"+1"只有m%n个。
        1.2.2. 最后一行是特例每个word用一个空格填充，尾部补全空格。

        Args:
            words:
            maxWidth:

        Returns:

        """
        ret = []
        # review 要根据下一步的结果决定当前步的操作
        r = 0
        while r < len(words):
            # 重置中间变量
            l = r
            len_t = 0
            # 1.计算当前行可以容纳的word
            while r < len(words) and len_t + len(words[r]) <= maxWidth:
                len_t = len_t + len(words[r]) + 1
                r += 1
            # 计算需要填充的空格总量
            m = maxWidth - len_t + (r - l)  # 空格总数
            n = r - l - 1  # 放置空格的间隔数,即word之间的空隙数
            # 2.格式化
            t = ''
            # 最后一行特殊处理
            if r == len(words):
                t = " ".join(words[l:r])
                t += " " * (maxWidth - len(t))  # 补全空格
            # 非最后一行
            else:
                if r - l == 1:  # 本行只有一个word
                    t = words[l] + (' ' * (maxWidth - len(words[l])))
                else:  # 本行有多个word
                    c = m % n
                    for w in words[l:r - 1]:
                        t += w + (' ' * (m // n))
                        if c > 0:
                            t += ' '
                            c -= 1
                    t += words[r - 1]  # 最后一个word
            # 3.加入结果集
            ret.append(t)

        return ret


def do_func(words: list, maxWidth: int, expect: list):
    ret = Solution().fullJustify(words, maxWidth)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(["This", "is", "an", "example", "of", "text", "justification."], 16, [
        "This    is    an",
        "example  of text",
        "justification.  "
    ])
    do_func(["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ])
    do_func(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"], 20, [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
            ])
    do_func(["this"], 20, ["this                "])


if __name__ == "__main__":
    main()
