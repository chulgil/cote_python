# palindrome.py
#!/usr/bin/env python#3
""" 팰린드롬 판별 메서드

- 입력 "소주 만 병 만 주소"
- 출력 true

- 입력 "소주 한 병 만 주소"
- 출력 false

"""
import re
import collections
from typing import Deque
from Utils.timeit import elapsed


@elapsed
def del_special(word: str) -> bool:
    """한글, 영어, 숫자를 제외한 특수문제 삭제
    Args:
        word: 대상 문자열
    Returns:
        str: 특수문제를 제외한 문자열
    """
    word = word.lower()
    word = re.sub('[^ a-z0-9ㄱ-ㅣ가-힣+]', '', word)
    return word


def is_palindrome_list(word: str) -> bool:
    """리스트를 활용한 팰린드롬 판별
    Args:
        word: 대상 문자열
    Returns:
        bool: 팰린드롬이면 True 아니면 False
    """
    words = []
    word = del_special(word)
    for char in word:
        words.append(char.lower())
        while len(words) > 1:
            if words.pop(0) != words.pop():
                return False
        return True


def is_palindrome_deque(word: str)  -> bool:
    """데크를 활용한 팰린드롬 판별
    Args:
        word: 대상 문자열
    Returns:
        bool: 팰린드롬이면 True 아니면 False
    """
    words: Deque = collections.deque()
    word = del_special(word)
    for char in word:
        words.append(char.lower())
    while len(words) > 1:
        if words.popleft() != words.pop():
            return False
        return True

def is_palindrome_slicing(word:str) -> bool:
    """슬라이싱을 활용한 팰린드롬 판별
    Args:
        word: 대상 문자열
    Returns:
        bool: 팰린드롬이면 True 아니면 False
    """
    word = del_special(word)
    return word == word[::-1]

word = "소주 한 병 만 주소"

print(is_palindrome_list(word))
print(is_palindrome_deque(word))
print(is_palindrome_slicing(word))