class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1
        for x in range(1, n+1):
            if offset*2 == x:
                offset = x
            dp[x] = 1 + dp[x-offset]
        return dp