"""
Given two integers num and k, consider a set of positive integers with the following properties:

The units digit（个位数） of each integer is k.
The sum of the integers is num.
Return the minimum possible size of such a set, or -1 if no such set exists.

Note:
    The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
    The units digit of a number is the rightmost digit of the number.


Example 1:
    Input: num = 58, k = 9

Output: 2
    Explanation:
    One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
    Another valid set is [19,39].
    It can be shown that 2 is the minimum possible size of a valid set.

Example 2:
    Input: num = 37, k = 2
    Output: -1
    Explanation: It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.

Example 3:
    Input: num = 0, k = 7
    Output: 0
    Explanation: The sum of an empty set is considered 0.

Constraints:
    0 <= num <= 3000
    0 <= k <= 9
"""


def minimumNumbers(num, k):
    """
    :type num: int
    :type k: int
    :rtype: int
    """

    if num == 0:
        return 0

    # 求的个位数为k的数字相加后，和的所有可能的个位数，及得到该个位数的最小相加次数
    possible_units_digit = dict()
    digit = k
    size = 1
    while True:
        units_digit = str(digit)[-1]
        if units_digit in possible_units_digit:
            break
        else:
            possible_units_digit[units_digit] = size
        digit += k
        size += 1

    # 输入数字的个位数（目标个位数）
    units_digit = str(num)[-1]
    # 最小集合size
    min_size = -1
    # 判断"目标个位数" 是否在 "可能个位数"集合中
    if units_digit in possible_units_digit:
        size = possible_units_digit[units_digit]
        # 确保输入数 大于等于 最小的可能个位数 * 最小相加次数，避免 num=17，k=9的情况
        if num >= k * size:
            min_size = size

    return min_size


num = 58
k = 9
print(minimumNumbers(num, k))

num = 37
k = 2
print(minimumNumbers(num, k))

num = 0
k = 7
print(minimumNumbers(num, k))

num = 27
k = 9
print(minimumNumbers(num, k))

num = 10
k = 8
print(minimumNumbers(num, k))