
from collections import deque
# 보드의 크기
# 백준 3190번 뱀 
N = int(input())
mat = [[0]*N for _ in range(N)]
# 가보지 않은 곳 0 , 뱀이 차지하고 있는 지역 1, 사과가 있는 곳 2

# 사과의 개수
K  = int(input())
apple_X = list()
apple_Y = list()

# 뱀의 길이 1 , 뱀의 움직임 초기 오른쪽(D)
for _ in range(K) :
    x, y =  map(int, input().split())
    mat[x-1][y-1] = 2

snake_move_count = int(input())

snake_move_time = list()
snake_move_direction = list()
for _ in range(snake_move_count):
    X, C = input().split()
    snake_move_time.append(int(X))
    snake_move_direction.append(C)
# input 종료

snake_location = deque([])

rangeX = [0,1,0,-1]
rangeY = [-1,0,1,0]


# 뱀 대가리 이동 변화  함수
def turn(direct, con):
    if (con == "L"):
        direct = (direct-1) % 4
    else:
        direct = (direct +1) % 4
    return direct

direction = 1
time = 1
y,x = 0,0
mat[y][x] = 1
snake_location.append([0,0])

while True:
    y, x = y+rangeY[direction],x+rangeX[direction]
    if(x<= -1 or x>= N or y <= -1 or y>= N or mat[y][x] == 1):
        break
    else:
        if not mat[y][x] == 2: # 사과가 없을 때
           temp_y,temp_x = snake_location.popleft()
           mat[temp_y][temp_x] = 0 # 뱀 꼬리 이동
        snake_location.append([y,x])
        mat[y][x] = 1

        if time in snake_move_time:
            i = snake_move_time.index(time)
            direction = turn(direction,snake_move_direction[i])
        time +=1



print(time)


