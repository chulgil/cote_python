# revese.py
#!/usr/bin/env python#3
""" 문자열 뒤집는 메서드

- 입력 "h,e,l,l,o"
- 출력 "o,l,l,e,h"

"""
from typing import List
from  utils.timeit import elapsed

@elapsed
def reverse_two_pointer(word: List[str]) -> None:
    left, right = 0, len(word) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

@elapsed
def reverse_string(word: List[str]) -> None:
    word.reverse()

@elapsed
def reverse_slicing(word: List[str]) -> None:
    word[:] = word[::-1]

word = ["문","자","열","뒤","집","는","메","서","드"]
reverse_two_pointer(word)
reverse_string(word)
reverse_slicing(word)
print(word)

