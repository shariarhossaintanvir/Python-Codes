t = int(input())
for _ in range(t):
    sticks = list(map(int, input().split()))
    if sticks[0] == sticks[1] == sticks[2] == sticks[3]:
        print("YES")
    else:
        print("NO")