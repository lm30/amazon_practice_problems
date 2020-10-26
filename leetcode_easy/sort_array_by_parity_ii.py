class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [0] * len(A)
        index = 0
        evenIndex = 0
        oddIndex = 1
        
        while evenIndex < len(A) - 1 or oddIndex < len(A):
            if A[index] % 2 == 1:
                result[oddIndex] = A[index]
                oddIndex += 2
            else:
                result[evenIndex] = A[index]
                evenIndex += 2
            index += 1
        
        return result