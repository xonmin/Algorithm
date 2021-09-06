def check(ans):
    for x,y,a in ans:
# 기둥 - 바닥 위에 / 보의 한쪽 끝 / 다른 기둥 위
        if a == 0:
            if y == 0 or [x-1, y, 1] in ans or [x,y,1] in ans or [x,y-1,0] in ans:
                continue
            else:
                return False
        elif a == 1:
            if [x,y-1,0] in ans or [x+1,y-1,0] in ans or ([x-1,y,1] in ans and [x+1,y,1] in ans) :
                continue
            else:
                return False
        return True



def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x,y,a,b = frame

        #설치
        if b == 1:
            answer.append([x,y,a])
            if check(answer) is False:
                answer.remove([x,y,a])
        #삭제
        else:
            answer.remove([x,y,a])
            if check(answer) is False:
                answer.append([x,y,a])

    answer.sort()
    return answer



n = int(input())
build_frame = []

for i in range(8):
    a = map(int,input().split(','))
    build_frame.append(list(a))

print(build_frame)
ans = solution(n,build_frame)
print(ans)