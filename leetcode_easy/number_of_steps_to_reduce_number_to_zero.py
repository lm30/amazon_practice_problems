class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # do a proof later to see if can simplify even more
        count = 0
        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            count += 1
        
        return count