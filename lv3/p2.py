# 합승 택시 요금
# 문제 설명
# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

# 밤늦게 귀가할 때 안전을 위해 항상 택시를 이용하던 무지는 최근 야근이 잦아져 택시를 더 많이 이용하게 되어 택시비를 아낄 수 있는 방법을 고민하고 있습니다. "무지"는 자신이 택시를 이용할 때 동료인 어피치 역시 자신과 비슷한 방향으로 가는 택시를 종종 이용하는 것을 알게 되었습니다. "무지"는 "어피치"와 귀가 방향이 비슷하여 택시 합승을 적절히 이용하면 택시요금을 얼마나 아낄 수 있을 지 계산해 보고 "어피치"에게 합승을 제안해 보려고 합니다.

# 2021_kakao_taxi_01.png

# 위 예시 그림은 택시가 이동 가능한 반경에 있는 6개 지점 사이의 이동 가능한 택시노선과 예상요금을 보여주고 있습니다.
# 그림에서 A와 B 두 사람은 출발지점인 4번 지점에서 출발해서 택시를 타고 귀가하려고 합니다. A의 집은 6번 지점에 있으며 B의 집은 2번 지점에 있고 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금이 얼마인 지 계산하려고 합니다.

# 그림의 원은 지점을 나타내며 원 안의 숫자는 지점 번호를 나타냅니다.
# 지점이 n개일 때, 지점 번호는 1부터 n까지 사용됩니다.
# 지점 간에 택시가 이동할 수 있는 경로를 간선이라 하며, 간선에 표시된 숫자는 두 지점 사이의 예상 택시요금을 나타냅니다.
# 간선은 편의 상 직선으로 표시되어 있습니다.
# 위 그림 예시에서, 4번 지점에서 1번 지점으로(4→1) 가거나, 1번 지점에서 4번 지점으로(1→4) 갈 때 예상 택시요금은 10원으로 동일하며 이동 방향에 따라 달라지지 않습니다.
# 예상되는 최저 택시요금은 다음과 같이 계산됩니다.
# 4→1→5 : A, B가 합승하여 택시를 이용합니다. 예상 택시요금은 10 + 24 = 34원 입니다.
# 5→6 : A가 혼자 택시를 이용합니다. 예상 택시요금은 2원 입니다.
# 5→3→2 : B가 혼자 택시를 이용합니다. 예상 택시요금은 24 + 22 = 46원 입니다.
# A, B 모두 귀가 완료까지 예상되는 최저 택시요금은 34 + 2 + 46 = 82원 입니다.
# [문제]
# 지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다. 이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.
# 만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.

# [제한사항]
# 지점갯수 n은 3 이상 200 이하인 자연수입니다.
# 지점 s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
# 즉, 출발지점, A의 도착지점, B의 도착지점은 서로 겹치지 않습니다.
# fares는 2차원 정수 배열입니다.
# fares 배열의 크기는 2 이상 n x (n-1) / 2 이하입니다.
# 예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. (6 x 5 / 2 = 15)
# fares 배열의 각 행은 [c, d, f] 형태입니다.
# c지점과 d지점 사이의 예상 택시요금이 f원이라는 뜻입니다.
# 지점 c, d는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
# 요금 f는 1 이상 100,000 이하인 자연수입니다.
# fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.
# 출발지점 s에서 도착지점 a와 b로 가는 경로가 존재하는 경우만 입력으로 주어집니다.
# [입출력 예]
# n	s	a	b	fares	result
# 6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
# 7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
# 6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18
# 입출력 예에 대한 설명
# 입출력 예 #1
# 문제 예시와 같습니다.

# 입출력 예 #2
# 2021_kakao_taxi_02.png

# 합승을 하지 않고, B는 3→2→1, A는 3→6→4 경로로 각자 택시를 타고 가는 것이 최저 예상 택시요금입니다.
# 따라서 최저 예상 택시요금은 (3 + 6) + (1 + 4) = 14원 입니다.
# 입출력 예 #3
# 2021_kakao_taxi_03.png

# A와 B가 4→6 구간을 합승하고 B가 6번 지점에서 내린 후, A가6→5` 구간을 혼자 타고 가는 것이 최저 예상 택시요금입니다.
# 따라서 최저 예상 택시요금은 7 + 11 = 18원 입니다.

## 시간초과 2케이스난 솔루션
# import math
# def solution(n, s, a, b, fares):
#     confirmed_cost_dict = {x:math.inf for x in range(1,n+1)}
#     confirmed_cost_dict[s] = 0

#     for _ in range(n):
#         for edge in fares:
#             d = edge[2]
#             n1 = edge[0]
#             n2 = edge[1]
#             if confirmed_cost_dict[n1] + d < confirmed_cost_dict[n2]:
#                 confirmed_cost_dict[n2] = confirmed_cost_dict[n1] + d
  
#             elif confirmed_cost_dict[n2] + d < confirmed_cost_dict[n1]:
#                 confirmed_cost_dict[n1] = confirmed_cost_dict[n2] + d

#             else:
#                 pass
    
#     final_cost = math.inf
#     confirmed_unvisited_list = [i for i in range(1,n+1)]
#     while(len(confirmed_unvisited_list)>0):
#         share_node = confirmed_unvisited_list.pop()
#         if confirmed_cost_dict[share_node] == math.inf:
#             continue
#         shared_cost_dict = {x:math.inf for x in range(1,n+1)}
#         shared_cost_dict[share_node] = confirmed_cost_dict[share_node]
#         for _ in range(n):
#             for edge in fares:
#                 d = edge[2]
#                 n1 = edge[0]
#                 n2 = edge[1] 
#                 if shared_cost_dict[n1] + d < shared_cost_dict[n2]:
#                     shared_cost_dict[n2] = shared_cost_dict[n1] + d
    
#                 elif shared_cost_dict[n2] + d < shared_cost_dict[n1]:
#                     shared_cost_dict[n1] = shared_cost_dict[n2] + d

#                 else:
#                     pass
#         expected_cost = shared_cost_dict[a] + shared_cost_dict[b] - shared_cost_dict[share_node]
#         if expected_cost < final_cost:
#             final_cost = expected_cost

#     return final_cost

import heapq
import math

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    def dijkstra(start):
        distances = [math.inf] * (n + 1)
        distances[start] = 0
        queue = []
        heapq.heappush(queue,start)
  
        while queue:
            current_node = heapq.heappop(queue)
            for adjacent, weight in graph[current_node]:
                distance = distances[current_node] + weight
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue,adjacent)
        return distances

    min_cost = math.inf
    for i in range(1, n + 1):
        temp_dist = dijkstra(i)
        cost = temp_dist[s] + temp_dist[a] + temp_dist[b]
        min_cost = min(min_cost, cost)

    return min_cost


테스트 1 〉	통과 (69.43ms, 10.3MB)
테스트 2 〉	통과 (539.71ms, 10.6MB)
테스트 3 〉	통과 (126.95ms, 10MB)
테스트 4 〉	통과 (101.69ms, 10.4MB)
테스트 5 〉	통과 (122.63ms, 10.2MB)
테스트 6 〉	통과 (113.07ms, 10.2MB)
테스트 7 〉	통과 (8921.10ms, 15.5MB)
테스트 8 〉	통과 (8205.47ms, 15.4MB)
테스트 9 〉	통과 (1018.96ms, 15.3MB)
테스트 10 〉	통과 (905.43ms, 15.3MB)
테스트 11 〉	통과 (1027.35ms, 15.3MB)
테스트 12 〉	통과 (3894.69ms, 12.8MB)
테스트 13 〉	통과 (4002.93ms, 12.7MB)
테스트 14 〉	통과 (3723.80ms, 12.9MB)
테스트 15 〉	통과 (4082.37ms, 12.8MB)
테스트 16 〉	통과 (86.75ms, 10.2MB)
테스트 17 〉	통과 (96.89ms, 10.2MB)
테스트 18 〉	통과 (103.48ms, 10.3MB)
테스트 19 〉	통과 (355.27ms, 10.2MB)
테스트 20 〉	통과 (685.75ms, 10.5MB)
테스트 21 〉	통과 (789.30ms, 10.4MB)
테스트 22 〉	통과 (4142.18ms, 12.7MB)
테스트 23 〉	통과 (4100.40ms, 12.8MB)
테스트 24 〉	통과 (3989.29ms, 12.9MB)
테스트 25 〉	통과 (65.95ms, 10.2MB)
테스트 26 〉	통과 (41.30ms, 10.3MB)
테스트 27 〉	통과 (583.96ms, 10.5MB)
테스트 28 〉	통과 (604.28ms, 10.3MB)
테스트 29 〉	통과 (28.92ms, 10.2MB)
테스트 30 〉	통과 (35.24ms, 10.3MB)


## 힙큐를 제대로 이용하니 시간 효율성 최대 5배 향상
import heapq
import math

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    def dijkstra(start):
        distances = [math.inf] * (n + 1)
        distances[start] = 0
        queue = []
        heapq.heappush(queue,(0,start))
  
        while queue:
            distance,current_node = heapq.heappop(queue)
            if distance > distances[current_node]:
                continue
            else:
                for adjacent, weight in graph[current_node]:
                    distance = distances[current_node] + weight
                    if distance < distances[adjacent]:
                        distances[adjacent] = distance
                        heapq.heappush(queue,(distance,adjacent))
        return distances

    min_cost = math.inf
    for i in range(1, n + 1):
        temp_dist = dijkstra(i)
        cost = temp_dist[s] + temp_dist[a] + temp_dist[b]
        min_cost = min(min_cost, cost)

    return min_cost


테스트 1 〉	통과 (21.57ms, 10.4MB)
테스트 2 〉	통과 (102.58ms, 10.6MB)
테스트 3 〉	통과 (36.24ms, 10.2MB)
테스트 4 〉	통과 (35.81ms, 10.2MB)
테스트 5 〉	통과 (35.87ms, 10.3MB)
테스트 6 〉	통과 (36.58ms, 10.2MB)
테스트 7 〉	통과 (1082.53ms, 15.6MB)
테스트 8 〉	통과 (1067.32ms, 15.4MB)
테스트 9 〉	통과 (963.95ms, 15.5MB)
테스트 10 〉	통과 (1026.63ms, 15.5MB)
테스트 11 〉	통과 (944.55ms, 15.6MB)
테스트 12 〉	통과 (537.14ms, 12.9MB)
테스트 13 〉	통과 (537.15ms, 12.9MB)
테스트 14 〉	통과 (605.31ms, 12.8MB)
테스트 15 〉	통과 (606.73ms, 12.8MB)
테스트 16 〉	통과 (35.34ms, 10.2MB)
테스트 17 〉	통과 (32.03ms, 10.2MB)
테스트 18 〉	통과 (30.96ms, 10.4MB)
테스트 19 〉	통과 (83.00ms, 10.6MB)
테스트 20 〉	통과 (133.37ms, 10.7MB)
테스트 21 〉	통과 (137.05ms, 10.7MB)
테스트 22 〉	통과 (553.83ms, 12.9MB)
테스트 23 〉	통과 (558.12ms, 12.9MB)
테스트 24 〉	통과 (535.87ms, 12.9MB)
테스트 25 〉	통과 (23.53ms, 10.3MB)
테스트 26 〉	통과 (17.83ms, 10.2MB)
테스트 27 〉	통과 (119.18ms, 10.4MB)
테스트 28 〉	통과 (122.18ms, 10.4MB)
테스트 29 〉	통과 (13.20ms, 10.3MB)
테스트 30 〉	통과 (12.39ms, 10.2MB)


## 플로이드 워샬 방식의 경우, 다익스트라에 비해 모두 꾸준히 높은 값을 보임. 플로이드 워샬 알고리즘의 노드 갱신순서를 잘 확인할 것.
import math

def solution(n, s, a, b, fares):
    INF = math.inf
    graph = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i][i]=0

    for fare in fares:
        graph[fare[0]-1][fare[1]-1] = fare[2]
        graph[fare[1]-1][fare[0]-1] = fare[2]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = graph[j][i]
                y = graph[j][k]
                d = graph[i][k]
                if x+d < y:
                    graph[j][k] = x+d

    min_cost = math.inf
    for i in range(n):
        cost = graph[s-1][i] + graph[i][a-1] + graph[i][b-1]
        min_cost = min(min_cost, cost)

    return min_cost

테스트 1 〉	통과 (175.08ms, 10.3MB)
테스트 2 〉	통과 (539.24ms, 11MB)
테스트 3 〉	통과 (1222.23ms, 11.3MB)
테스트 4 〉	통과 (1214.40ms, 11.3MB)
테스트 5 〉	통과 (1247.52ms, 11.4MB)
테스트 6 〉	통과 (1240.79ms, 11.5MB)
테스트 7 〉	통과 (1405.68ms, 13.8MB)
테스트 8 〉	통과 (1444.19ms, 14.1MB)
테스트 9 〉	통과 (1299.53ms, 13MB)
테스트 10 〉	통과 (1400.84ms, 12.9MB)
테스트 11 〉	통과 (1272.01ms, 12.8MB)
테스트 12 〉	통과 (1296.82ms, 12.8MB)
테스트 13 〉	통과 (1407.73ms, 12.7MB)
테스트 14 〉	통과 (1262.13ms, 12.7MB)
테스트 15 〉	통과 (1287.31ms, 12.8MB)
테스트 16 〉	통과 (1206.42ms, 11.4MB)
테스트 17 〉	통과 (1211.16ms, 11.3MB)
테스트 18 〉	통과 (1238.94ms, 11.2MB)
테스트 19 〉	통과 (1246.69ms, 11.3MB)
테스트 20 〉	통과 (1270.08ms, 11.7MB)
테스트 21 〉	통과 (1282.37ms, 11.7MB)
테스트 22 〉	통과 (1291.60ms, 12.8MB)
테스트 23 〉	통과 (1308.97ms, 12.8MB)
테스트 24 〉	통과 (1264.79ms, 12.7MB)
테스트 25 〉	통과 (1199.53ms, 11.1MB)
테스트 26 〉	통과 (1177.97ms, 10.8MB)
테스트 27 〉	통과 (1189.18ms, 10.5MB)
테스트 28 〉	통과 (1196.89ms, 10.4MB)
테스트 29 〉	통과 (158.75ms, 10.3MB)
테스트 30 〉	통과 (159.99ms, 10.4MB)