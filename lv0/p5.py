# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 <numer1, denom1, numer2, denom2 < 1,000
# 입출력 예
# numer1	denom1	numer2	denom2	result
# 1	2	3	4	[5, 4]
# 9	2	1	3	[29, 6]
# 입출력 예 설명
# 입출력 예 #1

# 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
# 입출력 예 #2

# 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

def solution(numer1, denom1, numer2, denom2):
    numer_a = numer1*denom2 + numer2*denom1
    numer_b = denom1*denom2

    while(True):
        trigger = 1
        if numer_a < numer_b:
            z = numer_a
        else:
            z = numer_b
        for x in range(2,z+1):
            if numer_a%x==0:
                if numer_b%x==0:
                    numer_a = int(numer_a/x)
                    numer_b = int(numer_b/x)
                    trigger = 2
                    break
        if trigger ==2:
            continue
        else:
            break
    return [numer_a,numer_b]

## 자기 자신으로 나누는 것도 가능하다.