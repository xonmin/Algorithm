N = int(input())
connect_num = int(input())
connect_line =  list()

for i in range(connect_num):
    connect_line.append(list(map(int,input().split())))

visited = [False] * (N+1)


print(connect_line)