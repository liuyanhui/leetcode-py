class Solution:
    def reverse_words(self, s):
        if not s.strip():
            return ""
        print(s.strip())
        ret = ""
        split_arr = s.strip().split()
        print(split_arr)
        split_arr.reverse()
        print(split_arr)
        for w in split_arr:
            ret += w + " "
        ret = ret.strip()

        print(type(s.strip().split().reverse()))
        print(" ".join(s.strip().split()[::-1]))
        print(" ".join(reversed(s.split())))

        return ret


def main():
    s = "this is string example....wow!!!"
    s = "the sky is blue    "
    s = "  hello world!  "
    # s = "a good   example"
    ret = Solution().reverse_words(s)
    print(ret)


if __name__ == '__main__':
    main()
