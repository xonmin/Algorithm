from itertools import combinations

def solution(users, emoticons):
    # 가입자 늘리기
    # 판매액 늘리기
    candidate_rate = [40, 30, 20, 10]
    sale_com = [emoticons, candidate_rate]
    sale_emo = combinations(emoticons, candidate_rate)
    sale_ = [x,y for x, y ]
    for i in



print(solution([[40, 10000], [25,10000]], [7000, 9000]))