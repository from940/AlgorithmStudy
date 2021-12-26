
def fib_optimized(n):
    previous, current = 0, 1

    for i in range(1, n):
        current, previous = current+previous ,current

    # 피보나치 n번째 수를 리턴한다
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))