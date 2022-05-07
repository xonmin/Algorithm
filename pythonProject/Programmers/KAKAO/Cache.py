from collections import deque

'''
LRU
cache hit -> 1 miss -> 5
'''

answer = 0


def element_change(cache, cacheSize, item):
    global answer
    if cacheSize == 0:
        answer += 5
        return
    if item in cache:
        answer += 1
        cache.remove(item)
        cache.append(item)
    else:
        if len(cache) == cacheSize:
            cache.popleft()
            cache.append(item)
            answer += 5
        else:
            cache.append(item)
            answer += 5


def solution(cacheSize, cities):
    global answer
    answer = 0
    q = deque()

    for c in cities:
        c = str.lower(c)
        element_change(q, cacheSize, c)

    return answer
