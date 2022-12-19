'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)
        count = 0
        while i > 0:
            i -= 1
            if s[i] == " " and count != 0:
                return count
            elif s[i] != " ":
                count += 1
        return count


# Split string on spaces
# Get length of index -1
# Problem: Does not account for 2 trailing slashes
# Solution: Count backwards through string each character that is not equal to " "
# If it encounters a space & count is still 0, continue (this accounts for double spaces at the end)
# Otherwise, the word has finished, and count should be returned
