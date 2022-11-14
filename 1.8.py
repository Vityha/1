def more_than_five(lst):
    spisok = []
    for i in lst:
        if abs(i) > 10:
            spisok.append(i)
    return spisok

lest=[5, 10, 15, -20, -500, 200, -51]
print(more_than_five(lest))