class Solution(object):
    def characterReplacement(self, s, k):
        count = defaultdict(int) 
        l = 0
        result = k
        
        for x in range(0,len(s)):
            count[s[x]] += 1
            
            if (x-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, x-l+1)
            
        return result
            
        