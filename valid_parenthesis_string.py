'''
Problem 16 - 16/04/2020
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. 
We define the validity of a string by these rules:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.
    string size would be in the range of [0,100]

Example:
Input: "(*))"
Output: True
'''
#Approach - initialize 2 stack and pop only if indexes follow order
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, c in enumerate(s):
            if c == '*':
                star.append(i)
            elif c=='(':
                stack.append(i)
            elif c==')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else: return False
                
        while star and stack:
            if (stack[-1] < star[-1]):
                stack.pop()
                star.pop()
            else: break
        return len(stack)==0
    
#approach 2 , count * as left parathesis once, as right paranthesis next
class Solution:
    def checkValidString(self, s: str) -> bool:
            lo = 0
            hi = 0;
            for c in s:
                lo += 1 if c == '(' else -1
                hi += 1 if c != ')' else -1
                if (hi < 0) :
                    break
                lo = max(lo, 0);

            return lo == 0;
