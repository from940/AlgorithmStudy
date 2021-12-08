
# n번째 피보나치 수 리턴
def fib(n) :
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# test
for i in range(1, 11):
    print(fib(i))