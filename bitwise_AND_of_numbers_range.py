'''
Problem 23 - 23/04/2020
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example:
Input: [5,7]
Output: 4
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        #find the common left header (or, same prefix) of m and n
        while m != n:
            m >>= 1 #shift to right by 1 bit
            n >>= 1
            shift += 1
        #then shift back to left to form the final result
        #(the remaining bits are not the same, so definitely result in 0 after AND)
        return m << shift
        
