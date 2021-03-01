print("welkom")
print("Gilles ge kunt het niet")

letters = int(input())
for _ in range(letters):
    positie, woord = input().rstrip().split()
    print(woord[int(positie) - 1])

