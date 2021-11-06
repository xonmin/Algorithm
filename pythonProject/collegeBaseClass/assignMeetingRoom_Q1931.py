# 백준 회의실 배정 1931
import sys

n = int(sys.stdin.readline())

meeting = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append([start, end])


meeting.sort(key=lambda x: (x[1],x[0]))

#meeting.sort(key=lambda x: x[1])
# 반례 -> 44,44,34,24,14 답 3이 2로 조회

#print(meeting)

end_meet = meeting[0]
ans = 1

for m in meeting[1:]:
    if m[0] >= end_meet[1]:
        ans += 1
        end_meet = m

print(ans)