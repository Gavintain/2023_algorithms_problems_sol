# 문제 설명
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# image.png
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# board는 n * n 배열입니다.
# 1 ≤ n ≤ 100
# 지뢰는 1로 표시되어 있습니다.
# board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
# 입출력 예
# board	result
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
# [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0
# 입출력 예 설명
# 입출력 예 #1

# (3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.
# 입출력 예 #2

# (3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.
# 입출력 예 #3

# 모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.

def solution(board):
    n = len(board)
    new_board = [[0]*(n+2) for _ in range(n+2)]
    answer=0
    for x in range(n):
        for y in range(n):
            nb_x = x+1
            nb_y = y+1
            if board[x][y] ==1:
                new_board[nb_x][nb_y] = 1
                new_board[nb_x-1][nb_y-1] = 1
                new_board[nb_x-1][nb_y+1] = 1
                new_board[nb_x-1][nb_y] = 1
                new_board[nb_x+1][nb_y+1] = 1
                new_board[nb_x+1][nb_y] = 1
                new_board[nb_x+1][nb_y-1] = 1
                new_board[nb_x][nb_y-1] = 1
                new_board[nb_x][nb_y+1] = 1

    new_board.pop(-1)
    new_board.pop(0)

    for i in range(n):
        print(new_board)
        new_board[i].pop(-1)
        new_board[i].pop(0)
        answer += new_board[i].count(0)

    return answer


## 파이썬의 얕은 복사, 깊은 복사 개념을 알게됨.
## new_board = [[0]*(n+2)] *(n+2) 는 [[0]*(n+2)]를 참조하는 객체를 n+2개를 만든다 (얕은 복사). [[0]*(n+2)] 주소의 값이 바뀌면 n+2개의 모든 리스트 값이 똑같은 값으로 바뀜.
## [[0]*(n+2) for _ in range(n+2)] 이런식으로 작성해야함.

## 인상깊은 타인의 알고리즘 코드 리뷰.

# def solution(board):
#     n = len(board)
#     danger = set()
#     for i, row in enumerate(board):
#         for j, x in enumerate(row):
#             if not x:
#                 continue
#             danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
#     return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

### set 자료구조가 중복된 자료를 가지지 않는 것을 이용한 것 같다. 파이썬 스타일의 코딩이 특히 인상적이다.
### set.update() 매서드는 매개변수로 iterable 객체를 받을 때 튜플을 set에 저장할 수 있다. 튜플을 저장하려면 튜플 집합을 한번에 업데이트해야한다.
# sett = set()
# tuple_lst = [(1,2),(2,3)]

# sett.update(tuple_lst[0])
# sett.update(tuple_lst[1])
# 이런식으로 하면 {1,2,3}이 되고
# sett.update(item for item in tuple_lst)
# 이렇게 하면 {(1,2),(2,3)} 이 된다.