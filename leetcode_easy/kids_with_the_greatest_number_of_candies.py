class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = [False] * len(candies)
        
        # greatest number of candies held by a kid in the list
        greatestNumberCandies = max(candies)
        
        for index in range(len(candies)):
            if candies[index] + extraCandies >= greatestNumberCandies:
                result[index] = True
        
        return result