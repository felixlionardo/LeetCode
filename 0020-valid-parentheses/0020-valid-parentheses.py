class Solution(object):
    def isValid(self, s):
        dictionary = {']':'[', '}' : '{', ')' : '('}
        stack = []
        
        for x in s:
            if x in dictionary:
                if stack and stack[-1] == dictionary[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
                
        if stack:
            return False
        else:
            return True
        