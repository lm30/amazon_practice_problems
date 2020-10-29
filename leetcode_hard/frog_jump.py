class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 2 and stones[0] + 1 != stones[1]:
            return False
        
        leapDict = {}
        for stone in stones: 
            leapDict[stone] = set()
        
        leapDict[0].add(0)

        for stone in stones:
            
            prevHops = leapDict[stone]
            for prevHop in prevHops:
                for hop in [prevHop - 1, prevHop, prevHop + 1]:
                    if hop <= 0: 
                        continue
                    if stone + hop in leapDict:
                        leapDict[stone + hop].add(hop)
        return len(leapDict[stones[-1]]) > 0  