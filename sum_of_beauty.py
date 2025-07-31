from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = Counter() #creates a hashmap storing frequencies
            for j in range(i,len(s)):
                freq[s[j]] += 1
                total_beauty += max(freq.values()) - min(freq.values()) #subtracting the least freq from the most freq

        return total_beauty
