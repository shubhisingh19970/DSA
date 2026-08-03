class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        valList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result = ''
        
        for i in range(len(valList)):
            if num >= valList[i]:
                count = num // valList[i]
                result += symList[i] * count
                num %= valList[i]
        
        return result