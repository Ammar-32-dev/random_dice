import random
min=1
max=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    #print("rolling the dices")
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll_again=input("Roll your dices ")