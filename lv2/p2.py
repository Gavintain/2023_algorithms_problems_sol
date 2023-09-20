# 문제 설명
# 메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다. 지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다. 지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며, 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다. 이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다. 어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 합니다.

# 지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요. 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.

# 제한사항
# 3 ≤ maps의 길이 ≤ 100
# 3 ≤ maps[i]의 길이 ≤ 100
# maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열입니다.
# 지도는 직사각형 형태입니다.
# 입출력 예
# maps	result
# ["X591X","X1X5X","X231X", "1XXX1"]	[1, 1, 27]
# ["XXX","XXX","XXX"]	[-1]



import sys
sys.setrecursionlimit(10**5) ### 테스트 케이스 런타임 오류에 많이 메달렸는데, 파이썬 재귀제한이 문제였다..

def solution(maps):
    num_row = len(maps)
    num_col = len(maps[0])
    unvisited = [i for i in range(num_row*num_col)]
    answer = []
    def x_y_val(x0,y0):
        if x0 >= num_row or y0 >= num_col or x0 <0 or y0 <0:
            return 0
        else:
            return 1
    
    def DFS(x_cod,y_cod):
        if x_y_val(x_cod,y_cod):
            if x_cod*num_col+y_cod in unvisited:
                unvisited.remove(x_cod*num_col+y_cod)
                if maps[x_cod][y_cod] == "X":
                    return 0
                else:
                    food = int(maps[x_cod][y_cod])
                    food += DFS(x_cod+1,y_cod)
                    food += DFS(x_cod-1,y_cod)
                    food += DFS(x_cod,y_cod+1)
                    food += DFS(x_cod,y_cod-1)
                    return food
            else:
                return 0
        else:
            return 0
                    
    while(len(unvisited) >0):
        visited = unvisited[0]
        x = visited//num_col
        y = visited%num_col
        num_food = DFS(x,y)
        if num_food <1:
            continue
        else:
            answer.append(num_food)
    if len(answer)==0:
        return [-1]
    else:
        answer.sort()
        return answer


## 셀프 코드리뷰

# 방문 노드 관리를 2차원 배열을 사용하는 방식이나, 파이썬 1차원 리스트로 하는 방식이나 둘 다 시간 복잡도는 O(n^2)이다. 
# 세부적으로 알고리즘을 봤을 때 파이썬 remove 매서드가 O(n) (=kn)이고, 방문한 노드가 많아질수록 n이 줄기 때문에 파이썬 1차원 리스트 방식이 시간 복잡도가 kn(n-1)/2,
# 2차원 배열 방식은 n^2 이기 때문에 k가 2보다 크지 않다면 파이썬 1차원 리스트 방식이 약간 더 빠를 것 같다.. 
# 하지만 n이 커질수록 파이썬 리스트가 동적 배열이기 때문에 오버헤드가 커져서 2차원 배열이 더 좋을 것이다.
# 직접 테스트해본다면 n값에 따라 크로스가 나는 지점을 찾으면 의미있을 것 같다. 아 remove 매서드 내부 구현도 알아봐야 할 수도 있다.
