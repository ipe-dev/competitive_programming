n = int(input())
cards = list(map(int, input().split()))
alice = 0
bob = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        alice += cards.pop(cards.index(max(cards)))
    if i % 2 == 0:
        bob += cards.pop(cards.index(max(cards)))
print(alice - bob)

# 別解 こっちの方が処理早い
# cards.sort(key=None, reverse=True)
# for i in range(0, n):
#     if i % 2 == 0:
#         alice += cards[i]
#     else:
#         bob += cards[i]
# print(alice - bob)