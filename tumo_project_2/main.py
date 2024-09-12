import random
def random_number():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    return die_1,die_2
x,y =random_number()
sum_of_dies = x+y
def  playgame(sum_of_dies):
    if sum_of_dies in [7,11]:
        print("rolling a die....")
        print(f'the sum of dies is {x} + {y} = {sum_of_dies}')
        print("you won")

    elif sum_of_dies in [2,3,12]:
        print("rolling a die....")
        print(f'the sum of dies is {x} + {y} = {sum_of_dies}')
        print("casino wins")
    else:
        print("you need to roll again")
        print("rolling a die...")
        goal = sum_of_dies
        print(f"your goal is {goal}")
        while True:

             x,y= random_number()
             sum_with_rolling = x+y
             if sum_with_rolling ==goal:
                 print("rolling a die....")
                 print(f"your goal value is {x} + {y} ={sum_with_rolling}")
                 print("you won")
                 break
             elif sum_with_rolling ==7:
                 print("rolling a die.....")
                 print(f"your goal value is {x} + {y} ={sum_with_rolling}")
                 print("casino wins")
                 break


playgame(sum_of_dies)




