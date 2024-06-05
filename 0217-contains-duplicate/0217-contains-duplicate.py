class Solution(object):
    def containsDuplicate(self, nums):
        nums_dictionary = defaultdict(lambda:0)
        for x in nums:
            if nums_dictionary[x] == 1:
                return True
            nums_dictionary[x] += 1
        
        return False
        