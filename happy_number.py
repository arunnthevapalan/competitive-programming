'''
Problem 02 - 02/04/2020
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = [n]
        while(True):
            n = sum(int(c)**2 for c in str(n)) 
            if n==1:
                return True
            elif n in seen:
                return False
            seen.append(n)
        
