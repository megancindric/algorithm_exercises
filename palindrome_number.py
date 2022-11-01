# Given an integer x, return true if x is a palindrome
# And return false otherwise
# Negative numbers are not palindromes: -121 would become 121-
from math import ceil


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        for i in range((ceil(len(str_x)/2))+1):
            if str_x[i] != str_x[-1-i]:
                return False

        return True


# Loop through string version of integer
    # From 0 up to length of string version of integer / 2
    # Wrap all that in ceil(), to account for odd number of digits
    # Use range for loop, and count to that value, + 1
    # Use index & negative index to compare digits one at a time
    # If they're not equal, return false
    # If loop completes, return true

 # 12321
    # 2.5 -> round up

# Above solution breaks on LeetCode.  Pasting alternative solution I created below:
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[-1-i]:
                return False

        return True
'''
