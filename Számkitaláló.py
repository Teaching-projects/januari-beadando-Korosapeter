import random

csúcs = input("adj meg egy számot")

random_szám = random.randint(0,csúcs)
kitalált = 0

while True:
    kitalált += 1
    tipp = input("találd ki:")


    if tipp == random_szám:
       print("eltaláltad")
    elif tipp > random_szám:
       print("főlé tippeltél")
    else:
        print("alá tippeltél")
      

