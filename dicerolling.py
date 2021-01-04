import random as rnd 
rolleddice=[]
def roller(rollnum,rolleddice):
    rolleddice=[]
    while not 1<=rollnum<=3:
            rollnum=int(input("please enter the count of dices you want to roll(please enter 1,2 or 3, please enter quit to quit the program): "))
    for i in range(rollnum):
        rolleddice.append(rnd.randint(1,6))
    print(rolleddice)
while True:
    rollnum=int(input("please enter the count of dices you want to roll(please enter 1,2 or 3 to roll, please enter 0 to quit the program): "))
    if rollnum==0:
        break
    roller(rollnum,rolleddice)