input = list(map(int, input().split()))
n = input[0]
a = input[1]
b = input[2]

ans = 0
def sumDigit(i: int):
    result = 0
    while i > 0: 
        result += i % 10 
        i = int(i / 10)   
    return result

for n_value in range(1, n + 1):
    result = sumDigit(n_value)
    if (a <= result) and (result <= b):
        ans += n_value
print(ans)