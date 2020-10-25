from collections import Counter
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jewelRef = set(J)
        jewelCount = 0
        
        # option A
#         for stone in S:
#             if stone in jewelRef:
#                 jewelCount += 1

        # option B uses Counter and faster according to leetcode
        stoneCounter = Counter(S)
        for stone in stoneCounter.most_common():
            if stone[0] in jewelRef:
                jewelCount += stone[1]
        
        return jewelCount