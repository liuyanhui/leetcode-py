import sys


class Solution:
    def convert(self, s, numRows):
        if s == '' and numRows < 0:
            return ''
        if len(s) == 1 or numRows == 1:
            return s

        zigzagArray = [['' for i in range(len(s))] for i in range(numRows)]
        i = 0
        j = 0
        for letter in s:
            if j % (numRows - 1) == 0 and i < numRows:
                zigzagArray[i][j] = letter
                i += 1
            elif i == numRows:
                i -= 2
                j += 1
                zigzagArray[i][j] = letter
                if numRows == 2:
                    i += 1
                    pass
                else:
                    i -= 1
                    j += 1
            elif j % (numRows - 1) != 0 and i > 0:
                zigzagArray[i][j] = letter
                i -= 1
                j += 1

        print(zigzagArray)

        for x in zigzagArray:
            print(x)

        ret = ''
        for a in zigzagArray:
            for b in a:
                ret += b

        print(ret)
        return ret


def main():
    ret = Solution().convert('yrokktvusuiqiojfckyatryekijksvusokcyeavwufpctajxkixdbxjmitwcqqxfbbfhbadvfuaaujxfrwkvuuhep', 76)
    out = (ret);
    print(out)


if __name__ == '__main__':
    main()
