class Solution:
    def uniquePaths(self, m: int, n: int) -> int:      
        
      
        
        dp = [[0]*(m) for i in range(n)]
        
        dp[0][0] = 1      
        
      
        for i in range(n):
            for j in range(m):                
                
                    if i >= 1 and j >=1:                        
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i >= 1 :
                        dp[i][j] = dp[i-1][j]
                    elif j >= 1:
                        dp[i][j] = dp[i][j-1] 
                    
                        
        return dp[n-1][m-1]
                    
                
        