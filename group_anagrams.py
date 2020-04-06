'''
Problem 06- 06/04/2020
Given an array of strings, group anagrams together.
All inputs will be in lowercase and order of the output does not matter.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        grouped = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26                      #create a list of size 26 for all 26 letters
            for c in s:
                count[ord(c) - ord('a')] += 1     #list of values with counts of each letter
            grouped[tuple(count)].append(s)       #convert the list as tuples and use it as the hash-key
        return grouped.values()
        
