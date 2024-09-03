n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d.sort(key=None, reverse=True)
ans = 0
current_v = 101
for v in d:
    if v < current_v:
        current_v = v
        ans += 1

print(ans)