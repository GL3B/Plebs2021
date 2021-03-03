import sys

alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def find_lowest_point(matrix):
    i = 0
    j = 0
    lowest_i = 0
    lowest_j = 0
    lowest_value = matrix[i][j]
    for row in matrix:
        j = 0
        for element in row:
            if element < lowest_value:
                lowest_value = element
                lowest_i = i
                lowest_j = j

            j+=1
        i +=1
    return (lowest_i, lowest_j)
#print(find_lowest_point(matrix))


def right(row, column, row_length, column_length):
    if column != (column_length -1):
        return (row, column+1)
    else:
        return None

def up(row, column, row_length, column_length):
    if row != 0:
        return (row-1, column)
    else:
        return None

def down(row, column, row_length, column_length):
    if row != (row_length -1):
        return (row + 1, column)
    else:
        return None

def left(row, column, row_length, column_length):
    if column != 0:
        return (row, column - 1)
    else:
        return None



def get_best_direction(row, column, current_value, row_length, column_length, matrix):
    lowest_dif = -1
    best_dir = None

    up1 = up(row, column, row_length, column_length)
    if up1 is not None:
        up_value = int(matrix[up1[0]][up1[1]])
        up_val_dif = up_value - current_value
    else:
        up_val_dif = -1

    down1 = down(row, column, row_length, column_length)
    if down1 is not None:
        down_value= int(matrix[down1[0]][down1[1]])
        down_val_dif = down_value - current_value
    else:
        down_val_dif = -1

    right1 = right(row, column, row_length, column_length)
    if right1 is not None:
        right_value = int(matrix[right1[0]][right1[1]])
        right_val_dif = right_value - current_value
    else:
        right_val_dif= -1

    left1 = left(row, column, row_length, column_length)
    if left1 is not None:
        left_value = int(matrix[left1[0]][left1[1]])
        left_val_dif = left_value - current_value
    else:
        left_val_dif = -1


    if (up_val_dif>0):
        if (up_val_dif < lowest_dif) | (lowest_dif < 0):
            lowest_dif = up_val_dif
            best_dir = up1

    if (down_val_dif>0):
        if (down_val_dif < lowest_dif) | (lowest_dif < 0):
            lowest_dif = down_val_dif
            best_dir = down1

    if (right_val_dif>0):
        if (right_val_dif < lowest_dif) | (lowest_dif < 0):
            lowest_dif = right_val_dif
            best_dir = right1

    if (left_val_dif>0):
        if (left_val_dif < lowest_dif) | (lowest_dif < 0):
            lowest_dif = left_val_dif
            best_dir = left1
    #print(best_dir)
    return best_dir, current_value+lowest_dif


weg = []
nb_of_tests = int(input())
matrix = []
for test in range(1, nb_of_tests + 1):
    size = input().split()
    for row in range(int(size[1])):
        line= input().split()
        matrix.append(line)
    best_dir = find_lowest_point(matrix)
    lowest_value = matrix[int(best_dir[0])][int(best_dir[1])]
    weg.append(best_dir)
    while best_dir is not None:
        best_dir, lowest_value = get_best_direction(int(best_dir[0]), int(best_dir[1]), int(lowest_value), int(size[1]), int(size[0]), matrix)
        if best_dir is not None:
            weg.append(best_dir)

    new_matrix = []
    for a in range(int(size[1])):
        new_matrix.append(str(test) + " ")
        for b in range(int(size[0])):
            if (a, b) not in weg:
                new_matrix[a] += '.'
            else:
                index = weg.index((a, b))
                new_matrix[a] += alfabet[index]
        new_matrix[a] += '\n'

sys.stdout.writelines(new_matrix)