# def solution(spell, dic):
#     len_spell = len(spell)
#     set_spell = set(spell)
#     for word in dic:
#         set_word = set(word)
#         if len(set_spell.intersection(set_word)) == len_spell:
#             tmp_lst = []
#             for s in word:
#                 if s in set_spell:
#                     tmp_lst.append(s)
#             if len(tmp_lst) == len_spell:
#                 return 1
#             else:
#                 continue
#         else:
#             continue
#     return 2

def solution(spell, dic):
    len_spell = len(spell)
    set_spell = set(spell)
    for word in dic:
        set_word = set(word)
        tmp_lst = []
        for s in word:
            if s in set_spell:
                tmp_lst.append(s)
        if len(set(tmp_lst)) == len_spell:
            return 1
        else:
            continue
    return 2