# 리코쳇 로봇
# 문제 설명
# 리코쳇 로봇이라는 보드게임이 있습니다.

# 이 보드게임은 격자모양 게임판 위에서 말을 움직이는 게임으로, 시작 위치에서 목표 위치까지 최소 몇 번만에 도달할 수 있는지 말하는 게임입니다.

# 이 게임에서 말의 움직임은 상, 하, 좌, 우 4방향 중 하나를 선택해서 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것을 한 번의 이동으로 칩니다.

# 다음은 보드게임판을 나타낸 예시입니다.

# ...D..R
# .D.G...
# ....D.D
# D....D.
# ..D....
# 여기서 "."은 빈 공간을, "R"은 로봇의 처음 위치를, "D"는 장애물의 위치를, "G"는 목표지점을 나타냅니다.
# 위 예시에서는 "R" 위치에서 아래, 왼쪽, 위, 왼쪽, 아래, 오른쪽, 위 순서로 움직이면 7번 만에 "G" 위치에 멈춰 설 수 있으며, 이것이 최소 움직임 중 하나입니다.

# 게임판의 상태를 나타내는 문자열 배열 board가 주어졌을 때, 말이 목표위치에 도달하는데 최소 몇 번 이동해야 하는지 return 하는 solution함수를 완성하세요. 만약 목표위치에 도달할 수 없다면 -1을 return 해주세요.

# 제한 사항
# 3 ≤ board의 길이 ≤ 100
# 3 ≤ board의 원소의 길이 ≤ 100
# board의 원소의 길이는 모두 동일합니다.
# 문자열은 ".", "D", "R", "G"로만 구성되어 있으며 각각 빈 공간, 장애물, 로봇의 처음 위치, 목표 지점을 나타냅니다.
# "R"과 "G"는 한 번씩 등장합니다.
# 입출력 예
# board	result
# ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	7
# [".D.R", "....", ".G..", "...D"]	-1
# 입출력 예 설명
# 입출력 예 #1

# 문제 설명의 예시와 같습니다.
# 입출력 예 #2

# .D.R
# ....
# .G..
# ...D
# "R" 위치에 있는 말을 어떻게 움직여도 "G" 에 도달시킬 수 없습니다.
# 따라서 -1을 return 합니다.

import math
from collections import deque

def isvalid(cor1,cor2,lx,ly,board):
    if (cor1<0)or(cor2<0)or(cor1>=ly)or(cor2>=lx):
        return False
    if board[cor1][cor2]=='D':
        return False
    return True

def solution(board):
        
    lx = len(board[0])
    ly = len(board)
    dir_list = [[-1,0],[1,0],[0,-1],[0,1]]
    cordinate = [0,0]
    G_cordinate = [0,0]
    
    for i in range(ly):
        for j in range(lx):
            if board[i][j] == 'R':
                cordinate[0] = i
                cordinate[1] = j
            elif board[i][j] == 'G':
                G_cordinate[0] = i
                G_cordinate[1] = j
            else:
                pass
    
    ans_map =[[math.inf for _ in range(lx)] for _ in range(ly)]
    ans_map[cordinate[0]][cordinate[1]] = 0 
    visited = deque([cordinate])
    
    while(len(visited)>0):
        cordinate = visited.popleft()
        step = ans_map[cordinate[0]][cordinate[1]]
        toggle = 0
        while(True):
            dir = dir_list[toggle]
            new_cordinate = [cordinate[0],cordinate[1]]
            while(isvalid(new_cordinate[0] + dir[0],new_cordinate[1] + dir[1],lx,ly,board)):
                new_cordinate = [new_cordinate[0] + dir[0],new_cordinate[1] + dir[1]]
            if new_cordinate == cordinate:
                if toggle>=3:
                    break
                else:
                    toggle+=1
                    continue
            else:
                if (step + 1) < ans_map[new_cordinate[0]][new_cordinate[1]]:
                    ans_map[new_cordinate[0]][new_cordinate[1]] = step + 1
                    visited.append(new_cordinate)

                if toggle>=3:
                    break
                else:
                    toggle+=1
                    continue
            
    ans = ans_map[G_cordinate[0]][G_cordinate[1]]
    if ans == math.inf:
        return -1
    else:
        return ans

## BFS를 염두에 두고 풀었다. 다른 사람 풀이. 거의 같은 방식으로 보이나, 내 방식은 deque만을 사용하여 방문할 노드를 관리했고, 아래 풀이는 que와 set를 이용해서 관리했다.
## 방문한 노드에 갱신이 일어난 노드만을 deque에 추가한 것이 내 방식이고, 아래 방식은 방문가능한 모든 노드를 que에 추가하고 set를 통해 실제로 방문해야할 노드인지 확인하는 방식이다.
## 아쉽게도 내 풀이가 좀 더 시간이 많이 걸리고 메모리도 더 쓴다..
#  방문한 노드를 저장해두는 편이 그렇지 않고 기존 값과 비교하여 갱신하는 편보다 효율적인 것 같다.
#  왜냐하면 최초 방문 때 갱신한 값이 항상 최소값인 것으로 보이기 떄문이다.
#  최초 방문 때 갱신한 값보다 최소인 경우가 나중에 방문할 때 있을 수 있다고 생각했었다..
#  DFS 방식이었다면 내 생각이 맞았겠지만 BFS 방식이기 떄문에 불필요한 과정이 된 것이다..
#  BFS 방식이라면 최초 방문 때 갱신한 값이 최소값! 기존 값과 비교하는 과정은 불필요하고 방문했었는지 여부와 방문 가능한 노드만 관리하면 된다!  

# def solution(board):
#     que = []
#     for x, row in enumerate(board):
#         for y, each in enumerate(row):
#             if board[x][y] == 'R':
#                 que.append((x, y, 0))
#     visited = set()
#     while que:
#         x, y, length = que.pop(0)
#         if (x, y) in visited:
#             continue
#         if board[x][y] == 'G':
#             return length
#         visited.add((x, y))
#         for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#             now_x, now_y = x, y
#             while True:
#                 next_x, next_y = now_x + diff_x, now_y + diff_y
#                 if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
#                     now_x, now_y = next_x, next_y
#                     continue
#                 que.append((now_x, now_y, length + 1))
#                 break
#     return -1


## 내 풀이 결과
# 테스트 1 〉	통과 (15.78ms, 10.3MB)
# 테스트 2 〉	통과 (19.73ms, 10.3MB)
# 테스트 3 〉	통과 (0.99ms, 10.4MB)
# 테스트 4 〉	통과 (2.91ms, 10.4MB)
# 테스트 5 〉	통과 (2.70ms, 10.2MB)
# 테스트 6 〉	통과 (1.32ms, 10.3MB)
# 테스트 7 〉	통과 (23.25ms, 10.4MB)
# 테스트 8 〉	통과 (3.24ms, 10.3MB)
# 테스트 9 〉	통과 (5.90ms, 10.4MB)
# 테스트 10 〉	통과 (10.67ms, 10.2MB)
# 테스트 11 〉	통과 (0.08ms, 10.2MB)
# 테스트 12 〉	통과 (0.07ms, 10.2MB)
# 테스트 13 〉	통과 (1.21ms, 10.3MB)
# 테스트 14 〉	통과 (6.69ms, 10.4MB)
# 테스트 15 〉	통과 (2.57ms, 10.1MB)
# 테스트 16 〉	통과 (7.48ms, 10.4MB)
# 테스트 17 〉	통과 (3.55ms, 10.2MB)
# 테스트 18 〉	통과 (5.21ms, 10.4MB)
# 테스트 19 〉	통과 (7.09ms, 10.3MB)
# 테스트 20 〉	통과 (0.68ms, 10.3MB)
# 테스트 21 〉	통과 (12.48ms, 10.3MB)
# 테스트 22 〉	통과 (1.81ms, 10MB)
# 테스트 23 〉	통과 (0.87ms, 10.4MB)
# 테스트 24 〉	통과 (14.45ms, 10.2MB)
# 테스트 25 〉	통과 (8.71ms, 10.1MB)
# 테스트 26 〉	통과 (7.12ms, 10.3MB)
# 테스트 27 〉	통과 (2.32ms, 10.4MB)

# 아래 풀이 결과
# 테스트 1 〉	통과 (6.81ms, 10.3MB)
# 테스트 2 〉	통과 (5.08ms, 10.2MB)
# 테스트 3 〉	통과 (0.57ms, 10.1MB)
# 테스트 4 〉	통과 (2.03ms, 10.1MB)
# 테스트 5 〉	통과 (1.97ms, 10MB)
# 테스트 6 〉	통과 (0.39ms, 10.2MB)
# 테스트 7 〉	통과 (8.32ms, 10.2MB)
# 테스트 8 〉	통과 (0.88ms, 10.2MB)
# 테스트 9 〉	통과 (3.10ms, 10.3MB)
# 테스트 10 〉	통과 (5.09ms, 10.3MB)
# 테스트 11 〉	통과 (0.04ms, 10.1MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.08ms, 10.1MB)
# 테스트 14 〉	통과 (0.61ms, 10.1MB)
# 테스트 15 〉	통과 (0.33ms, 10.1MB)
# 테스트 16 〉	통과 (3.44ms, 10.4MB)
# 테스트 17 〉	통과 (0.65ms, 9.93MB)
# 테스트 18 〉	통과 (0.88ms, 10.2MB)
# 테스트 19 〉	통과 (3.12ms, 10.1MB)
# 테스트 20 〉	통과 (0.16ms, 10MB)
# 테스트 21 〉	통과 (8.99ms, 10.1MB)
# 테스트 22 〉	통과 (1.28ms, 9.92MB)
# 테스트 23 〉	통과 (0.47ms, 9.99MB)
# 테스트 24 〉	통과 (9.82ms, 10.1MB)
# 테스트 25 〉	통과 (3.44ms, 10.1MB)
# 테스트 26 〉	통과 (3.16ms, 10.1MB)
# 테스트 27 〉	통과 (1.90ms, 9.93MB)
# 채점 결과