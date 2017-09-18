class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        total = 10
        pre = 9
        availableNumber = 9
        while n > 1:
            pre *= availableNumber
            availableNumber -= 1
            n -= 1
            total += pre
        return total