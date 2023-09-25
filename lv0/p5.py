

# 문제 설명
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# sides의 원소는 자연수입니다.
# sides의 길이는 2입니다.
# 1 ≤ sides의 원소 ≤ 1,000
# 입출력 예
# sides	result
# [1, 2]	1
# [3, 6]	5
# [11, 7]	13

def solution(sides):
    a = max(sides)
    b = min(sides)
    if a == b:
        return a+b-1
    else:
        return 2*b-1

# 수학 문제는 수식을 써서 증명하는 과정을 거치는 것이 확실한 답을 찾는 방법인 것 같다.
# else 케이스의 경우, a>z>a-b 와 a+b>z>a 를 만족하는 z는 2b>z>0 이므로 2b-1 이다.