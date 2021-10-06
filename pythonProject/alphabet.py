import sys
import collections

#백준 1987번 알파벳

r, c = map(int,sys.stdin.readline().split())

board = [list(sys.stdin.readline().split()) for _ in range(r)]

print(board)

