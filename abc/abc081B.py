n = input()
a = list(map(int, input().split()))
# ans = float("inf")
# for v in a:
#     ans = min(ans, list(reversed(bin(v))).index('1'))
# print(ans)
ans = 0
while True:
    oddFlg = False
    for v in a:
        if v % 2 == 1:
            oddFlg = True
    if oddFlg:
        break
    for i in range(len(a)):
        a[i] = a[i] / 2
    ans+=1

print(ans)