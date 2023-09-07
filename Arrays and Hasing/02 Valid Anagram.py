"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

s and t consist of lowercase English letters.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false

Solution:
    Create two Hash Maps
    Add each char to their HM
    Look through both Hash Maps to check count
    Return True or False

Time & Space: O(n) or O(s + t)

Other Solution:
    Sorth both strings, then compare
        return sorted(s) == sorted(t)
    This will reduce Space to O(1)
    Sorting can take up a lot of time    
    Might have to setup a sort alg    
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
        # or just 
        # return countS == countT