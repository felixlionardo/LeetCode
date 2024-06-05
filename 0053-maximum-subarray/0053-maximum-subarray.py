class Solution(object):
    def maxSubArray(self, nums):
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        largest_sum = nums[0]
        current_sum = nums[0]
        for x in nums[1:]:
            if current_sum < 0:
                current_sum = 0
            current_sum = current_sum + x
            largest_sum = max(largest_sum, current_sum)
            
        return largest_sum
            
        