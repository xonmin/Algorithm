
test_num = int(input())


def findP(n):
    if(n == 0):
        return 0
    elif( 0<n<=3):
        return 1
    return test_arr[n-3] +test_arr[n-2]

test_arr = [0,1,1,1]

for i in range(4,100):
    test_arr.append(test_arr[i-3] + test_arr[i-2])

for _ in range(test_num):
    n = int(input())
    pn = findP(n)
    print(pn)






