# 시저 암호
# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.
# 입출력 예
# s	n	result
# "AB"	1	"BC"
# "z"	1	"a"
# "a B z"	4	"e F d"

# def solution(s, n):
#     abc_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,
#                 'f':5,'g':6,'h':7,'i':8,'j':9,
#                 'k':10,'l':11,'m':12,'n':13,'o':14,
#                 'p':15,'q':16,'r':17,'s':18,'t':19,
#                 'u':20,'v':21,'w':22,'x':23,'y':24,
#                 'z':25
#                }
#     ABC_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,
#                 'F':5,'G':6,'H':7,'I':8,'J':9,
#                 'K':10,'L':11,'M':12,'N':13,'O':14,
#                 'P':15,'Q':16,'R':17,'S':18,'T':19,
#                 'U':20,'V':21,'W':22,'X':23,'Y':24,
#                 'Z':25
#                }
#     ott_dict = {0:'a',1:'b',2:'c',3:'d',4:'e',
#                 5:'f',6:'g',7:'h',8:'i',9:'j',
#                 10:'k',11:'l',12:'m',13:'n',14:'o',
#                 15:'p',16:'q',17:'r',18:'s',19:'t',
#                 20:'u',21:'v',22:'w',23:'x',24:'y',
#                 25:'z'
#                 }
#     OTT_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',
#                 5:'F',6:'G',7:'H',8:'I',9:'J',
#                 10:'K',11:'L',12:'M',13:'N',14:'O',
#                 15:'P',16:'Q',17:'R',18:'S',19:'T',
#                 20:'U',21:'V',22:'W',23:'X',24:'Y',
#                 25:'Z'
#                 }
#     answer = ''
#     for alpha in s:
#         if alpha.isupper():
#             num0 = ABC_dict[alpha]
#             num0+=n
#             answer+=OTT_dict[num0%26]
#         elif alpha.islower():
#             num0 = abc_dict[alpha]
#             num0+=n
#             answer+=ott_dict[num0%26]
#         else:
#             answer+= alpha
#     return answer

def solution(s, n):
    abc_str = 'abcdefghijklmnopqrstuvwxyz'
    ABC_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for alpha in s:
        if alpha.isupper():
            num0 = ABC_str.index(alpha)
            num0+=n
            answer+= ABC_str[num0%26]
        elif alpha.islower():
            num0 = abc_str.index(alpha)
            num0+=n
            answer+=abc_str[num0%26]
        else:
            answer+= alpha
    return answer


## 해시방식이 2.9ms, 배열 방식이 1.5ms로 배열방식이 더 빨랐다. 예상 밖 이였다.

# 다른 사람 풀이를 보고 보완한 풀이. 유니코드를 이용해서 알파벳 리스트를 따로 만들지 않고 풀었다.
# def solution(s, n):
#     answer = ''
#     for alpha in s:
#         if alpha.isupper():
#             base = ord('A')
#             num0 = ord(alpha) - base
#             num0+=n
#             answer+= chr(num0%26+base)
#         elif alpha.islower():
#             base = ord('a')
#             num0 = ord(alpha) - base
#             num0+=n
#             answer+= chr(num0%26+base)
#         else:
#             answer+= alpha
#     return answer