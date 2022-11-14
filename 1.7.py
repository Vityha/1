for i in range(500):
  x = [int(a) for a in str(i)]
  for i in x:
    if i == 8:
      result = int(''.join(map(str, x)))
      if result % 7 == 0:
        print(result)