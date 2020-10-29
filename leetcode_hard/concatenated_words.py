class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        result = set()
        
        prewords = set()
        
        for word in words:
            if self.check(word, prewords):
                result.add(word)
            prewords.add(word)
        
        return result
    
    def check(self, target, words):
        if not words:
            return False
        
        dp = [False] * (len(target) + 1)
        dp[0] = True
        for i in range(len(target) + 1):
            for j in range(i):
                if dp[j] and target[j : i] in words:
                    dp[i] = True
                    break
        return dp[-1]