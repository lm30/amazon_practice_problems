class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # brute force
#         count = 0
        
#         for i in range(len(rating)):
#             for j in range(i, len(rating)):
#                 for k in range(j, len(rating)):
#                     if rating[i] < rating[j] < rating[k]:
#                         count += 1
#                     elif rating[i] > rating[j] > rating[k]:
#                         count += 1
#         return count
        
        greaterThan = [0] * len(rating)
        lessThan = [0] * len(rating)
        result = 0
        
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] > rating[j]:
                    lessThan[i] += 1
                elif rating[i] < rating[j]:
                    greaterThan[i] += 1
        
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] > rating[j]:
                    result += lessThan[j]
                else:
                    result += greaterThan[j]
        return result