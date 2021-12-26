
"""
1) Memorization
재귀 사용하기
"""

def fib_memo(n, cache):
    i = 1
    while i <= n :
        if i <= 2 :
            cache[i] = 1
        else :
            cache[i] = cache[i-1] + cache[i-2]
        i+=1
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))