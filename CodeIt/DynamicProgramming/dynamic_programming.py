
"""
Dynamic Programming 의 조건
1) 최적 부분 구조 Optimal Substructure
2) 중복되는 부분 문제 Overlapping Subproblems

최적 부분 구조가 있다는 건
부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것.

한 번 계산한 결과를 버리지 말고 재활용하자. 한 번만 풀고 기억해두자

구현 방법
1) Memorization
재귀
필요한 연산만
2) Tabulation
반복문
전부 계산

공간 최적화 : 사용하는 메모리 공간을 아낄 수 있다.
current = previous + current
previous = current
"""

