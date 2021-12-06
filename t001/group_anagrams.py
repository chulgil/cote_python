# group_anagrams.py
#!/usr/bin/env python#3
""" 문자열배열을 애너그램 단위로 그룹핑
애너그램은 일종의 언어유희로 문전박대 -> 대박전문 과 같은 의미이다.
같은 문자를 가진 배열을 그룹핑한다.

Example 1:

Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

https://leetcode.com/problems/group-anagrams/
"""
import collections
import re
from typing import List
from utils.timeit import elapsed

@elapsed
def group_anagrams(words: List[str]) -> List[List[str]]:
    #keyError를 방지하기위해 항상 디폴트를 생성한다.
    anagrams = collections.defaultdict(list)

    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

words = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(words))