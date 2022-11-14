from random import randint
s = 0
def season(month):
    if month <= 6:
        if month <=3:
            print("Это зима")
        else:
            print("Это весна")
    elif month <= 9:
        print("Это лето")
    else:
        print("Это осень")
s = randint(1,12)
print(s)
s = season(s)