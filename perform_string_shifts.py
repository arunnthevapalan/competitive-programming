'''
Problem 14 - 14/04/2020
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
    direction can be 0 (for left shift) or 1 (for right shift). 
    amount is the amount by which string s is to be shifted.
    A left shift by 1 means remove the first character of s and append it to the end.
    Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
'''
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s)==1:
            return s
        operation = 0
        for op in shift:
            if op[0]==1:
                operation+=op[1]
            else: operation -= op[1]
        operation = operation % len(s) #ensure the operation not higher than the len(s)
        if operation == 0: return s
        elif operation >0: return (s[len(s)-operation:]+s[0:len(s)-operation] )
        else: return (s[-operation:]+s[0:-operation])
