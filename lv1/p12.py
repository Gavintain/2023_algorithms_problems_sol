# 둘만의 암호
# 문제 설명
# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
# skip에 있는 알파벳은 제외하고 건너뜁니다.
# 예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

# 두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ s의 길이 ≤ 50
# 1 ≤ skip의 길이 ≤ 10
# s와 skip은 알파벳 소문자로만 이루어져 있습니다.
# skip에 포함되는 알파벳은 s에 포함되지 않습니다.
# 1 ≤ index ≤ 20
# 입출력 예
# s	skip	index	result
# "aukks"	"wbqd"	5	"happy"
# 입출력 예 설명
# 입출력 예 #1
# 본문 내용과 일치합니다.

def solution(s, skip, index):
    answer=''
    old_abc_str = 'abcdefghijklmnopqrstuvwxyz'
    new_abc_str=''
    for x in old_abc_str:
        if x in skip:
            pass
        else:
            new_abc_str+=x
    table_length = len(new_abc_str)
    for alphabet in s:
        num = new_abc_str.index(alphabet)
        answer+=new_abc_str[(num+index)%table_length]
    return answer

# 다른 사람 풀이. 스트링 모듈에 소문자관련 패키지가 있는 것을 처음 알았다.

# from string import ascii_lowercase

# def solution(s, skip, index):
#     result = ''

#     a_to_z = set(ascii_lowercase)
#     a_to_z -= set(skip)
#     a_to_z = sorted(a_to_z)
#     l = len(a_to_z)

#     dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

#     for i in s:
#         result += a_to_z[(dic_alpha[i] + index) % l]

#     return result