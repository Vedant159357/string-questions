class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) #maps characters to their frequency
        
        bucket = defaultdict(list) #maps frequency to list of characters which have it 
        #freq -> char

        for char,count in count.items():
            bucket[count].append(char)

        res = []

        for i in range(len(s),0,-1): #decreasing order to print the character with highest frequency first
            for c in bucket[i]: #iterating through the characters which got mapped by their respective frequency
                res.append(c * i)

        return "".join(res)
                
