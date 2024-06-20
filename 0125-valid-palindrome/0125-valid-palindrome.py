class Solution(object):
    def isPalindrome(self, s):
        alphanum = ''.join(char.lower() for char in s if char.isalnum())
        return alphanum == alphanum[::-1]