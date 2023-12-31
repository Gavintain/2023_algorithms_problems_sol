# 과일 장수
# 문제 설명
# 과일 장수가 사과 상자를 포장하고 있습니다. 사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 사과 한 상자의 가격은 다음과 같이 결정됩니다.

# 한 상자에 사과를 m개씩 담아 포장합니다.
# 상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
# 과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)

# 예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.

# (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8
# 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ k ≤ 9
# 3 ≤ m ≤ 10
# 7 ≤ score의 길이 ≤ 1,000,000
# 1 ≤ score[i] ≤ k
# 이익이 발생하지 않는 경우에는 0을 return 해주세요.
# 입출력 예
# k	m	score	result
# 3	4	[1, 2, 3, 1, 2, 3, 1]	8
# 4	3	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	33
# 입출력 예 설명
# 입출력 예 #1

# 문제의 예시와 같습니다.
# 입출력 예 #2

# 다음과 같이 사과 상자를 포장하여 모두 팔면 최대 이익을 낼 수 있습니다.
# 사과 상자	가격
# [1, 1, 2]	1 x 3 = 3
# [2, 2, 2]	2 x 3 = 6
# [4, 4, 4]	4 x 3 = 12
# [4, 4, 4]	4 x 3 = 12
# 따라서 (1 x 3 x 1) + (2 x 3 x 1) + (4 x 3 x 2) = 33을 return합니다.

from collections import Counter,defaultdict
def solution(k, m, score):
    iter = Counter(score)
    dict = defaultdict(int)
    for key in iter.keys():
        dict[key] = iter[key]

    keylst = sorted(list(dict.keys()),reverse = True)
    task = len(score)//m
    left_over=0
    answer=0
    for key in keylst:
        bucket = left_over+dict[key]
        boxs = bucket//m
        left_over = bucket%m
        
        if boxs>=task:
            answer+=key*(task)*m
            break
        else:
            answer+=key*boxs*m
            task-=boxs
    return answer

# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.1MB)
# 테스트 6 〉	통과 (3.14ms, 10.5MB)
# 테스트 7 〉	통과 (3.40ms, 10.7MB)
# 테스트 8 〉	통과 (0.49ms, 10.3MB)
# 테스트 9 〉	통과 (4.67ms, 10.5MB)
# 테스트 10 〉	통과 (4.69ms, 10.5MB)
# 테스트 11 〉	통과 (47.82ms, 18.7MB)
# 테스트 12 〉	통과 (58.07ms, 18.6MB)
# 테스트 13 〉	통과 (55.77ms, 18.7MB)
# 테스트 14 〉	통과 (42.97ms, 18.6MB)
# 테스트 15 〉	통과 (48.22ms, 18.6MB)
# 테스트 16 〉	통과 (0.05ms, 10.4MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.04ms, 10.4MB)
# 테스트 19 〉	통과 (0.05ms, 10.2MB)
# 테스트 20 〉	통과 (0.04ms, 10.2MB)
# 테스트 21 〉	통과 (0.03ms, 10.1MB)
# 테스트 22 〉	통과 (0.04ms, 10.2MB)
# 테스트 23 〉	통과 (0.03ms, 10.2MB)
# 테스트 24 〉	통과 (0.05ms, 10.2MB)


## 아래 풀이는 시간초과

# def solution(k, m, score):
#     score.sort()
#     new_score = [x for x in score]
#     answer=0
#     l = len(new_score)
#     while(l>=m):
#         answer+=new_score[-m]*m
#         new_score = new_score[:(l-m)]
#         l -= m
#     return answer


## 다른 사람 풀이. 한줄에 풀린다... 하지만 내 풀이가 대부분의 테스트케이스에서 더 빠르다!
## 그 이유로 크게 보면 첫 번쨰는 score 전체를 정렬하느냐 안하느냐에 있다. 나는 정렬(최소 O(nlogn))하지 않고 카운팅(O(n))만 한다.
## 두 번째는 score에 추가로 접근하는 정도에 있다. 나는 key 갯수 만큼 접근하지만 한줄 알고리즘은 매 배수만큼 접근한다.
## 사실 score의 각 원소들이 서로 중복되지 않을수록 내 알고리즘은 오래걸리게 된다. 
## 그럼에도 불구하고 내 알고리즘은 상수 n의 시간복잡도이고 
## 한줄 알고리즘은 nlogn (정렬떄문에) 시간복잡도여서 항상 내 알고리즘이 더 빠르다고 보면 된다. 히히


# def solution(k, m, score):
#     return sum(sorted(score)[len(score)%m::m])*m

def solution(k, m, score):
    return sum(sorted(score,reverse=True)[m-1::m])*m
        
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (4.72ms, 11.3MB)
테스트 7 〉	통과 (8.57ms, 11.4MB)
테스트 8 〉	통과 (0.96ms, 10.2MB)
테스트 9 〉	통과 (5.65ms, 11.4MB)
테스트 10 〉	통과 (5.72ms, 11.2MB)
테스트 11 〉	통과 (87.68ms, 29.3MB)
테스트 12 〉	통과 (77.47ms, 29.2MB)
테스트 13 〉	통과 (82.30ms, 29.2MB)
테스트 14 〉	통과 (76.01ms, 29.2MB)
테스트 15 〉	통과 (76.33ms, 29.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10MB)
테스트 21 〉	통과 (0.00ms, 10.1MB)
테스트 22 〉	통과 (0.00ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10MB)
