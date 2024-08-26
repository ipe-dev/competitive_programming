n = input()
a = list(map(int, input().split()))
# ans = float("inf")
# for v in a:
#     ans = min(ans, list(reversed(bin(v))).index('1'))
# print(ans)
ans = 0
while True:
    for v,i in enumerate(a):
        isInOdd = False
        if v % 2 == 1:
            isInOdd = True
        if isInOdd:
            break
    

print(ans)

    
