class Solution:
    def climbStairs(self, n: int) -> int:

        return self.climb(0,n,{})


    def climb(self,k,n, dp):
        if k == n:
            return 1
        elif k > n:
            return 0
        else:
            if k + 1 in dp and k+2 in dp:
                return dp[k+1] + dp[k+2]
            elif k + 1 in dp:
                dp[k+2] = self.climb(k+2,n,dp)
            elif  k+2 in dp:
                dp[k+1] = self.climb(k+1,n,dp)
            else:
                dp[k+2] = self.climb(k+2,n,dp)
                dp[k+1] = self.climb(k+1,n,dp)
            return dp[k+1] + dp[k+2]

class Solution:
    def climbStairs(self, n: int) -> int:

        one = 1
        two = 1

        for i in range(n-1):
            tmp = two
            two += one
            one = tmp
        return two