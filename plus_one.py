'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num = ''.join(str(n) for n in digits)
        return (int(n) for n in str(int(str_num) + 1))

# First, use list comprehension to convert all integers in digits into strings
# Then, join them together for variable str_num
# Take str_num and convert it into an integer, then increment by 1
# We convert this integer into a string, so it is iterable
# Then, using list comprehension we convert each string number into an integer
