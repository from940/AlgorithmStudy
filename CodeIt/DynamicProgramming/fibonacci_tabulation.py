"""
2) Tabulation
테이블 방식으로 구하자
상향식 접근
"""

def fib_tab(n):
    cache = {}
    i = 1
    while i <= n:
        if i <= 2:
            cache[i] = 1
        else:
            cache[i] = cache[i - 1] + cache[i - 2]
        i += 1
    return cache[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))