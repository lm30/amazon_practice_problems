class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """        
        letterReference = {}
        for i in range(len(S)):
            if S[i] in letterReference:
                letterReference[S[i]][1] = i
            else:
                letterReference[S[i]] = [i, i]
        
        letterRanges = letterReference.values()
        letterRanges.sort()
        
        result = []
        start = letterRanges[0][0]
        end = letterRanges[0][1]
        letterRanges.pop(0)
        
        while letterRanges:
            if letterRanges[0][0] > start and letterRanges[0][0] < end:
                if letterRanges[0][1] > end:
                    end = letterRanges[0][1]
            else:
                result.append(end - start + 1)
                start = letterRanges[0][0]
                end = letterRanges[0][1]
            letterRanges.pop(0)
        
        result.append(end - start + 1)
        return result