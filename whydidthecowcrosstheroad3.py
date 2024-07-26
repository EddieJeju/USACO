import sys

input = sys.stdin.readline
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())

cows = []

for i in range(n):
  cows.append(list(map(int, input().split())))

cows.sort()
current_time = 0
for c in cows:

  if current_time > c[0]:
    current_time += c[1]
  else:
    current_time = c[0] + c[1]

print(current_time)
