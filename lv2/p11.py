# 쿼드압축 후 개수 세기
# 문제 설명
# 0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

# 당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
# 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
# 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
# arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태를 하고 있습니다. 즉, arr의 행의 개수는 1, 2, 4, 8, ..., 1024 중 하나입니다.
# arr의 각 행의 길이는 arr의 행의 개수와 같습니다. 즉, arr은 정사각형 배열입니다.
# arr의 각 행에 있는 모든 값은 0 또는 1 입니다.
# 입출력 예
# arr	result
# [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	[4,9]
# [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]	[10,15]
# 입출력 예 설명
# 입출력 예 #1

# 다음 그림은 주어진 arr을 압축하는 과정을 나타낸 것입니다.
# ex1.png
# 최종 압축 결과에 0이 4개, 1이 9개 있으므로, [4,9]를 return 해야 합니다.
# 입출력 예 #2

# 다음 그림은 주어진 arr을 압축하는 과정을 나타낸 것입니다.
# ex2.png
# 최종 압축 결과에 0이 10개, 1이 15개 있으므로, [10,15]를 return 해야 합니다.

import math
def solution(arr):
    count_0=0
    count_1=0
    l = int(math.log2(len(arr)))

    def dc(arr,l):
        nonlocal count_0
        nonlocal count_1
        
        if l<=1:
            new_arr = [arr[0][0],arr[0][1],arr[1][0],arr[1][1]]
            c = new_arr[0]
            if new_arr.count(c)==4:
                if c==0:
                    return 0
                elif c==1:
                    return 1
                else:
                    return 3
            else:
                count_0+=new_arr.count(0)
                count_1+=new_arr.count(1)
                return 3
        else:
            new_arr=[[],[],[],[]]
            for i in range(2**(l-1)):
                new_arr[0]+=[arr[i][:2**(l-1)]]
                new_arr[1]+=[arr[i][2**(l-1):2**(l)]]
                new_arr[2]+=[arr[i+2**(l-1)][:2**(l-1)]]
                new_arr[3]+=[arr[i+2**(l-1)][2**(l-1):2**(l)]]
            result = [dc(new_arr[0],l-1),dc(new_arr[1],l-1),dc(new_arr[2],l-1),dc(new_arr[3],l-1)]
            c= result[0]

            if result.count(c)==4:
                if c==0:
                    return 0
                elif c==1:
                    return 1
                else:
                    return 3
            else:
                count_0+=result.count(0)
                count_1+=result.count(1)
                return 3
    
    ans = dc(arr,l)

    if ans==0:
        return [1,0]
    elif ans==1:
        return[0,1]
    else:
        return [count_0,count_1]
    

# divide and conquer 알고리즘 문제. 다른사람 풀이. 코드가 훨씬 짧다.. arr를 굳이 나누어 각각 확인하지 않고, 배열의 첫번째 값과 일치하지
# 않는 수가 나올 경우에만 문제를 divide하고 answer list를 업데이트하여 문제를 풀었다. 배열의 첫번째 값과 모두 일치하면, 그대로 answer list에 업데이트한다.
# 내 알고리즘은 바텀업 방식이지만 이 풀이는 탑 다운 방식이다. 
# 바텀업 방식은 divide가 항상 n*n 배열에 대해 log2(n)번 일어난다.
# 탑다운 방식은 divide가 최소 0번(모든 수가 0또는 1인 경우) 최대 log2(n)번 일어난다.
# divide 이후의 알고리즘은, 바텀업 방식에서는 서브 배열들의 결과를 종합하는 과정이 있으나 탑다운 방식에서는 없다.
# 따라서 전체적인 알고리즘에서 탑다운 방식이 시간적으로 더 유리하고 공간 면에서도 좀 더 유리하다.


# def solution(arr):
#     answer = [0, 0]

#     def check(size, x, y):
#         if size == 1:
#             answer[arr[y][x]] += 1
#             return
#         else:
#             first = arr[y][x]

#             for dy in range(size):
#                 for dx in range(size):
#                     if first != arr[y + dy][x + dx]:
#                         check(size // 2, x, y)
#                         check(size // 2, x + size // 2, y)
#                         check(size // 2, x, y + size // 2)
#                         check(size // 2, x + size // 2, y + size // 2)
#                         return
#             answer[first] += 1
#     check(len(arr),0,0)


#     return answer


# 탑다운 방식 테스트 결과
# 테스트 1 〉	통과 (0.45ms, 10.2MB)
# 테스트 2 〉	통과 (0.35ms, 10.3MB)
# 테스트 3 〉	통과 (0.18ms, 10.1MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (140.04ms, 12.2MB)
# 테스트 6 〉	통과 (58.54ms, 12.2MB)
# 테스트 7 〉	통과 (40.54ms, 12.2MB)
# 테스트 8 〉	통과 (36.45ms, 12.2MB)
# 테스트 9 〉	통과 (38.36ms, 12.2MB)
# 테스트 10 〉	통과 (120.69ms, 19.2MB)
# 테스트 11 〉	통과 (0.12ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (45.85ms, 12.2MB)
# 테스트 14 〉	통과 (217.10ms, 19.1MB)
# 테스트 15 〉	통과 (199.16ms, 19.1MB)
# 테스트 16 〉	통과 (65.21ms, 12.2MB)

# 바텀업 방식 테스트 결과
# 테스트 1 〉	통과 (0.73ms, 10.5MB)
# 테스트 2 〉	통과 (1.40ms, 10.2MB)
# 테스트 3 〉	통과 (0.69ms, 10.4MB)
# 테스트 4 〉	통과 (0.33ms, 10.3MB)
# 테스트 5 〉	통과 (205.84ms, 14.7MB)
# 테스트 6 〉	통과 (255.74ms, 14.7MB)
# 테스트 7 〉	통과 (237.97ms, 14.6MB)
# 테스트 8 〉	통과 (237.07ms, 14.7MB)
# 테스트 9 〉	통과 (248.69ms, 14.7MB)
# 테스트 10 〉	통과 (957.90ms, 29.1MB)
# 테스트 11 〉	통과 (0.29ms, 10.2MB)
# 테스트 12 〉	통과 (0.17ms, 10.2MB)
# 테스트 13 〉	통과 (194.46ms, 14.8MB)
# 테스트 14 〉	통과 (797.29ms, 29.2MB)
# 테스트 15 〉	통과 (805.20ms, 29.3MB)
# 테스트 16 〉	통과 (241.63ms, 14.8MB)