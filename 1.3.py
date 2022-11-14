from random import randint
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    else:
        return True

num = randint(1,1000)
print(num)
num2 = is_prime(num)
print(num2)