#input = open("oefen.txt")
#letters = int(input())
#for _ in range(letters):
#    positie, woord = input().rstrip().split()
#    print(woord[int(positie) - 1])

# Read data from the file
#f = open("start.dat")
#lines = f.readlines()
#f.close()
# Process data in lines
#for line in lines:
#    #only read non-empty lines
#    if len(line.strip()) != 0:
#        columns = line.split("--")

f = open("oefen.txt")
lines = f.readlines()
f.close()
for line in lines:
    if len(line.strip()) != 0:
        columns = line.split(" ")
cijfers = lines
print(cijfers)