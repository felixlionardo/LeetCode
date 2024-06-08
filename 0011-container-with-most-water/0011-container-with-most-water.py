class Solution(object):
    def maxArea(self, height):
        l,r = 0, len(height)-1
        max_area = 0
        
        while l<r:
            h = min(height[l], height[r])
            
            curr_area = h*(r-l)
            max_area = max(max_area, curr_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
            
        