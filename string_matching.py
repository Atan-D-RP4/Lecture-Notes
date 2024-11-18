class Solution(object):
    def isMatchHelper(self, s, p):
        return p == '.' or s == p
    
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # Initialize dp table
        dp = [[False for i in range(n + 1)] 								 for j in range(m + 1)]
        					dp[0][0] = True
        
        # Handle patterns with leading *
        for i in range(2, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        
        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Two cases: 
                    # 1. Don't use * (zero occurrences)
                    # 2. Use * by matching current char with previous char in pattern
                    dp[i][j] = dp[i][j - 2] or \
                              (self.isMatchHelper(s[i - 1], p[j - 2]) and dp[i - 1][j])
                else:
                    # For non-* chars, check if current chars match and previous state was match
                    if self.isMatchHelper(s[i - 1], p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]