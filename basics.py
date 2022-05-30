import random

lotto = []
szám= 0
while szám < 5:
    lottószám = random.randint(1, 100)
    if lottószám not in lotto:
        lotto.append(lottószám)
        szám += 1

lotto.sort()
print('A lottószámok:', lotto)     
