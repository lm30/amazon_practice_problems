class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        numJobs = len(jobDifficulty)
        if d > numJobs or numJobs == 0:
            return -1
        
        maxVal = collections.defaultdict(int)
        for i in range(1, numJobs + 1):
            for k in range(i):
                maxVal[(k,i)] = max(jobDifficulty[k:i])
        
        dp = [[]] * (numJobs + 1)
        for i in range(numJobs + 1):
            dp[i] = [float('inf')] * (d + 1)
        
        dp[0][0] = 0
        
        for i in range(1, numJobs + 1):
            for j in range(1, min(i + 1, d + 1)):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + maxVal[(k,i)])
        
        return dp[numJobs][d]