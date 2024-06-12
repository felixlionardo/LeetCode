class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        substring = ""
        for x in range(0,len(s)):
            if s[x] in substring:
                substring = substring[substring.find(s[x])+1:]
            substring += s[x]
            longest = max(longest, len((substring)))
        
        return longest
                
        