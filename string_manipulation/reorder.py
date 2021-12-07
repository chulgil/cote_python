# reorder.py
#!/usr/bin/env python#3
""" 로그파일 재정렬

    0. 식별자는 문자열의 가장 앞부분
    1. 문자가 숫자 보다 앞에 위치
    2. 문자와 숫자는 입력 순으로 정렬
    3. 내용이 같으면 식별자 기준 정렬

입력: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
출력: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List


def reorder_log(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 첫번째 인자를 기준으로 오름차순으로 정렬 : art can
    # 두번째 인자를 기분으로 오름차수능로 정렬 : let1
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(logs)
logs = reorder_log(logs)
print(logs)
