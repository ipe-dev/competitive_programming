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