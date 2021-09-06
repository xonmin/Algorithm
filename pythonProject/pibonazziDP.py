mem = [0 for i in range(46)]


def fibonazzi(n):
    if n<= 1:
        return n
    elif(mem[n]!= 0):
        return mem[n]
    else:
        mem[n] = fibonazzi(n-1) + fibonazzi(n-2)
        return mem[n]


n = int(input())

k = fibonazzi(n)
print(k)