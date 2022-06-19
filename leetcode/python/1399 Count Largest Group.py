"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.

Example 1:
    Input: n = 13
    Output: 4
    Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
    [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:
    Input: n = 2
    Output: 2
    Explanation: There are 2 groups [1], [2] of size 1.

Example 3:
    Input: n = 15
    Output: 6

Example 4:
    Input: n = 24
    Output: 5

Constraints:
    1 <= n <= 10^4
"""

def countLargestGroup(n):
    groups = dict()
    for i in range(1, n + 1):
        num = list(str(i))
        sum = 0
        for digit in num:
            sum += int(digit)
        if sum not in groups:
            groups[sum] = [i]
        else:
            groups[sum].append(i)

    num_of_largest_group = 0
    size_of_largest_group = 0

    for group in groups:
        l = len(groups[group])
        if l > size_of_largest_group:
            size_of_largest_group = l
            num_of_largest_group = 1
        elif l == size_of_largest_group:
            num_of_largest_group += 1
    return num_of_largest_group

print(countLargestGroup(24))
