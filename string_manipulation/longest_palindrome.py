# longest_palindrome.py
#!/usr/bin/env python#3
"""가장 긴 팰린드롬 부분 분자열 출력
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

https://leetcode.com/problems/longest-palindromic-substring/
"""
def longest_palindrome(word: str) -> str:

    if len(word) < 2 or word == word[::-1]:
        return word

    def expend(left: int, right: int) -> str:
        while left >= 0 and right < len (word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left+1: right]

    result = ''
    for i in range(len(word) - 1):
        result = max(result,
                     expend(i, i + 1),
                     expend(i, i + 2),
                     key=len)
    return result






















#
#
#
# def longest_palindrome(word: str) -> str:
#
#     if len(word) < 2 or word == word[::-1]:
#         return word
#
#     def expand(left: int, right: int) -> str:
#         while left >=0 and right < len(word) and word[left] == word[right]:
#             left -= 1
#             right += 1
#         return word[left + 1:right]
#
#     result = ''
#
#     for i in range(len(word) - 1):
#         result = max(result,
#                      expand(i, i + 1),
#                      expand(i, i + 2),
#                      key=len)
#
#     return result

word = "worddrowa"
print(longest_palindrome(word))

