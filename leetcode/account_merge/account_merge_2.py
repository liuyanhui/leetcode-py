import collections


class Account_merge_2:
    def accounts_merge(self, accounts):
        ret = collections.defaultdict(set)
        for tmplist in accounts:
            ret[tmplist[0]].add(tmplist[1:])

        return ret


def match(text, pattern):
    if not pattern:
        return not text
    print(bool(text))

    print("222=", ('dddd' in {text[0], '.'}))

    first_match = bool(text) and pattern[0] in {text[0], '.'}
    print("first_match=%s,%d" %(first_match, 3))
    return first_match and match(text[1:], pattern[1:])


def main():
    match('abc', 'abc')


if __name__ == '__main__':
    main()
