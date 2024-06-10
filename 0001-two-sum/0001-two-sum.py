class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for x in range(0,len(nums)):
            complement = target - nums[x]
            if complement in numMap:
                return [numMap[complement], x]
            numMap[nums[x]] = x
        return []