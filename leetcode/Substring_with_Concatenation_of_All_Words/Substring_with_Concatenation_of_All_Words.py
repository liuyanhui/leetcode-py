class Solution:
    def findSubstring(self, s, words):
        """
        https://leetcode.com/problems/substring-with-concatenation-of-all-words/
        30. Substring with Concatenation of All Words
        tip:
        1.words中每个单词长度固定,所以right和left每次前进这个固定的长度
        2.跟find_all_anagrams_in_a_string类似,只不过anagram是单个字符,这个是固定长度的单词
        :param words:
        :param s:
        """
        ret = []
        if not s or not words:
            return ret

        word_length = len(words[0])
        for i in range(word_length):
            dict_appear_word = {}
            for w in words:
                dict_appear_word[w] = dict_appear_word.get(w, 0) + 1
            count = len(dict_appear_word)
            right = i
            left = i
            while right < len(s):
                r_word = s[right:right + word_length]
                if r_word in dict_appear_word:
                    dict_appear_word[r_word] -= 1
                    if dict_appear_word[r_word] == 0:
                        count -= 1
                right += word_length

                while count == 0:
                    l_word = s[left:left + word_length]
                    if l_word in dict_appear_word:
                        if dict_appear_word[l_word] == 0:
                            count += 1
                        dict_appear_word[l_word] += 1

                    if right - left == len(words) * word_length:
                        ret.append(left)

                    left += word_length

        return ret


def main():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    ret = Solution().findSubstring(s, words)
    print(ret)

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    ret = Solution().findSubstring(s, words)
    print(ret)

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    ret = Solution().findSubstring(s, words)
    print(ret)

    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    ret = Solution().findSubstring(s, words)
    print(ret)

    s = "aaaaaaaa"
    words = ["aa", "aa", "aa"]
    ret = Solution().findSubstring(s, words)
    print(ret)


if __name__ == "__main__":
    main()
