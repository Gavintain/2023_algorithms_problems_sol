# 연속 부분 수열 합의 개수
# 문제 설명
# 철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.
# 그림.png
# 원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
# 원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ elements의 길이 ≤ 1,000
# 1 ≤ elements의 원소 ≤ 1,000
# 입출력 예
# elements	result
# [7,9,1,1,4]	18
# 입출력 예 설명
# 입출력 예 #1
# 길이가 1인 연속 부분 수열로부터 [1, 4, 7, 9] 네 가지의 합이 나올 수 있습니다.
# 길이가 2인 연속 부분 수열로부터 [2, 5, 10, 11, 16] 다섯 가지의 합이 나올 수 있습니다.
# 길이가 3인 연속 부분 수열로부터 [6, 11, 12, 17, 20] 다섯 가지의 합이 나올 수 있습니다.
# 길이가 4인 연속 부분 수열로부터 [13, 15, 18, 21] 네 가지의 합이 나올 수 있습니다.
# 길이가 5인 연속 부분 수열로부터 [22] 한 가지의 합이 나올 수 있습니다.
# 이들 중 중복되는 값을 제외하면 다음과 같은 18가지의 수들을 얻습니다.
# [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22]

import sys
sys.setrecursionlimit(10**8)
def solution(elements):
    s = set()
    n = len(elements)
    
    def recursive(mode,ppre_lst,pre_lst,trial):
        if mode == True:
            i=0
            t_lst = []
            for _ in range(n):
                tmp = 0
                for x in range(2):
                    tmp += elements[(i+x)%n]
                t_lst.append(tmp)
                i+=1
            s.update(t_lst)
            recursive(False,elements,t_lst,trial+1)
        else:
            if trial>=n-1:
                return
            else:
                i=0
                t_lst = []
                for _ in range(n):
                    tmp = 0
                    for x in range(2):
                        tmp += pre_lst[(i+x)%n]
                    tmp -= ppre_lst[(i+1)%n]
                    t_lst.append(tmp)
                    i+=1
                s.update(t_lst)
                recursive(False,pre_lst,t_lst,trial+1)
        
    s.update(elements)
    recursive(True,[],[],0)
    answer = len(s)
    
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (23.54ms, 13.3MB)
# 테스트 3 〉	통과 (57.87ms, 15.6MB)
# 테스트 4 〉	통과 (106.44ms, 20.4MB)
# 테스트 5 〉	통과 (175.02ms, 32MB)
# 테스트 6 〉	통과 (237.69ms, 33MB)
# 테스트 7 〉	통과 (313.81ms, 37.9MB)
# 테스트 8 〉	통과 (419.62ms, 43.9MB)
# 테스트 9 〉	통과 (536.11ms, 61.2MB)
# 테스트 10 〉	통과 (670.61ms, 66.7MB)
# 테스트 11 〉	통과 (221.81ms, 32.3MB)
# 테스트 12 〉	통과 (276.74ms, 33.3MB)
# 테스트 13 〉	통과 (273.33ms, 35.2MB)
# 테스트 14 〉	통과 (326.25ms, 38MB)
# 테스트 15 〉	통과 (389.87ms, 40.7MB)
# 테스트 16 〉	통과 (447.03ms, 59.3MB)
# 테스트 17 〉	통과 (474.09ms, 59.9MB)
# 테스트 18 〉	통과 (592.40ms, 61.2MB)
# 테스트 19 〉	통과 (661.74ms, 62.2MB)
# 테스트 20 〉	통과 (736.80ms, 66.8MB)

# 다른 사람 풀이. 연속된 수의 합이므로 O(n^2)에 수행가능... 간단한 구현이라 인상적.


def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (8.69ms, 13MB)
# 테스트 3 〉	통과 (20.37ms, 14.1MB)
# 테스트 4 〉	통과 (39.30ms, 18.3MB)
# 테스트 5 〉	통과 (74.58ms, 26.8MB)
# 테스트 6 〉	통과 (88.02ms, 27MB)
# 테스트 7 〉	통과 (143.09ms, 26.8MB)
# 테스트 8 〉	통과 (193.06ms, 27.6MB)
# 테스트 9 〉	통과 (214.31ms, 43.7MB)
# 테스트 10 〉	통과 (279.56ms, 43.6MB)
# 테스트 11 〉	통과 (67.51ms, 26.7MB)
# 테스트 12 〉	통과 (85.75ms, 27MB)
# 테스트 13 〉	통과 (102.77ms, 26.9MB)
# 테스트 14 〉	통과 (152.45ms, 26.8MB)
# 테스트 15 〉	통과 (169.55ms, 27MB)
# 테스트 16 〉	통과 (159.78ms, 43.5MB)
# 테스트 17 〉	통과 (188.55ms, 43.5MB)
# 테스트 18 〉	통과 (257.79ms, 43.6MB)
# 테스트 19 〉	통과 (364.93ms, 43.6MB)
# 테스트 20 〉	통과 (294.20ms, 43.6MB)