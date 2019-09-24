"""
https://leetcode.com/discuss/interview-question/347457
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""


class Solution:
    def find_shortest_route(self, map):
        return self.find_shortest_route_bfs(map)

    def find_shortest_route_bfs(self, map):
        """
        因为是求minstep所以bfs思路更合理.在bfs情况下,第一个到达目的就是最小步数.而dfs无法做到这一点.
        1.访问过的节点,值设置为1
        2.通过两个队列来缓存节点,一个保存当前bfs层级的节点,另一个保存下一个bfs层级的节点
        :param map:
        :return:
        """
        ret = 0
        max_x = len(map)
        max_y = len(map[0])
        que_cur = [[0, 0]]
        que_next = []
        while que_cur:
            tmp_l = que_cur.pop(0)
            x = tmp_l[0]
            y = tmp_l[1]
            if map[x][y] == 'X':
                return ret
            # 设置为已访问
            map[x][y] = '1'
            # 顺时针入队
            # 12点方向
            t_x, t_y = x - 1, y
            if 0 <= t_x and map[t_x][t_y] not in ['D', '1']:
                que_next.append([t_x, t_y])
            # 3点方向
            t_x, t_y = x, y + 1
            if t_y < max_y and map[t_x][t_y] not in ['D', '1']:
                que_next.append([t_x, t_y])
            # 6点方向
            t_x, t_y = x + 1, y
            if t_x < max_x and map[t_x][t_y] not in ['D', '1']:
                que_next.append([t_x, t_y])
            # 9点方向
            t_x, t_y = x, y - 1
            if 0 <= t_y and map[t_x][t_y] not in ['D', '1']:
                que_next.append([t_x, t_y])

            # 最后把que_next赋值给que_cur,并清空que_next
            if len(que_cur) == 0 and len(que_next) > 0:
                que_cur = que_next.copy()
                que_next.clear()
                ret += 1

        return -1


def main():
    map = [['O', 'O', 'O', 'O'],
           ['D', 'O', 'D', 'O'],
           ['O', 'O', 'O', 'O'],
           ['X', 'D', 'D', 'O']]
    ret = Solution().find_shortest_route(map)
    print(ret)
    print("-----------")

    map = [['O', 'O', 'O', 'O'],
           ['D', 'O', 'D', 'O'],
           ['O', 'O', 'O', 'O'],
           ['D', 'D', 'D', 'O']]
    ret = Solution().find_shortest_route(map)
    print(ret)
    print("-----------")


if __name__ == "__main__":
    main()
