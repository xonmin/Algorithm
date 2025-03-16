# def solution1(score):
#     answer = 0
#
#     if score > 100:
#         answer += score // 100
#         score %= 100
#     if score > 50:
#         answer += score // 50
#         score %= 50
#     if score > 5:
#         answer += score // 5
#         score %= 5
#     answer += score
#
#     return answer
#
#
# def solution2(capacity, routes):
#     answer = True
#     way = [0 for _ in range(1001)]
#     for route in routes:
#         for i in range(route[1], route[2]):
#             way[i] += route[0]
#
#     if max(way) > capacity:
#         answer = False
#
#     return answer


def solution(pouches):
    answer = 0
    jellies = 'abcde'

    for jelly in jellies:
        scores = []

        for pouch in pouches:
            count_jelly = pouch.count(jelly)
            total = len(pouch)
            the_others = total - count_jelly
            score = count_jelly - the_others
            scores.append(score)

        scores.sort(reverse=True)

        current_count, pick = 0, 0
        for score in scores:
            if current_count + score > 0:
                current_count += score
                pick += 1
            else:
                break

        answer = max(answer, pick)

    return answer


if __name__ == '__main__':
    print()
