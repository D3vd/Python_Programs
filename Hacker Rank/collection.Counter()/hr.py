from collections import Counter

n = int(input())
avail_shoe_sizes = Counter(map(int, input().split()))

x = int(input())

total = 0

for i in range(x):
    a, b = map(int, input().split())
    if avail_shoe_sizes[a] > 0:
        total += b
        avail_shoe_sizes[a] = avail_shoe_sizes[a] - 1

print(total)
