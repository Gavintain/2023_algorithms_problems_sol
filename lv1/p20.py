# [1차] 다트 게임
# 문제 설명
# 다트 게임
# 카카오톡에 뜬 네 번째 별! 심심할 땐? 카카오톡 게임별~

# Game Star

# 카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
# 갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T

# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
# 출력 형식
# 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# 예) 37

# 입출력 예제
# 예제	dartResult	answer	설명
# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
# 2	1D2S#10S	9	12 + 21 * (-1) + 101
# 3	1D2S0T	3	12 + 21 + 03
# 4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	1T2D3D#	-4	13 + 22 + 32 * (-1)
# 7	1D2S3T*	59	12 + 21 * 2 + 33 * 2
# 해설 보러가기

## 정규식을 안써서 매우 복잡하게 풀었다.

def solution(dartResult):
    answer = 0
    base = ''
    option = False
    toggle = False
    chr_dir = {'S':1,'D':2,'T':3}
    previous = 0
    
    for chr in dartResult:

        ## 문자열의 요소가 알파벳인 경우
        if chr.isupper() or chr.islower():
            ## 일련의 숫자를 다 찾았으므로 토글을 누른다.
            toggle = True
            base = int(base) ** chr_dir[chr]

        ## 문자열의 요소가 알파벳이 아닌 경우
        else:
            if chr =='*':
                option = True
            elif chr == '#':
                base *= -1
            
            ## 문자열의 요소가 숫자인 경우
            else:

                ## 일련의 숫자를 찾는 중인 경우
                if not toggle:
                    base += chr
                
                ## 일련의 숫자를 다 찾은 경우
                else:
                    ## 토글 초기화
                    toggle = False

                    if option:
                        answer += previous + base*2
                        option = False
                        previous = int(base*2)
                    else:
                        answer += int(base)
                        previous = int(base)
                    base = chr
        
    if option:
        answer += previous + int(base)*2
        option = False
    else:
        answer += int(base)

    return answer

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.1MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.4MB)
# 테스트 12 〉	통과 (0.03ms, 10.1MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.1MB)
# 테스트 16 〉	통과 (0.03ms, 10.5MB)
# 테스트 17 〉	통과 (0.03ms, 10.1MB)
# 테스트 18 〉	통과 (0.03ms, 10.1MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.03ms, 10.2MB)
# 테스트 21 〉	통과 (0.03ms, 10.4MB)
# 테스트 22 〉	통과 (0.03ms, 10.4MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (0.02ms, 10.2MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
# 테스트 26 〉	통과 (0.02ms, 10.2MB)
# 테스트 27 〉	통과 (0.03ms, 10.3MB)
# 테스트 28 〉	통과 (0.03ms, 10.2MB)
# 테스트 29 〉	통과 (0.03ms, 10.2MB)
# 테스트 30 〉	통과 (0.03ms, 10.3MB)
# 테스트 31 〉	통과 (0.02ms, 10.1MB)
# 테스트 32 〉	통과 (0.03ms, 10.1MB)


## 다른 사람 풀이. 정규식을 활용했다. 직관적이고 깔끔하다...
## 하지만 내 알고리즘이 5배 이상 더 빠르게 문제를 풀었다.
## 정규식을 적용하는 finall의 시간 복잡도는 O(nm)으로 볼 수 있다.
## 즉 내 알고리즘의 시간 복잡도는 대강 n 이라면, 정규식을 이용한 알고리즘은 nm+m 이다.
## m = 3 을 고려하면 정규식을 이용한 알고리즘은 3(n+1)
## n = 9 를 대입하여 최종적으로 비교하면 9 vs 30, 대략 3.3배 빨라야 한다. 하지만 그 이상으로 빠른데,
## 테스트 케이스 14의 경우 18배 이상 빠르다.. 왜 그럴까?
## 아래 코드에서 테스트해본 결과, findall에서 걸린 시간보다 dart 원소를 순회하는 부분에서 더 시간이 걸렸다.

import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    ## 정규식을 컴파일
    p = re.compile('(\d+)([SDT])([*#]?)')
    ## dartResult에 정규식과 같은 원소 찾기
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


테스트 1 〉	통과 (0.16ms, 10.2MB)
테스트 2 〉	통과 (0.18ms, 10.4MB)
테스트 3 〉	통과 (0.16ms, 10.4MB)
테스트 4 〉	통과 (0.20ms, 10.3MB)
테스트 5 〉	통과 (0.17ms, 10.4MB)
테스트 6 〉	통과 (0.16ms, 10.4MB)
테스트 7 〉	통과 (0.15ms, 10.4MB)
테스트 8 〉	통과 (0.16ms, 10.3MB)
테스트 9 〉	통과 (0.15ms, 10.3MB)
테스트 10 〉	통과 (0.16ms, 10.4MB)
테스트 11 〉	통과 (0.16ms, 10.5MB)
테스트 12 〉	통과 (0.15ms, 10.5MB)
테스트 13 〉	통과 (0.16ms, 10.3MB)
테스트 14 〉	통과 (0.36ms, 10.3MB)
테스트 15 〉	통과 (0.16ms, 10.4MB)
테스트 16 〉	통과 (0.15ms, 10.3MB)
테스트 17 〉	통과 (0.29ms, 10.3MB)
테스트 18 〉	통과 (0.18ms, 10.3MB)
테스트 19 〉	통과 (0.22ms, 10.2MB)
테스트 20 〉	통과 (0.23ms, 10.3MB)
테스트 21 〉	통과 (0.16ms, 10.3MB)
테스트 22 〉	통과 (0.30ms, 10.4MB)
테스트 23 〉	통과 (0.15ms, 10.4MB)
테스트 24 〉	통과 (0.17ms, 10.3MB)
테스트 25 〉	통과 (0.15ms, 10.4MB)
테스트 26 〉	통과 (0.18ms, 10.2MB)
테스트 27 〉	통과 (0.15ms, 10.4MB)
테스트 28 〉	통과 (0.16ms, 10.4MB)
테스트 29 〉	통과 (0.16ms, 10.3MB)
테스트 30 〉	통과 (0.15ms, 10.3MB)
테스트 31 〉	통과 (0.16ms, 10.3MB)
테스트 32 〉	통과 (0.15ms, 10.3MB)


# import re
# import time

# stime = time.perf_counter()
# for x in [1,2,3,4,5,6,7,8,9]:
#     pass
# etime = time.perf_counter()
# unit = etime-stime

# def solution1(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     stime = time.perf_counter()
#     dart = p.findall(dartResult)
#     etime = time.perf_counter()
#     print('findall time:',round((etime-stime)/unit,3))
#     stime = time.perf_counter()
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
#     etime = time.perf_counter()
#     print('dart loop time:',round((etime-stime)/unit,3))
#     answer = sum(dart)

#     return answer


# def solution2(dartResult):
#     answer = 0
#     base = ''
#     option = False
#     toggle = False
#     chr_dir = {'S':1,'D':2,'T':3}
#     previous = 0

#     stime = time.perf_counter()
#     for chr in dartResult:

#         ## 문자열의 요소가 알파벳인 경우
#         if chr.isupper() or chr.islower():
#             ## 일련의 숫자를 다 찾았으므로 토글을 누른다.
#             toggle = True
#             base = int(base) ** chr_dir[chr]

#         ## 문자열의 요소가 알파벳이 아닌 경우
#         else:
#             if chr =='*':
#                 option = True
#             elif chr == '#':
#                 base *= -1
            
#             ## 문자열의 요소가 숫자인 경우
#             else:

#                 ## 일련의 숫자를 찾는 중인 경우
#                 if not toggle:
#                     base += chr
                
#                 ## 일련의 숫자를 다 찾은 경우
#                 else:
#                     ## 토글 초기화
#                     toggle = False

#                     if option:
#                         answer += previous + base*2
#                         option = False
#                         previous = int(base*2)
#                     else:
#                         answer += int(base)
#                         previous = int(base)
#                     base = chr
        
#     if option:
#         answer += previous + int(base)*2
#         option = False
#     else:
#         answer += int(base)

#     etime = time.perf_counter()
#     print('s2 time:',round((etime-stime)/unit,3))
#     return answer

# dartResult = '1S*2T*3S'
# solution1(dartResult)
# solution2(dartResult)
