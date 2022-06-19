"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:
    Input: s = "lEeTcOdE"
    Output: "E"
    Explanation:
    The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:
    Input: s = "arRAzFif"
    Output: "R"
    Explanation:
    The letter 'R' is the greatest letter to appear in both lower and upper case.
    Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:
    Input: s = "AbCdEfGhIjK"
    Output: ""
    Explanation:
    There is no letter that appears in both lower and upper case.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase and uppercase English letters.
"""


def greatestLetter(s):
    greatest_letter = ''
    uppercase_letters = set()
    lowercase_letters = set()
    letter_set = set(s)
    for letter in letter_set:
        if letter.isupper():
            uppercase_letters.add(letter)
        else:
            lowercase_letters.add(letter.upper())
    intersectio_letters = uppercase_letters & lowercase_letters
    if len(intersectio_letters) != 0:
        greatest_letter = max(list(intersectio_letters))
    return greatest_letter

s = "lEeTcOdE"
print(greatestLetter(s))
s = "arRAzFif"
print(greatestLetter(s))
s = "AbCdEfGhIjK"
print(greatestLetter(s))