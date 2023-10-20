# 문제 설명
# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
# 입출력 예
# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# 입출력 예 설명
# 예제 #1

# 문제에 나온 예와 같습니다.

# 예제 #2

# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.

# ※ 공지 - 2023년 4월 21일 문제 지문이 리뉴얼되었습니다.

## 기존 풀이

# from collections import deque
# def solution(priorities, location):
#     deq = deque(priorities)
#     ldeq = deque([i for i in range(0,len(priorities))])
#     count = 0
#     while(len(deq)>0):
#         out = deq.popleft()
#         lout = ldeq.popleft()
#         if len(deq)<1:
#             m = out
#         else:
#             m = max(deq)
#         if out<m:
#             deq.append(out)
#             ldeq.append(lout)
#         else:
#             count+=1
#             if lout == location:
#                 return count
#             else:
#                 pass
#     return count


## 다른 사람 풀이. 
## Any 함수로 Max 함수 부분을 대체하면 약간의 시간을 세이브 할 수 있는 것을 배웠다. 또 enumerate를 활용하지 못했던 부분을 보충했다.

from collections import deque
def solution(priorities, location):
    
    deq = deque([(i,p) for i,p in enumerate(priorities)])
    count = 0
    while(len(deq)>0):
        out = deq.popleft()
        if any(out[1]<x[1] for x in deq):
            deq.append(out)
        else:
            count+=1
            if out[0] == location:
                return count
            else:
                pass
    return count