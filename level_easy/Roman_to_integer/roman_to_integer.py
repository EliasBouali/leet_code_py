class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0

        for i, char in enumerate(s):
            if i < len(s) - 1 and d[char] < d[s[i+1]]:
                result -= d[char]
            else :
                result += d[char]

        return result 
