# 정수를 나선형으로 배치하기
# 문제 설명
# 양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 30
# 입출력 예
# n	result
# 4	[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
# 5	[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
# 입출력 예 설명
# 입출력 예 #1

# 예제 1번의 n의 값은 4로 4 × 4 배열에 다음과 같이 1부터 16까지 숫자를 채울 수 있습니다.

# 행 \ 열	0	1	2	3
# 0	1	2	3	4
# 1	12	13	14	5
# 2	11	16	15	6
# 3	10	9	8	7
# 따라서 [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]를 return 합니다.

# 입출력 예 #2

# 예제 2번의 n의 값은 5로 5 × 5 배열에 다음과 같이 1부터 25까지 숫자를 채울 수 있습니다.

# 행 \ 열	0	1	2	3	4
# 0	1	2	3	4	5
# 1	16	17	18	19	6
# 2	15	24	25	20	7
# 3	14	23	22	21	8
# 4	13	12	11	10	9
# 따라서 [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]를 return 합니다.

def solution(n):
    lst_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    map = [[0]*n for _ in range(n)]
    cursor1=0
    cursor2=0
    dir = lst_dir[0]
    for i in range(1,n*n+1):
        if dir == lst_dir[0]:
            if (cursor2>=n) or (map[cursor1][cursor2]!=0):
                dir = lst_dir[2]
                cursor2-=1
                cursor1+=dir[0]
                cursor2+=dir[1]
            else:
                pass 
        elif dir == lst_dir[1]:
            if (cursor2<0) or (map[cursor1][cursor2]!=0):
                dir = lst_dir[3]
                cursor2+=1
                cursor1+=dir[0]
                cursor2+=dir[1]
            else:
                pass 
        elif dir == lst_dir[2]:
            if (cursor1>=n) or (map[cursor1][cursor2]!=0):
                dir = lst_dir[1]
                cursor1-=1
                cursor1+=dir[0]
                cursor2+=dir[1]
            else:
                pass 
        else:
            if (cursor1<0) or (map[cursor1][cursor2]!=0):
                dir = lst_dir[0]
                cursor1+=1
                cursor1+=dir[0]
                cursor2+=dir[1]
            else:
                pass 
            
        map[cursor1][cursor2] = i 
        cursor1+=dir[0]
        cursor2+=dir[1]
        
    return map


# def solution(n):
#     answer = [[None for j in range(n)] for i in range(n)]
#     move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     x, y, m = 0, 0, 0
#     for i in range(1, n**2 + 1):
#         answer[y][x] = i
#         if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
#             m = (m + 1) % len(move)
#         y, x = y + move[m][0], x + move[m][1]
#     return answer
## 다른사람의 풀이. 나선형으로 돌 때 도는 순서가 일정한 것과 % 연산자를 활용하면 더 간략하게 코드를 줄일 수 있다. 
## 이동하면서 숫자를 채우고 다음 위치를 확인하다가 예외케이스일 경우 다음 순서의 방향으로 트는 것. 이러한 흐름 자체는 내 알고리즘과 같다.
