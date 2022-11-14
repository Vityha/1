x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Исходный массив: ', x)
lenx = len(x)
change = 0
coun1 = 0
coun2 = 0
for i in range(1, lenx):
    if i % 2 == 0:
        coun2 +=1
    else:
        coun1 +=1
if coun1 > coun2:
    change = lenx
elif coun1 == coun2:
    change = lenx - 1
for i in range(lenx//2):
    if i % 2 != 0:
        el = x[i]
        x[i] = x[change-i]
        x[change-i] = el
print('Преобразованный массив: ', x)