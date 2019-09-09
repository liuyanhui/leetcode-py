"""
https://leetcode.com/problems/word-search-ii/
212. Word Search II
Hard
-----------------------------------
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

import leetcode.implement_trie_prefix_tree.implement_trie_prefix_tree as TrieTree


class Solution:
    def findWords(self, board, words):
        return self.findWords_5(board, words)

    def findWords_1(self, board, words):
        """
        采用深度搜索的思路,通过stack记录访问过程
        1.顺时针方向遍历neighbor,从12点开始
        2.需要记录上一个字母的位置,因为一个位置只能使用一次
        结果Time Limit Exceeded,超时了.需要更巧妙的方法
        :param board:
        :param words:
        :return:
        """
        if board is None and len(board) == 0:
            return None
        if words is None and len(words) == 0:
            return []

        ret = []
        visted = set()

        def do_find(word, beg, board_x, board_y, last_p):
            """
            1.需要记录轨迹,防止某个节点被重复访问

            :param word: 当前需要匹配的单词
            :param beg: word中当前处理的字符index
            :param board_x: 当前处理的board中的index
            :param board_y: 当前处理的board中的index
            :param last_p: -1,12,3,6,9分别对应四个方向,-1表示没有方向,12表示12点方向,3表示3点方向,以此类推
            :return:
            """
            # board 边界溢出判断
            if board_x < 0 or board_x >= len(board) or board_y < 0 or board_y >= len(board[0]):
                return False
            # 处理的字符串超长
            if beg >= len(word):
                return False
            visted_set_key = str(board_x) + "-" + str(board_y)
            if visted_set_key in visted:
                return False
            else:
                visted.add(visted_set_key)
            if word[beg] == board[board_x][board_y]:
                # 跳出递归的条件判断
                if beg == len(word) - 1:
                    if ret.count(word) == 0:
                        ret.append(word)
                    return True

                # 顺时针遍历,用来匹配下一个字母
                matched = False
                # 12点方向
                if last_p != 12:
                    matched = do_find(word, beg + 1, board_x - 1, board_y, 6)
                if matched is False and last_p != 3:
                    # 3点方向
                    matched = do_find(word, beg + 1, board_x, board_y + 1, 9)
                if matched is False and last_p != 6:
                    # 6点方向
                    matched = do_find(word, beg + 1, board_x + 1, board_y, 12)
                if matched is False and last_p != 9:
                    # 9点方向
                    matched = do_find(word, beg + 1, board_x, board_y - 1, 3)

            visted.remove(visted_set_key)
            return False

        for w in words:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    visted.clear()
                    # 处理的字符串超长
                    if len(w) > len(board) * len(board[i]):
                        continue
                    do_find(w, 0, i, j, 0)

        return ret

    def findWords_2(self, board, words):
        """
        findWords_1的优化版本
        采用Trie tree
        通过验证:
        Runtime: 1456 ms, faster than 5.06% of Python3 online submissions for Word Search II.
        Memory Usage: 38.2 MB, less than 41.67% of Python3 online submissions for Word Search II.
        :param board:
        :param words:
        :return:
        """

        if board is None and len(board) == 0:
            return None
        if words is None and len(words) == 0:
            return []
        ret = []
        trie = TrieTree.Trie()
        for w in words:
            trie.insert(w)

        visitedSet = set()

        def dfs(i, j, curWord, srcPosition):
            """

            :param i:
            :param j:
            :param srcPosition: 前一个字母的方向
            :return:
            """
            tmpKey = str(i) + ":" + str(j)
            if tmpKey in visitedSet:
                return

            curWord += board[i][j]

            if not trie.startsWith(curWord):
                return
            if trie.search(curWord):
                if ret.count(curWord) == 0:
                    ret.append(curWord)
                    # 下面的return必须注释掉,因为即使匹配了某个字符串,仍然需要继续匹配后续长度的字符串
                    # return

            visitedSet.add(tmpKey)

            # 12 o'clock
            if srcPosition != 12 and i - 1 >= 0:
                dfs(i - 1, j, curWord, 6)
            # 3 o'clock
            if srcPosition != 3 and j + 1 < len(board[i]):
                dfs(i, j + 1, curWord, 9)
            # 6 o'clock
            if srcPosition != 6 and i + 1 < len(board):
                dfs(i + 1, j, curWord, 12)
            # 9 o'clock
            if srcPosition != 9 and j - 1 >= 0:
                dfs(i, j - 1, curWord, 3)

            visitedSet.remove(tmpKey)

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, "", -1)

        return ret

    def findWords_3(self, board, words):
        """
        findWords_2的优化版本
        采用Trie tree
        1.优化findWords_2中的visitedSet,
        :param board:
        :param words:
        :return:
        """

        if board is None and len(board) == 0:
            return None
        if words is None and len(words) == 0:
            return []
        ret = []
        trie = TrieTree.Trie()
        for w in words:
            trie.insert(w)

        def dfs(i, j, curWord, srcPosition):
            curChar = board[i][j]
            curWord += curChar
            if not trie.startsWith(curWord):
                return
            if trie.search(curWord):
                if ret.count(curWord) == 0:
                    ret.append(curWord)

            board[i][j] = "#"

            # 12 o'clock
            if srcPosition != 12 and i - 1 >= 0:
                dfs(i - 1, j, curWord, 6)
            # 3 o'clock
            if srcPosition != 3 and j + 1 < len(board[i]):
                dfs(i, j + 1, curWord, 9)
            # 6 o'clock
            if srcPosition != 6 and i + 1 < len(board):
                dfs(i + 1, j, curWord, 12)
            # 9 o'clock
            if srcPosition != 9 and j - 1 >= 0:
                dfs(i, j - 1, curWord, 3)

            board[i][j] = curChar

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, "", -1)

        return ret

    def findWords_4(self, board, words):
        """
        基于findWords_3的版本继续优化,
        参考思路:https://leetcode.com/problems/word-search-ii/discuss/59780/Java-15ms-Easiest-Solution-(100.00)
        1.主要是优化Trie树的startsWith()逻辑,采用更巧妙的方式.然而,并不是修改Trie的逻辑.
        执行结果表明,优化效果非常明显,执行时间大幅缩短,由1456 ms降低到372ms.如下所示:
        Runtime: 372 ms, faster than 72.30% of Python3 online submissions for Word Search II.
        Memory Usage: 38.2 MB, less than 41.67% of Python3 online submissions for Word Search II.
        :param board:
        :param words:
        :return:
        """

        if board is None and len(board) == 0:
            return None
        if words is None and len(words) == 0:
            return []
        ret = []
        trie = TrieTree.Trie()
        for w in words:
            trie.insert(w)

        def dfs(i, j, curWord, srcPosition, trieNode):
            curChar = board[i][j]
            curIndex = ord(curChar) - ord('a')
            # 利用trie tree的特点取代startWiths()方法
            if 0 > curIndex or curIndex > 26 or not trieNode.child[curIndex]:
                return

            curWord += board[i][j]
            nextTrieNode = trieNode.child[curIndex]
            if nextTrieNode.isWord:
                if ret.count(curWord) == 0:
                    ret.append(curWord)

            board[i][j] = "#"
            # 12 o'clock
            if srcPosition != 12 and i - 1 >= 0:
                dfs(i - 1, j, curWord, 6, nextTrieNode)
            # 3 o'clock
            if srcPosition != 3 and j + 1 < len(board[i]):
                dfs(i, j + 1, curWord, 9, nextTrieNode)
            # 6 o'clock
            if srcPosition != 6 and i + 1 < len(board):
                dfs(i + 1, j, curWord, 12, nextTrieNode)
            # 9 o'clock
            if srcPosition != 9 and j - 1 >= 0:
                dfs(i, j - 1, curWord, 3, nextTrieNode)

            board[i][j] = curChar

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, "", -1, trie.root)

        return ret

    def findWords_5(self, board, words):
        """
        基于findWords_4的版本继续优化,
        1.0 > curIndex or curIndex > 26 替换为 curChar=="#"
        2.if ret.count(curWord) == 0: 去重代码优化
        3.去掉dfs中的srcPosition参数
        :param board:
        :param words:
        :return:
        """

        if board is None and len(board) == 0:
            return None
        if words is None and len(words) == 0:
            return []
        ret = []
        trie = TrieTree.Trie()
        for w in words:
            trie.insert(w)

        def dfs(i, j, curWord, trieNode):
            curChar = board[i][j]
            curIndex = ord(curChar) - ord('a')
            # 利用trie tree的特点取代startWiths()方法
            if curChar == "#" or not trieNode.child[curIndex]:
                return

            curWord += board[i][j]
            nextTrieNode = trieNode.child[curIndex]
            if nextTrieNode.isWord:  # 单词匹配
                ret.append(curWord)
                nextTrieNode.isWord = False  # 结果去重

            board[i][j] = "#"
            # 12 o'clock
            if i - 1 >= 0:
                dfs(i - 1, j, curWord, nextTrieNode)
            # 3 o'clock
            if j + 1 < len(board[i]):
                dfs(i, j + 1, curWord, nextTrieNode)
            # 6 o'clock
            if i + 1 < len(board):
                dfs(i + 1, j, curWord, nextTrieNode)
            # 9 o'clock
            if j - 1 >= 0:
                dfs(i, j - 1, curWord, nextTrieNode)

            board[i][j] = curChar

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, "", trie.root)

        return ret


def main():
    b = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    w = ["oath", "pea", "eat", "rain"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")

    b = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    w = ["o", "a", "eat", "rain"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")

    b = [["a", "a"]]
    w = ["a"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")

    b = [["a", "a", "a", "a"],
         ["a", "a", "a", "a"],
         ["a", "a", "a", "a"]]
    w = ["aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaab"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")

    b = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
         ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
         ["a", "a", "b", "a", "a", "b"]]
    w = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
         "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
         "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
         "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
         "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
         "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
         "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
         "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
         "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
         "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")

    b = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"], ["b", "c", "d", "e"],
         ["f", "g", "h", "i"], ["j", "k", "l", "m"], ["n", "o", "p", "q"], ["r", "s", "t", "u"], ["v", "w", "x", "y"],
         ["z", "z", "z", "z"]]
    w = ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac", "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae",
         "aaaaaaaaaaaaaaaf", "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai", "aaaaaaaaaaaaaaaj",
         "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal", "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao",
         "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar", "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat",
         "aaaaaaaaaaaaaaau", "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax", "aaaaaaaaaaaaaaay",
         "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba", "aaaaaaaaaaaaaabb", "aaaaaaaaaaaaaabc", "aaaaaaaaaaaaaabd",
         "aaaaaaaaaaaaaabe", "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg", "aaaaaaaaaaaaaabh", "aaaaaaaaaaaaaabi",
         "aaaaaaaaaaaaaabj", "aaaaaaaaaaaaaabk", "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm", "aaaaaaaaaaaaaabn",
         "aaaaaaaaaaaaaabo", "aaaaaaaaaaaaaabp", "aaaaaaaaaaaaaabq", "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs",
         "aaaaaaaaaaaaaabt", "aaaaaaaaaaaaaabu", "aaaaaaaaaaaaaabv", "aaaaaaaaaaaaaabw", "aaaaaaaaaaaaaabx",
         "aaaaaaaaaaaaaaby", "aaaaaaaaaaaaaabz", "aaaaaaaaaaaaaaca", "aaaaaaaaaaaaaacb", "aaaaaaaaaaaaaacc",
         "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace", "aaaaaaaaaaaaaacf", "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaach",
         "aaaaaaaaaaaaaaci", "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack", "aaaaaaaaaaaaaacl", "aaaaaaaaaaaaaacm",
         "aaaaaaaaaaaaaacn", "aaaaaaaaaaaaaaco", "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq", "aaaaaaaaaaaaaacr",
         "aaaaaaaaaaaaaacs", "aaaaaaaaaaaaaact", "aaaaaaaaaaaaaacu", "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw",
         "aaaaaaaaaaaaaacx", "aaaaaaaaaaaaaacy", "aaaaaaaaaaaaaacz", "aaaaaaaaaaaaaada", "aaaaaaaaaaaaaadb",
         "aaaaaaaaaaaaaadc", "aaaaaaaaaaaaaadd", "aaaaaaaaaaaaaade", "aaaaaaaaaaaaaadf", "aaaaaaaaaaaaaadg",
         "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi", "aaaaaaaaaaaaaadj", "aaaaaaaaaaaaaadk", "aaaaaaaaaaaaaadl",
         "aaaaaaaaaaaaaadm", "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado", "aaaaaaaaaaaaaadp", "aaaaaaaaaaaaaadq",
         "aaaaaaaaaaaaaadr", "aaaaaaaaaaaaaads", "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu", "aaaaaaaaaaaaaadv",
         "aaaaaaaaaaaaaadw", "aaaaaaaaaaaaaadx", "aaaaaaaaaaaaaady", "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea",
         "aaaaaaaaaaaaaaeb", "aaaaaaaaaaaaaaec", "aaaaaaaaaaaaaaed", "aaaaaaaaaaaaaaee", "aaaaaaaaaaaaaaef",
         "aaaaaaaaaaaaaaeg", "aaaaaaaaaaaaaaeh", "aaaaaaaaaaaaaaei", "aaaaaaaaaaaaaaej", "aaaaaaaaaaaaaaek",
         "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem", "aaaaaaaaaaaaaaen", "aaaaaaaaaaaaaaeo", "aaaaaaaaaaaaaaep",
         "aaaaaaaaaaaaaaeq", "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes", "aaaaaaaaaaaaaaet", "aaaaaaaaaaaaaaeu",
         "aaaaaaaaaaaaaaev", "aaaaaaaaaaaaaaew", "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey", "aaaaaaaaaaaaaaez",
         "aaaaaaaaaaaaaafa", "aaaaaaaaaaaaaafb", "aaaaaaaaaaaaaafc", "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe",
         "aaaaaaaaaaaaaaff", "aaaaaaaaaaaaaafg", "aaaaaaaaaaaaaafh", "aaaaaaaaaaaaaafi", "aaaaaaaaaaaaaafj",
         "aaaaaaaaaaaaaafk", "aaaaaaaaaaaaaafl", "aaaaaaaaaaaaaafm", "aaaaaaaaaaaaaafn", "aaaaaaaaaaaaaafo",
         "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq", "aaaaaaaaaaaaaafr", "aaaaaaaaaaaaaafs", "aaaaaaaaaaaaaaft",
         "aaaaaaaaaaaaaafu", "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw", "aaaaaaaaaaaaaafx", "aaaaaaaaaaaaaafy",
         "aaaaaaaaaaaaaafz", "aaaaaaaaaaaaaaga", "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc", "aaaaaaaaaaaaaagd",
         "aaaaaaaaaaaaaage", "aaaaaaaaaaaaaagf", "aaaaaaaaaaaaaagg", "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi",
         "aaaaaaaaaaaaaagj", "aaaaaaaaaaaaaagk", "aaaaaaaaaaaaaagl", "aaaaaaaaaaaaaagm", "aaaaaaaaaaaaaagn",
         "aaaaaaaaaaaaaago", "aaaaaaaaaaaaaagp", "aaaaaaaaaaaaaagq", "aaaaaaaaaaaaaagr", "aaaaaaaaaaaaaags",
         "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu", "aaaaaaaaaaaaaagv", "aaaaaaaaaaaaaagw", "aaaaaaaaaaaaaagx",
         "aaaaaaaaaaaaaagy", "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha", "aaaaaaaaaaaaaahb", "aaaaaaaaaaaaaahc",
         "aaaaaaaaaaaaaahd", "aaaaaaaaaaaaaahe", "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg", "aaaaaaaaaaaaaahh",
         "aaaaaaaaaaaaaahi", "aaaaaaaaaaaaaahj", "aaaaaaaaaaaaaahk", "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm",
         "aaaaaaaaaaaaaahn", "aaaaaaaaaaaaaaho", "aaaaaaaaaaaaaahp", "aaaaaaaaaaaaaahq", "aaaaaaaaaaaaaahr",
         "aaaaaaaaaaaaaahs", "aaaaaaaaaaaaaaht", "aaaaaaaaaaaaaahu", "aaaaaaaaaaaaaahv", "aaaaaaaaaaaaaahw",
         "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy", "aaaaaaaaaaaaaahz", "aaaaaaaaaaaaaaia", "aaaaaaaaaaaaaaib",
         "aaaaaaaaaaaaaaic", "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie", "aaaaaaaaaaaaaaif", "aaaaaaaaaaaaaaig",
         "aaaaaaaaaaaaaaih", "aaaaaaaaaaaaaaii", "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik", "aaaaaaaaaaaaaail",
         "aaaaaaaaaaaaaaim", "aaaaaaaaaaaaaain", "aaaaaaaaaaaaaaio", "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq",
         "aaaaaaaaaaaaaair", "aaaaaaaaaaaaaais", "aaaaaaaaaaaaaait", "aaaaaaaaaaaaaaiu", "aaaaaaaaaaaaaaiv",
         "aaaaaaaaaaaaaaiw", "aaaaaaaaaaaaaaix", "aaaaaaaaaaaaaaiy", "aaaaaaaaaaaaaaiz", "aaaaaaaaaaaaaaja",
         "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc", "aaaaaaaaaaaaaajd", "aaaaaaaaaaaaaaje", "aaaaaaaaaaaaaajf",
         "aaaaaaaaaaaaaajg", "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji", "aaaaaaaaaaaaaajj", "aaaaaaaaaaaaaajk",
         "aaaaaaaaaaaaaajl", "aaaaaaaaaaaaaajm", "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo", "aaaaaaaaaaaaaajp",
         "aaaaaaaaaaaaaajq", "aaaaaaaaaaaaaajr", "aaaaaaaaaaaaaajs", "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju",
         "aaaaaaaaaaaaaajv", "aaaaaaaaaaaaaajw", "aaaaaaaaaaaaaajx", "aaaaaaaaaaaaaajy", "aaaaaaaaaaaaaajz",
         "aaaaaaaaaaaaaaka", "aaaaaaaaaaaaaakb", "aaaaaaaaaaaaaakc", "aaaaaaaaaaaaaakd", "aaaaaaaaaaaaaake",
         "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg", "aaaaaaaaaaaaaakh", "aaaaaaaaaaaaaaki", "aaaaaaaaaaaaaakj",
         "aaaaaaaaaaaaaakk", "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm", "aaaaaaaaaaaaaakn", "aaaaaaaaaaaaaako",
         "aaaaaaaaaaaaaakp", "aaaaaaaaaaaaaakq", "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks", "aaaaaaaaaaaaaakt",
         "aaaaaaaaaaaaaaku", "aaaaaaaaaaaaaakv", "aaaaaaaaaaaaaakw", "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky",
         "aaaaaaaaaaaaaakz", "aaaaaaaaaaaaaala", "aaaaaaaaaaaaaalb", "aaaaaaaaaaaaaalc", "aaaaaaaaaaaaaald",
         "aaaaaaaaaaaaaale", "aaaaaaaaaaaaaalf", "aaaaaaaaaaaaaalg", "aaaaaaaaaaaaaalh", "aaaaaaaaaaaaaali",
         "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk", "aaaaaaaaaaaaaall", "aaaaaaaaaaaaaalm", "aaaaaaaaaaaaaaln",
         "aaaaaaaaaaaaaalo", "aaaaaaaaaaaaaalp", "aaaaaaaaaaaaaalq", "aaaaaaaaaaaaaalr", "aaaaaaaaaaaaaals",
         "aaaaaaaaaaaaaalt", "aaaaaaaaaaaaaalu", "aaaaaaaaaaaaaalv", "aaaaaaaaaaaaaalw", "aaaaaaaaaaaaaalx",
         "aaaaaaaaaaaaaaly", "aaaaaaaaaaaaaalz", "aaaaaaaaaaaaaama", "aaaaaaaaaaaaaamb", "aaaaaaaaaaaaaamc",
         "aaaaaaaaaaaaaamd", "aaaaaaaaaaaaaame", "aaaaaaaaaaaaaamf", "aaaaaaaaaaaaaamg", "aaaaaaaaaaaaaamh",
         "aaaaaaaaaaaaaami", "aaaaaaaaaaaaaamj", "aaaaaaaaaaaaaamk", "aaaaaaaaaaaaaaml", "aaaaaaaaaaaaaamm",
         "aaaaaaaaaaaaaamn", "aaaaaaaaaaaaaamo", "aaaaaaaaaaaaaamp", "aaaaaaaaaaaaaamq", "aaaaaaaaaaaaaamr",
         "aaaaaaaaaaaaaams", "aaaaaaaaaaaaaamt", "aaaaaaaaaaaaaamu", "aaaaaaaaaaaaaamv", "aaaaaaaaaaaaaamw",
         "aaaaaaaaaaaaaamx", "aaaaaaaaaaaaaamy", "aaaaaaaaaaaaaamz", "aaaaaaaaaaaaaana", "aaaaaaaaaaaaaanb",
         "aaaaaaaaaaaaaanc", "aaaaaaaaaaaaaand", "aaaaaaaaaaaaaane", "aaaaaaaaaaaaaanf", "aaaaaaaaaaaaaang",
         "aaaaaaaaaaaaaanh", "aaaaaaaaaaaaaani", "aaaaaaaaaaaaaanj", "aaaaaaaaaaaaaank", "aaaaaaaaaaaaaanl",
         "aaaaaaaaaaaaaanm", "aaaaaaaaaaaaaann", "aaaaaaaaaaaaaano", "aaaaaaaaaaaaaanp", "aaaaaaaaaaaaaanq",
         "aaaaaaaaaaaaaanr", "aaaaaaaaaaaaaans", "aaaaaaaaaaaaaant", "aaaaaaaaaaaaaanu", "aaaaaaaaaaaaaanv",
         "aaaaaaaaaaaaaanw", "aaaaaaaaaaaaaanx", "aaaaaaaaaaaaaany", "aaaaaaaaaaaaaanz", "aaaaaaaaaaaaaaoa",
         "aaaaaaaaaaaaaaob", "aaaaaaaaaaaaaaoc", "aaaaaaaaaaaaaaod", "aaaaaaaaaaaaaaoe", "aaaaaaaaaaaaaaof",
         "aaaaaaaaaaaaaaog", "aaaaaaaaaaaaaaoh", "aaaaaaaaaaaaaaoi", "aaaaaaaaaaaaaaoj", "aaaaaaaaaaaaaaok",
         "aaaaaaaaaaaaaaol", "aaaaaaaaaaaaaaom", "aaaaaaaaaaaaaaon", "aaaaaaaaaaaaaaoo", "aaaaaaaaaaaaaaop",
         "aaaaaaaaaaaaaaoq", "aaaaaaaaaaaaaaor", "aaaaaaaaaaaaaaos", "aaaaaaaaaaaaaaot", "aaaaaaaaaaaaaaou",
         "aaaaaaaaaaaaaaov", "aaaaaaaaaaaaaaow", "aaaaaaaaaaaaaaox", "aaaaaaaaaaaaaaoy", "aaaaaaaaaaaaaaoz",
         "aaaaaaaaaaaaaapa", "aaaaaaaaaaaaaapb", "aaaaaaaaaaaaaapc", "aaaaaaaaaaaaaapd", "aaaaaaaaaaaaaape",
         "aaaaaaaaaaaaaapf", "aaaaaaaaaaaaaapg", "aaaaaaaaaaaaaaph", "aaaaaaaaaaaaaapi", "aaaaaaaaaaaaaapj",
         "aaaaaaaaaaaaaapk", "aaaaaaaaaaaaaapl", "aaaaaaaaaaaaaapm", "aaaaaaaaaaaaaapn", "aaaaaaaaaaaaaapo",
         "aaaaaaaaaaaaaapp", "aaaaaaaaaaaaaapq", "aaaaaaaaaaaaaapr", "aaaaaaaaaaaaaaps", "aaaaaaaaaaaaaapt",
         "aaaaaaaaaaaaaapu", "aaaaaaaaaaaaaapv", "aaaaaaaaaaaaaapw", "aaaaaaaaaaaaaapx", "aaaaaaaaaaaaaapy",
         "aaaaaaaaaaaaaapz", "aaaaaaaaaaaaaaqa", "aaaaaaaaaaaaaaqb", "aaaaaaaaaaaaaaqc", "aaaaaaaaaaaaaaqd",
         "aaaaaaaaaaaaaaqe", "aaaaaaaaaaaaaaqf", "aaaaaaaaaaaaaaqg", "aaaaaaaaaaaaaaqh", "aaaaaaaaaaaaaaqi",
         "aaaaaaaaaaaaaaqj", "aaaaaaaaaaaaaaqk", "aaaaaaaaaaaaaaql", "aaaaaaaaaaaaaaqm", "aaaaaaaaaaaaaaqn",
         "aaaaaaaaaaaaaaqo", "aaaaaaaaaaaaaaqp", "aaaaaaaaaaaaaaqq", "aaaaaaaaaaaaaaqr", "aaaaaaaaaaaaaaqs",
         "aaaaaaaaaaaaaaqt", "aaaaaaaaaaaaaaqu", "aaaaaaaaaaaaaaqv", "aaaaaaaaaaaaaaqw", "aaaaaaaaaaaaaaqx",
         "aaaaaaaaaaaaaaqy", "aaaaaaaaaaaaaaqz", "aaaaaaaaaaaaaara", "aaaaaaaaaaaaaarb", "aaaaaaaaaaaaaarc",
         "aaaaaaaaaaaaaard", "aaaaaaaaaaaaaare", "aaaaaaaaaaaaaarf", "aaaaaaaaaaaaaarg", "aaaaaaaaaaaaaarh",
         "aaaaaaaaaaaaaari", "aaaaaaaaaaaaaarj", "aaaaaaaaaaaaaark", "aaaaaaaaaaaaaarl", "aaaaaaaaaaaaaarm",
         "aaaaaaaaaaaaaarn", "aaaaaaaaaaaaaaro", "aaaaaaaaaaaaaarp", "aaaaaaaaaaaaaarq", "aaaaaaaaaaaaaarr",
         "aaaaaaaaaaaaaars", "aaaaaaaaaaaaaart", "aaaaaaaaaaaaaaru", "aaaaaaaaaaaaaarv", "aaaaaaaaaaaaaarw",
         "aaaaaaaaaaaaaarx", "aaaaaaaaaaaaaary", "aaaaaaaaaaaaaarz", "aaaaaaaaaaaaaasa", "aaaaaaaaaaaaaasb",
         "aaaaaaaaaaaaaasc", "aaaaaaaaaaaaaasd", "aaaaaaaaaaaaaase", "aaaaaaaaaaaaaasf", "aaaaaaaaaaaaaasg",
         "aaaaaaaaaaaaaash", "aaaaaaaaaaaaaasi", "aaaaaaaaaaaaaasj", "aaaaaaaaaaaaaask", "aaaaaaaaaaaaaasl",
         "aaaaaaaaaaaaaasm", "aaaaaaaaaaaaaasn", "aaaaaaaaaaaaaaso", "aaaaaaaaaaaaaasp", "aaaaaaaaaaaaaasq",
         "aaaaaaaaaaaaaasr", "aaaaaaaaaaaaaass", "aaaaaaaaaaaaaast", "aaaaaaaaaaaaaasu", "aaaaaaaaaaaaaasv",
         "aaaaaaaaaaaaaasw", "aaaaaaaaaaaaaasx", "aaaaaaaaaaaaaasy", "aaaaaaaaaaaaaasz", "aaaaaaaaaaaaaata",
         "aaaaaaaaaaaaaatb", "aaaaaaaaaaaaaatc", "aaaaaaaaaaaaaatd", "aaaaaaaaaaaaaate", "aaaaaaaaaaaaaatf",
         "aaaaaaaaaaaaaatg", "aaaaaaaaaaaaaath", "aaaaaaaaaaaaaati", "aaaaaaaaaaaaaatj", "aaaaaaaaaaaaaatk",
         "aaaaaaaaaaaaaatl", "aaaaaaaaaaaaaatm", "aaaaaaaaaaaaaatn", "aaaaaaaaaaaaaato", "aaaaaaaaaaaaaatp",
         "aaaaaaaaaaaaaatq", "aaaaaaaaaaaaaatr", "aaaaaaaaaaaaaats", "aaaaaaaaaaaaaatt", "aaaaaaaaaaaaaatu",
         "aaaaaaaaaaaaaatv", "aaaaaaaaaaaaaatw", "aaaaaaaaaaaaaatx", "aaaaaaaaaaaaaaty", "aaaaaaaaaaaaaatz",
         "aaaaaaaaaaaaaaua", "aaaaaaaaaaaaaaub", "aaaaaaaaaaaaaauc", "aaaaaaaaaaaaaaud", "aaaaaaaaaaaaaaue",
         "aaaaaaaaaaaaaauf", "aaaaaaaaaaaaaaug", "aaaaaaaaaaaaaauh", "aaaaaaaaaaaaaaui", "aaaaaaaaaaaaaauj",
         "aaaaaaaaaaaaaauk", "aaaaaaaaaaaaaaul", "aaaaaaaaaaaaaaum", "aaaaaaaaaaaaaaun", "aaaaaaaaaaaaaauo",
         "aaaaaaaaaaaaaaup", "aaaaaaaaaaaaaauq", "aaaaaaaaaaaaaaur", "aaaaaaaaaaaaaaus", "aaaaaaaaaaaaaaut",
         "aaaaaaaaaaaaaauu", "aaaaaaaaaaaaaauv", "aaaaaaaaaaaaaauw", "aaaaaaaaaaaaaaux", "aaaaaaaaaaaaaauy",
         "aaaaaaaaaaaaaauz", "aaaaaaaaaaaaaava", "aaaaaaaaaaaaaavb", "aaaaaaaaaaaaaavc", "aaaaaaaaaaaaaavd",
         "aaaaaaaaaaaaaave", "aaaaaaaaaaaaaavf", "aaaaaaaaaaaaaavg", "aaaaaaaaaaaaaavh", "aaaaaaaaaaaaaavi",
         "aaaaaaaaaaaaaavj", "aaaaaaaaaaaaaavk", "aaaaaaaaaaaaaavl", "aaaaaaaaaaaaaavm", "aaaaaaaaaaaaaavn",
         "aaaaaaaaaaaaaavo", "aaaaaaaaaaaaaavp", "aaaaaaaaaaaaaavq", "aaaaaaaaaaaaaavr", "aaaaaaaaaaaaaavs",
         "aaaaaaaaaaaaaavt", "aaaaaaaaaaaaaavu", "aaaaaaaaaaaaaavv", "aaaaaaaaaaaaaavw", "aaaaaaaaaaaaaavx",
         "aaaaaaaaaaaaaavy", "aaaaaaaaaaaaaavz", "aaaaaaaaaaaaaawa", "aaaaaaaaaaaaaawb", "aaaaaaaaaaaaaawc",
         "aaaaaaaaaaaaaawd", "aaaaaaaaaaaaaawe", "aaaaaaaaaaaaaawf", "aaaaaaaaaaaaaawg", "aaaaaaaaaaaaaawh",
         "aaaaaaaaaaaaaawi", "aaaaaaaaaaaaaawj", "aaaaaaaaaaaaaawk", "aaaaaaaaaaaaaawl", "aaaaaaaaaaaaaawm",
         "aaaaaaaaaaaaaawn", "aaaaaaaaaaaaaawo", "aaaaaaaaaaaaaawp", "aaaaaaaaaaaaaawq", "aaaaaaaaaaaaaawr",
         "aaaaaaaaaaaaaaws", "aaaaaaaaaaaaaawt", "aaaaaaaaaaaaaawu", "aaaaaaaaaaaaaawv", "aaaaaaaaaaaaaaww",
         "aaaaaaaaaaaaaawx", "aaaaaaaaaaaaaawy", "aaaaaaaaaaaaaawz", "aaaaaaaaaaaaaaxa", "aaaaaaaaaaaaaaxb",
         "aaaaaaaaaaaaaaxc", "aaaaaaaaaaaaaaxd", "aaaaaaaaaaaaaaxe", "aaaaaaaaaaaaaaxf", "aaaaaaaaaaaaaaxg",
         "aaaaaaaaaaaaaaxh", "aaaaaaaaaaaaaaxi", "aaaaaaaaaaaaaaxj", "aaaaaaaaaaaaaaxk", "aaaaaaaaaaaaaaxl",
         "aaaaaaaaaaaaaaxm", "aaaaaaaaaaaaaaxn", "aaaaaaaaaaaaaaxo", "aaaaaaaaaaaaaaxp", "aaaaaaaaaaaaaaxq",
         "aaaaaaaaaaaaaaxr", "aaaaaaaaaaaaaaxs", "aaaaaaaaaaaaaaxt", "aaaaaaaaaaaaaaxu", "aaaaaaaaaaaaaaxv",
         "aaaaaaaaaaaaaaxw", "aaaaaaaaaaaaaaxx", "aaaaaaaaaaaaaaxy", "aaaaaaaaaaaaaaxz", "aaaaaaaaaaaaaaya",
         "aaaaaaaaaaaaaayb", "aaaaaaaaaaaaaayc", "aaaaaaaaaaaaaayd", "aaaaaaaaaaaaaaye", "aaaaaaaaaaaaaayf",
         "aaaaaaaaaaaaaayg", "aaaaaaaaaaaaaayh", "aaaaaaaaaaaaaayi", "aaaaaaaaaaaaaayj", "aaaaaaaaaaaaaayk",
         "aaaaaaaaaaaaaayl", "aaaaaaaaaaaaaaym", "aaaaaaaaaaaaaayn", "aaaaaaaaaaaaaayo", "aaaaaaaaaaaaaayp",
         "aaaaaaaaaaaaaayq", "aaaaaaaaaaaaaayr", "aaaaaaaaaaaaaays", "aaaaaaaaaaaaaayt", "aaaaaaaaaaaaaayu",
         "aaaaaaaaaaaaaayv", "aaaaaaaaaaaaaayw", "aaaaaaaaaaaaaayx", "aaaaaaaaaaaaaayy", "aaaaaaaaaaaaaayz",
         "aaaaaaaaaaaaaaza", "aaaaaaaaaaaaaazb", "aaaaaaaaaaaaaazc", "aaaaaaaaaaaaaazd", "aaaaaaaaaaaaaaze",
         "aaaaaaaaaaaaaazf", "aaaaaaaaaaaaaazg", "aaaaaaaaaaaaaazh", "aaaaaaaaaaaaaazi", "aaaaaaaaaaaaaazj",
         "aaaaaaaaaaaaaazk", "aaaaaaaaaaaaaazl", "aaaaaaaaaaaaaazm", "aaaaaaaaaaaaaazn", "aaaaaaaaaaaaaazo",
         "aaaaaaaaaaaaaazp", "aaaaaaaaaaaaaazq", "aaaaaaaaaaaaaazr", "aaaaaaaaaaaaaazs", "aaaaaaaaaaaaaazt",
         "aaaaaaaaaaaaaazu", "aaaaaaaaaaaaaazv", "aaaaaaaaaaaaaazw", "aaaaaaaaaaaaaazx", "aaaaaaaaaaaaaazy",
         "aaaaaaaaaaaaaazz"]
    ret = Solution().findWords(b, w)
    print(ret)
    print("----------------------")


if __name__ == "__main__":
    main()
