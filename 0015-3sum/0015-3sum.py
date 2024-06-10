class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        
        for x in range(0,len(nums)-2):
            left = x + 1
            right = len(nums)-1
            
            if nums[x-1] == nums[x] and x > 0:
                continue
            
            while left<right:
                current_sum = nums[x]+nums[left]+nums[right]
                if current_sum == 0:
                    result.append([nums[x], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result
            
        