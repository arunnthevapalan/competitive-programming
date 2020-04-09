'''
Problem 09 - 09/04/2020
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=[]
        t=[]
        for c in S:
            if c=='#':
                if s: s.pop()
            else: s.append(c)
        for c in T:
            if c=='#':
                if t: t.pop()
            else: t.append(c)
        return s==t
