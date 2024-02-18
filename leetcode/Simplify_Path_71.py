"""
71. Simplify Path
Medium
--------------------------
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        return self.simplifyPath_1(path)

    def simplifyPath_1(self, path: str) -> str:
        """
        Round 3
        Score[4] Lower is harder

        Thinking：
        1. 先根据'/'分割字符串为数组arr[]，再计算分割后的字符串
        2. 遍历arr[]，满足结果的arr[i]加入到结果集ret[]中
        2.1. 先提取和过滤root path的'/'
        2.2. IF arr[i]=='.' THEN 跳过arr[i]
        2.3. ELSE IF arr[i]=='..' THEN 删除arr[-1],跳过arr[i]
        2.4. ELSE IF arr[i]=='' THEN 跳过arr[i]
        2.5. ELSE ret.append(arr[i])
        3. 格式化ret为string, '/'.join(ret)

        验证通过:
        Runtime 39 ms Beats 52.45%
        Memory 16.62 MB Beats 66.53%
        """
        if not path:
            return ''
        arr = path.split('/')
        if not arr:
            return ''
        ret_list = []

        for s in arr:
            if s == '' or s == '.':
                pass
            elif s == '..':
                ret_list = ret_list[0:-1]
            else:
                ret_list.append(s)

        return '/'+('/'.join(ret_list))


def do_func(n: int, expect: int):
    ret = Solution().simplifyPath(n)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func("/home/", "/home")
    do_func("/../", "/")
    do_func("/home//foo/", "/home/foo")
    do_func("/home/.../foo/", "/home/.../foo")
    do_func("//////", "/")


if __name__ == "__main__":
    main()
