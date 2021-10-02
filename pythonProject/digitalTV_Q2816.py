# 백준 2816번 디지털 티비
import sys

n = int(sys.stdin.readline())

channel_list = list()

for i in range(n):
    channel_list.append(sys.stdin.readline().strip())


# 1. 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
# 2. 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
# 3. 현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
# 4. 현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

kbs1_idx = channel_list.index('KBS1')
kbs2_idx = channel_list.index('KBS2')

ans = list()

for i in range(kbs1_idx):
    ans.append('1')
for i in range(kbs1_idx):
    ans.append('4')

if kbs1_idx > kbs2_idx: #kbs1 위로 올리다보면 kbs2 한 칸 아래로 갔을 것이기 때문
    kbs2_idx += 1

for i in range(kbs2_idx):
    ans.append('1')
for i in range(kbs2_idx-1): #두번쨰까지만 보내기
    ans.append('4')

print("".join(ans))