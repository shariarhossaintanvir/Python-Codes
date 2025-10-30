n = int(input())
count = 0

for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        count += 1

print(count)