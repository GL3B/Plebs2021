import sys
nb_lists = int(input())
lists = []
for _ in range(nb_lists):
    lijst = []
    for k in range(int(input().rstrip().split()[0])):
        lijst.append(int(input().rstrip().split()[0]))
    lists.append(lijst)
i = 1
lijst_max = []
lijst_min = []

for individual_lists in lists:
    minimum = min(individual_lists)
    maximum = max(individual_lists)
    lijst_max.append(maximum)
    lijst_min.append(minimum)

output = open("output.txt", "w")
for j in range(nb_lists):
    output.writelines(str(i)+ " " + str(lijst_min[j]) + " " + str(lijst_max[j]) + "\n")
    i +=1
output.close()

out = open("output.txt")
out1 = out.readlines()
out.close()

sys.stdout.writelines(out1)

