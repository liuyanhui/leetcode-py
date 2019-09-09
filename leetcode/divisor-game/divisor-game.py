class Solution:
    """
    https://leetcode.com/problems/divisor-game/
    1025. Divisor Game
    easy
    """

    def divisorGame(self, N):
        return self.divisorGame_2(N)

    def divisorGame_1(self, N):
        """
        DP问题，公式为：dp[i]=!dp[i-1] or !dp[i1] or !dp[i2]。其中i-i%j==0时，in=i-i%j。
        直观理解：N是否True，取决于第一步的选择，之后的选择又依赖于上一步的选择，一次类推。
        """
        if N <= 1:
            return False
        dp = [False] * (N + 1)
        dp[1] = False
        for i in range(1, N + 1):
            signal = False
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    signal = True
                    break
            dp[i] = signal
        # print(str(dp))
        return dp[N]

    def divisorGame_2(self, N):
        """
        even 赢，odd输
        参考https://leetcode.com/problems/divisor-game/discuss/274566/just-return-N-2-0-(proof)
        """
        if N <= 1:
            return False
        return N % 2 == 0
