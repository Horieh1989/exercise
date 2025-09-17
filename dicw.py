import random
dice=[1,2,3,4,5,6]
#dice=random.randint(1,6)
sum=0
for i in range (100):
    dice=random.randint(1,6)
    if dice==6:
        print("you rolled a 6!")
        sum=sum+dice
print(f"the sum of 100 dice rolls is {sum}")
    
