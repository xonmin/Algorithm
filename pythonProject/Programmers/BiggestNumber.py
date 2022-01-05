
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers_str = sorted(numbers , key=lambda x: str(x) * 3,reverse=True)
    return str(int("".join(numbers_str)))



print(solution([6, 10, 2]))
solution([3, 30, 34, 5, 9])
print(solution([1,10,100,1000]))
print(solution([0,0,0,0]))