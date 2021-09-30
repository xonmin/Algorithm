# 백준 1759 암호 만들기
import sys
from itertools import combinations
#최소 두 개 이상의 자음
#최소 한 개 이상의 모음
l, c = map(int,sys.stdin.readline().split())

alpha_list = sys.stdin.readline().split()

aeiou = set(['a', 'e', 'i', 'o', 'u'])
ans = []
alpha_list = set(alpha_list)

# 모음 교집합으로 구하기
# 최소 한 개
input_collections = aeiou & alpha_list
# 자음 - 차집합으로 구하기
# 최소 두 개
input_consonants = alpha_list - input_collections

input_consonants = list(input_consonants)

input_collections = list(input_collections)
for i in range(1, l):
    if(l-i < 2):
        continue

    temp_collection = combinations(input_collections,i);

    for coll in temp_collection:
        temp_consonant = combinations(input_consonants, l - i);
        for cons in temp_consonant:
            candidate_key = coll + cons
            candidate_key = list(candidate_key)
            candidate_key.sort()
            ans.append("".join(candidate_key))

ans.sort()
for _ in ans:
    print(_)