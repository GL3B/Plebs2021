import sys

nb_lists = int(input())
lists = []
for _ in range(nb_lists):
    lijst = []
    len_list = input()
    for k in range(int(len_list)):
        value = input()
        lijst.append(int(value))
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