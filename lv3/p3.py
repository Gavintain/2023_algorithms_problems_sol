# 길 찾기 게임
# 문제 설명
# 길 찾기 게임
# 전무로 승진한 라이언은 기분이 너무 좋아 프렌즈를 이끌고 특별 휴가를 가기로 했다.
# 내친김에 여행 계획까지 구상하던 라이언은 재미있는 게임을 생각해냈고 역시 전무로 승진할만한 인재라고 스스로에게 감탄했다.

# 라이언이 구상한(그리고 아마도 라이언만 즐거울만한) 게임은, 카카오 프렌즈를 두 팀으로 나누고, 각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리하는 것이다.

# 그냥 지도를 주고 게임을 시작하면 재미가 덜해지므로, 라이언은 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후, 순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

# 라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.

# 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
# 모든 노드는 서로 다른 x값을 가진다.
# 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
# 자식 노드의 y 값은 항상 부모 노드보다 작다.
# 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
# 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.
# 아래 예시를 확인해보자.

# 라이언의 규칙에 맞게 이진트리의 노드만 좌표 평면에 그리면 다음과 같다. (이진트리의 각 노드에는 1부터 N까지 순서대로 번호가 붙어있다.)

# tree_3.png

# 이제, 노드를 잇는 간선(edge)을 모두 그리면 아래와 같은 모양이 된다.

# tree_4.png

# 위 이진트리에서 전위 순회(preorder), 후위 순회(postorder)를 한 결과는 다음과 같고, 이것은 각 팀이 방문해야 할 순서를 의미한다.

# 전위 순회 : 7, 4, 6, 9, 1, 8, 5, 2, 3
# 후위 순회 : 9, 6, 5, 8, 1, 4, 3, 2, 7
# 다행히 두 팀 모두 머리를 모아 분석한 끝에 라이언의 의도를 간신히 알아차렸다.

# 그러나 여전히 문제는 남아있다. 노드의 수가 예시처럼 적다면 쉽게 해결할 수 있겠지만, 예상대로 라이언은 그렇게 할 생각이 전혀 없었다.

# 이제 당신이 나설 때가 되었다.

# 곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

# 제한사항
# nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
# nodeinfo의 길이는 1 이상 10,000 이하이다.
# nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
# 모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
# 트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
# 모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.
# 입출력 예
# nodeinfo	result
# [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
# 입출력 예 설명
# 입출력 예 #1

# 문제에 주어진 예시와 같다.

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    y_node_dict = defaultdict(list)
    node_x_dict = defaultdict(int)
    node_y_dict = defaultdict(int)
    for i in range(len(nodeinfo)):
        node_xy = nodeinfo[i]
        node_num = i+1
        y_node_dict[node_xy[1]].append(node_num)
        node_x_dict[node_num] = node_xy[0]
        node_y_dict[node_num] = node_xy[1]
    
    y_lst = sorted(list(y_node_dict.keys()))
    max_y = y_lst[-1]
    root = y_node_dict[max_y][0]

    def consistent_check(parent_lst,node,child):
        for ancestor in parent_lst:
            if (node_x_dict[node]<node_x_dict[ancestor]) == (node_x_dict[child]<node_x_dict[ancestor]):
                pass
            else:
                return False
        return True 
        
    def has_child(parent_lst,node):
        node_y = node_y_dict[node]
        index = y_lst.index(node_y)-1
        exist = False
        left = None
        right = None
        if index<0:
            return [False,None,None]
        else:
            child_ylevel = y_lst[index]
            child_lst = y_node_dict[child_ylevel]
            for child in child_lst:
                if right !=None and left !=None:
                    break
                else:
                    if node_x_dict[child]>node_x_dict[node]:
                        if consistent_check(parent_lst,node,child):
                            right  = child
                            exist = True
                    elif node_x_dict[child]<node_x_dict[node]:
                        if consistent_check(parent_lst,node,child):
                            left = child
                            exist = True
                    else:
                        continue
            return [exist,left,right]
        

    answer=[[],[]]

    def travel(parent_lst,node):
        if node == None:
            return []
        else:
            child = has_child(parent_lst,node)
            new_parent_lst = parent_lst + [node]
            if child[0]:
                answer[0].append(node)
                travel(new_parent_lst,child[1])
                travel(new_parent_lst,child[2])
                answer[1].append(node) 
            else:
                answer[0].append(node)
                answer[1].append(node)
            
    travel([],root)
              
    return answer

# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (85.83ms, 15.4MB)
# 테스트 7 〉	통과 (87.95ms, 15.4MB)
# 테스트 8 〉	통과 (527.60ms, 12MB)
# 테스트 9 〉	통과 (3989.86ms, 14.9MB)
# 테스트 10 〉	통과 (161.47ms, 11MB)
# 테스트 11 〉	통과 (4375.93ms, 14.8MB)
# 테스트 12 〉	통과 (5558.33ms, 15MB)
# 테스트 13 〉	통과 (3.90ms, 10.3MB)
# 테스트 14 〉	통과 (190.94ms, 10.6MB)
# 테스트 15 〉	통과 (2080.80ms, 12.4MB)
# 테스트 16 〉	통과 (8402.77ms, 14.5MB)
# 테스트 17 〉	통과 (55.88ms, 10.6MB)
# 테스트 18 〉	통과 (5497.59ms, 14.5MB)
# 테스트 19 〉	통과 (187.31ms, 10.9MB)
# 테스트 20 〉	통과 (936.96ms, 11.8MB)
# 테스트 21 〉	통과 (1691.79ms, 12.9MB)
# 테스트 22 〉	통과 (4180.86ms, 14.3MB)
# 테스트 23 〉	통과 (3919.11ms, 14.6MB)
# 테스트 24 〉	통과 (0.03ms, 10.2MB)
# 테스트 25 〉	통과 (0.03ms, 10.4MB)
# 테스트 26 〉	통과 (144.59ms, 14.9MB)
# 테스트 27 〉	통과 (0.03ms, 10.4MB)
# 테스트 28 〉	통과 (0.08ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.4MB)


## 다른사람풀이, 내 알고리즘보다 훨씬 시간효율적이나 공간효율성은 내 알고리즘이 더 좋다.

preorder = list() # 귀찮아서 전역으로
postorder = list()
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    order(nodes,levels,0)
    return [preorder,postorder]

def order(nodes,levels,curlevel):
    n = nodes[:] # copy
    cur = n.pop(0) # VISIT
    preorder.append(cur[0]) # PRE-ORDER
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor
            if n[i][1][1] == levels[curlevel+1]: # next floor
                if n[i][1][0] < cur[1][0]: # LEFT CHILD
                    order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
                else: # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                    break
    postorder.append(cur[0]) # POST-ORDER

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (126.38ms, 19.4MB)
# 테스트 7 〉	통과 (91.82ms, 19.5MB)
# 테스트 8 〉	통과 (53.41ms, 13.1MB)
# 테스트 9 〉	통과 (353.50ms, 26.1MB)
# 테스트 10 〉	통과 (16.05ms, 11.3MB)
# 테스트 11 〉	통과 (269.75ms, 22.5MB)
# 테스트 12 〉	통과 (336.90ms, 23.9MB)
# 테스트 13 〉	통과 (0.46ms, 10.4MB)
# 테스트 14 〉	통과 (4.25ms, 10.5MB)
# 테스트 15 〉	통과 (19.40ms, 12.1MB)
# 테스트 16 〉	통과 (50.00ms, 14.3MB)
# 테스트 17 〉	통과 (4.68ms, 10.6MB)
# 테스트 18 〉	통과 (98.52ms, 14.3MB)
# 테스트 19 〉	통과 (9.59ms, 10.9MB)
# 테스트 20 〉	통과 (26.57ms, 11.8MB)
# 테스트 21 〉	통과 (53.07ms, 12.5MB)
# 테스트 22 〉	통과 (56.76ms, 14.1MB)
# 테스트 23 〉	통과 (57.38ms, 14.5MB)
# 테스트 24 〉	통과 (0.03ms, 10.3MB)
# 테스트 25 〉	통과 (0.05ms, 10.3MB)
# 테스트 26 〉	통과 (143.64ms, 18.1MB)
# 테스트 27 〉	통과 (0.03ms, 10.3MB)
# 테스트 28 〉	통과 (0.07ms, 10.3MB)
# 테스트 29 〉	통과 (0.02ms, 10.2MB)