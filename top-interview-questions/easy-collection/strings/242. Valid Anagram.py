"""
LeetCode Problem: 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise

Link: https://leetcode.com/problems/valid-anagram/description/
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == len(t):
            count_s = {}
            count_t = {}
            for char in s:
                count_s[char] = count_s.get(char, 0) + 1
            for char in t:
                count_t[char] = count_t.get(char, 0) + 1
            if count_s == count_t:
                return True
            else:
                return False
        
        
