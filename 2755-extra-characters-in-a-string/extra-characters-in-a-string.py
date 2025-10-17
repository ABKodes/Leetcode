class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1
            for w in dictionary:
                w_len = len(w)
                if i >= w_len and s[i - w_len:i] == w:
                    dp[i] = min(dp[i], dp[i - w_len])
        
        return dp[n]