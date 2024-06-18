class Solution(object):
    def maxProduct(self, nums):
        maxnumber = max(nums)
        currmax, currmin = 1,1
        
        for x in nums:
            
            if x == 0:
                currmax, currmin = 1,1
                continue
            
            tmp = currmax*x
            currmax = max(currmax*x, currmin*x, x)
            currmin = min(tmp, currmin*x, x)
            
            maxnumber = max(maxnumber, currmax)
        
        return maxnumber
        