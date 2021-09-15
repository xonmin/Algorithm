#1449번 수리공 항승

N, L = map(int,input().split())
holl_list = list(map(float,input().split()))
#로직
holl_list.sort()
holl_len = len(holl_list)

ans = 1
#만지려는 구멍 위치
idx = 0
now_holl = holl_list[0]
cover_len = (holl_list[0] - 0.5) + L
while True:
    if(idx == N):
        break
    if(cover_len >= holl_list[idx]+0.5):
        #다음꺼도 커버 가능 하다면
        idx += 1
    else :
        #다음꺼가 커버 안된다면 테이프 하나 증가
        cover_len = (holl_list[idx] - 0.5 + L)
        idx += 1
        ans += 1



print(ans)
#print(N,L,holl_list,repair_range)

