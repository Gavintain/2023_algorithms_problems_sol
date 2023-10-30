# N개의 최소공배수
# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 입출력 예
# arr	result
# [2,6,8,14]	168
# [1,2,3]	6

def solution(arr):
    lcm_lst = [1]
    for num in arr:
        x= num
        lcm=2
        while(True):
            if lcm>x:
                break
            else:
                if x%lcm ==0:
                    if not lcm in lcm_lst:
                        lcm_lst.append(lcm) 
                    x = x//lcm
                    lcm = 2
                else:
                    lcm+=1
    arr.sort()
    base = 1
    for num in lcm_lst:
        base *=num

    new_base= base
    y=2
    while(any(new_base%num for num in arr)):
        new_base=base*y
        y+=1
    
    return new_base

## 다른 사람 풀이. gcd 함수를 사용했으나 문제가 개편되면서 사용할 수 없게 됨. 현재까진 나의 풀이가
## 가장 만족스럽다.


# from fractions import gcd
# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer


