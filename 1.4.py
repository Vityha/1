def reverse_list(lst):
  n = 3
  list = [0, 0, 0, 0]
  for i in lst:
    list[n] = i
    #print(lst)
    n=n-1
  return list

list = [8, 1, 0, 4]
print(list)
list = reverse_list(list)
print(list)