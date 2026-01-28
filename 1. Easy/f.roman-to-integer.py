class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1, 
            'V': 5, 
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            current_value = values[s[i]]
            if i + 1 < len(s):
                next_value = values[s[i+1]]
                if next_value <= current_value:
                    total += current_value
                else:
                    total -= current_value
            else:
                total += current_value
        return total
