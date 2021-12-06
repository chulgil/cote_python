# timeit.py
#!/usr/bin/env python#3
""" 시간관련 메서드

@elapsed
    print 함수 수행시간: %f 초

ex) 반복 테스트시 예
    import timeit
    print(timeit.timeit("method()", number=100, globals=globals()))

"""

import functools
import time

def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper
