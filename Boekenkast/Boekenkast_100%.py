import sys

nb_of_tests = int(input())
output = []


def get_bookshelfs_sorted(w_bookshelf):
    for _ in range(len(w_bookshelf)):
        for i in range(len(w_bookshelf) - 1):
            if w_bookshelf[i] < w_bookshelf[i + 1]:
                w_bookshelf[i], w_bookshelf[i + 1] = w_bookshelf[i + 1], w_bookshelf[i]
    return w_bookshelf


def get_alfabetic(books):
    for _ in range(len(books)):
        for i in range(len(books) - 1):
            if books[i][1] > books[i + 1][1]:
                books[i], books[i + 1] = books[i + 1], books[i]
    return books


for test in range(1, nb_of_tests + 1):
    needed_shelfs = 0
    books = []
    line_info_bookshelfs = raw_input().split()
    nb_of_bookshelfs = line_info_bookshelfs[0]
    width_bookshelfs = []
    for bookshelf in range(1, int(nb_of_bookshelfs) + 1):
        width_bookshelfs.append(int(line_info_bookshelfs[bookshelf]))
    nb_of_books = int(input())
    for book in range(nb_of_books):
        book_info = raw_input().split(" ", 1)
        books.append(book_info)
    alfa = get_alfabetic(books)
    sorted_shelfs = get_bookshelfs_sorted(width_bookshelfs)
    if len(alfa) > 0:

        needed_shelfs = 1
        blijven_gaan = True
        for shelf in sorted_shelfs:
            while (blijven_gaan) & (len(alfa) > 0):
                if (len(alfa) > 0) & (len(sorted_shelfs) > 0):
                    if int(alfa[0][0]) <= int(sorted_shelfs[0]):
                        sorted_shelfs[0] -= int(alfa[0][0])
                        alfa.remove(alfa[0])
                    else:
                        needed_shelfs += 1
                        sorted_shelfs.remove(sorted_shelfs[0])
                else:
                        blijven_gaan = False
        if len(alfa) == 0:
            output.append(str(test) + " " + str(needed_shelfs) + "\n")
        else:
            output.append(str(test) + " " + "ONMOGELIJK" + "\n")
    else:
        output.append(str(test) + " " + str(needed_shelfs) + "\n")

sys.stdout.writelines(output)