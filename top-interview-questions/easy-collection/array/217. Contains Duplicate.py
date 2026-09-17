"""
LeetCode Problem: 17. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Link: https://leetcode.com/problems/contains-duplicate/description/
"""

class Solution(object):
    def containsDuplicate(self, nums):
        duplicates = set()
        seen = set()
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False
