a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for countA in range(a + 1):
    for countB in range(b + 1):
        for countC in range(c + 1):
            sumA = 500 * countA
            sumB = 100 * countB
            sumC = 50 * countC
            if sumA + sumB + sumC == x:
                ans += 1
print(ans)