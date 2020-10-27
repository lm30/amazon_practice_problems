class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        aptr = 0
        bptr = 0
        result = []
        
        while aptr < len(A) and bptr < len(B):
            bend = B[bptr][1]
            aend = A[aptr][1]
            maxStart = max(A[aptr][0], B[bptr][0])
            minEnd = min(aend, bend)
            
            if maxStart <= minEnd:
                result.append([maxStart, minEnd])
            aptr = aptr + 1 if aend <= bend else aptr
            bptr = bptr + 1 if aend >= bend else bptr
        
        return result