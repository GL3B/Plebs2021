f = open("oefen.txt")
lines = f.readlines()
f.close()
amount_lists = int(lines[0])
print(amount_lists)
lists = []
cijfers = []

""" Reads the input txt file and separates all values in a list """
for line in lines:
    if len(line.strip()) != 0:
        columns = line.split("\n")
        cijfers.append(columns[0])

index = 0

""" Creates the three separate lists  inside "lists" """
for number in range(1, amount_lists+1):
    lijst = [] # contains numbers per list e.g. [23,42,13]
    index +=1
    len_list = int(lines[index])
    for lijst_index in range(len_list):
        print(lijst_index)
        index +=1
        lijst.append(int(cijfers[index]))
    lists.append(lijst)
#print(lists)


i = 1
lijst_max = []
lijst_min = []


for individual_lists in lists:
    minimum = min(individual_lists)
    maximum = max(individual_lists)
    lijst_max.append(maximum)
    lijst_min.append(minimum)

   #print(individual_lists)
print(lijst_max)
print(lijst_min)

output = open("output.txt", "w")
for j in range(amount_lists):
    output.writelines(str(i)+ " " + str(lijst_min[j]) + " " + str(lijst_max[j]) + "\n")
    i +=1
output.close()
