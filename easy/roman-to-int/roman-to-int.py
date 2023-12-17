class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        d = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M':1000}
        i = 0
        while i < len(s):
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                result += (d[s[i+1]] - d[s[i]])
                i += 2
            else:
                result += d[s[i]]
                i += 1
        return result