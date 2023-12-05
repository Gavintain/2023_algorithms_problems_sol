# 문제 설명
# N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 다음은 N = 5, K = 3인 경우의 예시입니다.

# 배달_1_uxun8t.png

# 위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다. 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다. 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
# road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
# a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
# 입출력 예
# N	road	K	result
# 5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
# 6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.

# 입출력 예 #2
# 주어진 마을과 도로의 모양은 아래 그림과 같습니다.
# 배달_3_njc7kq.png
# 1번 마을에서 배달에 4시간 이하가 걸리는 마을은 [1, 2, 3, 5] 4개이므로 4를 return 합니다.


import math
from collections import deque
def solution(N, road, K):
    node_lst = [math.inf for _ in range(N)]
    edge_lst = [[] for _ in range(N)]
    node_lst[0] = 0
    
    for r in road:
        node1 = r[0]-1
        node2 = r[1]-1
        edge_lst[node1].append([node2,r[2]])
        edge_lst[node2].append([node1,r[2]]) 
        
    to_visit=deque([0])

    while len(to_visit)>0:
        node = to_visit.pop()
        for edge in edge_lst[node]:
            if node_lst[node]+edge[1] < node_lst[edge[0]]:
                node_lst[edge[0]] = node_lst[node]+edge[1]
                to_visit.appendleft(edge[0])

            
                    
    answer = sum([True if x<=K else False for x in node_lst])

    return answer

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.08ms, 10.3MB)
# 테스트 13 〉	통과 (0.05ms, 10.2MB)
# 테스트 14 〉	통과 (1.47ms, 10.3MB)
# 테스트 15 〉	통과 (3.93ms, 10.4MB)
# 테스트 16 〉	통과 (0.05ms, 10.2MB)
# 테스트 17 〉	통과 (0.04ms, 10.2MB)
# 테스트 18 〉	통과 (0.38ms, 10.2MB)
# 테스트 19 〉	통과 (2.22ms, 10.5MB)
# 테스트 20 〉	통과 (0.61ms, 10.2MB)
# 테스트 21 〉	통과 (4.01ms, 10.7MB)
# 테스트 22 〉	통과 (0.62ms, 10.3MB)
# 테스트 23 〉	통과 (2.52ms, 10.6MB)
# 테스트 24 〉	통과 (1.58ms, 10.5MB)
# 테스트 25 〉	통과 (4.22ms, 10.6MB)
# 테스트 26 〉	통과 (4.73ms, 10.5MB)
# 테스트 27 〉	통과 (4.83ms, 10.5MB)
# 테스트 28 〉	통과 (6.27ms, 10.7MB)
# 테스트 29 〉	통과 (7.31ms, 10.5MB)
# 테스트 30 〉	통과 (1.91ms, 10.6MB)
# 테스트 31 〉	통과 (0.06ms, 10.2MB)
# 테스트 32 〉	통과 (0.09ms, 10.2MB)


import math
def solution(N, road, K):
    node_lst = [math.inf for _ in range(N)]
    node_lst[0] = 0
    
    for _ in range(N):
        for r in road:
            node1 = r[0]-1
            node2 = r[1]-1
            if node_lst[node1]+r[2] < node_lst[node2]:
                node_lst[node2] =  node_lst[node1]+r[2]
            if node_lst[node2]+r[2] < node_lst[node1]:
                node_lst[node1] =  node_lst[node2]+r[2]
    
         
    answer = sum([True if x<=K else False for x in node_lst])

    return answer

# 테스트 1 〉	통과 (0.06ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.08ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.05ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.08ms, 10.2MB)
# 테스트 12 〉	통과 (0.45ms, 10.3MB)
# 테스트 13 〉	통과 (0.47ms, 10.1MB)
# 테스트 14 〉	통과 (7.69ms, 10.2MB)
# 테스트 15 〉	통과 (12.39ms, 10.3MB)
# 테스트 16 〉	통과 (0.19ms, 10.1MB)
# 테스트 17 〉	통과 (0.42ms, 10.1MB)
# 테스트 18 〉	통과 (6.19ms, 10.2MB)
# 테스트 19 〉	통과 (13.68ms, 10.4MB)
# 테스트 20 〉	통과 (2.76ms, 10MB)
# 테스트 21 〉	통과 (19.02ms, 10.3MB)
# 테스트 22 〉	통과 (8.36ms, 10.1MB)
# 테스트 23 〉	통과 (17.97ms, 10.2MB)
# 테스트 24 〉	통과 (11.70ms, 10.2MB)
# 테스트 25 〉	통과 (32.28ms, 10.6MB)
# 테스트 26 〉	통과 (23.84ms, 10.3MB)
# 테스트 27 〉	통과 (22.18ms, 10.3MB)
# 테스트 28 〉	통과 (26.55ms, 10.4MB)
# 테스트 29 〉	통과 (27.50ms, 10.5MB)
# 테스트 30 〉	통과 (24.88ms, 10.5MB)
# 테스트 31 〉	통과 (0.64ms, 10.1MB)
# 테스트 32 〉	통과 (1.24ms, 10.2MB)

import math,heapq
from collections import deque
def solution(N, road, K):
    node_lst = [math.inf for _ in range(N)]
    edge_lst = [[] for _ in range(N)]
    unvisited = [True for _ in range(N)]
    node_lst[0] = 0
    
    for r in road:
        node1 = r[0]-1
        node2 = r[1]-1
        edge_lst[node1].append([node2,r[2]])
        edge_lst[node2].append([node1,r[2]]) 
        
    to_visit=[(0,0)]

    while len(to_visit):
        distance, node = heapq.heappop(to_visit)
        # if unvisited[node]:
        #     unvisited[node] = False
        for edge in edge_lst[node]:
            next_node, edge_distance = edge
            if node_lst[node] + edge_distance < node_lst[next_node]:
                node_lst[next_node] = node_lst[node] + edge_distance
                heapq.heappush(to_visit, (node_lst[next_node], next_node))
        
                    
    answer = sum([True if x<=K else False for x in node_lst])

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.06ms, 10.4MB)
# 테스트 13 〉	통과 (0.05ms, 10.1MB)
# 테스트 14 〉	통과 (1.94ms, 10.5MB)
# 테스트 15 〉	통과 (1.54ms, 10.4MB)
# 테스트 16 〉	통과 (0.05ms, 10.4MB)
# 테스트 17 〉	통과 (0.04ms, 10.1MB)
# 테스트 18 〉	통과 (0.30ms, 10.3MB)
# 테스트 19 〉	통과 (1.39ms, 10.3MB)
# 테스트 20 〉	통과 (0.25ms, 10.4MB)
# 테스트 21 〉	통과 (1.89ms, 10.4MB)
# 테스트 22 〉	통과 (0.45ms, 10.3MB)
# 테스트 23 〉	통과 (1.80ms, 10.8MB)
# 테스트 24 〉	통과 (1.17ms, 10.4MB)
# 테스트 25 〉	통과 (2.79ms, 10.6MB)
# 테스트 26 〉	통과 (3.21ms, 10.5MB)
# 테스트 27 〉	통과 (5.22ms, 10.6MB)
# 테스트 28 〉	통과 (2.78ms, 10.6MB)
# 테스트 29 〉	통과 (3.05ms, 10.4MB)
# 테스트 30 〉	통과 (2.24ms, 10.6MB)
# 테스트 31 〉	통과 (0.07ms, 10.3MB)
# 테스트 32 〉	통과 (0.09ms, 10.1MB)

## 힙큐를 사용한 경우가 가장 빠르다.. 2번째 알고리즘은 가장 간단하게 생각할 수 있는 방법이다.
## 2번째 방법에는 간선이 양방향이므로 if문을 병렬로 2번 사용했다.
## 해당 노드에 대한 거리가 갱신이 되었을 때, 다음으로 방문할 노드로 추가하는 것이 중요하다.
## 각 노드들에 대한 최단거리를 구하기 위해서는 시작점으로부터 짧은 거리에 있는 노드들부터 확인하는 것이 최적의 방법이다.
## 방문해야 할 노드들 중 가장 짧은 거리의 값을 가진 노드를 heapq 모듈을 통해 빠른 시간으로 얻을 수 있다.
## 방문해야할 노드를 heappush로 추가하고 heappop 으로 방문할 노드를 구한다..