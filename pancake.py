import math
import time

def pancakes(numberOfPeople, perPerson):

    def roundint(value, base=5):
        return int(value) - int(value) % int(base)


    totalPancakes = numberOfPeople * perPerson

    # Step 1: Declare quantities of ingredients needed
    # From experience, the original recipe makes around 8 decent-size pancakes, hence the division

    bakingPowder = math.ceil((10/8)*totalPancakes)        #         Original recipe asks for 2.5 tsp = 10g (4g/tsp)
    roundint(bakingPowder)

    salt = math.ceil(totalPancakes/8)                     #         In theory, this will assign 1 pinch of salt per 8 pancakes (i.e. 16 pancakes = 2 pinches)

    sugar = math.ceil((4/8)*totalPancakes)                #         Original recipe asks for 1 tsp = 10g (4g/tsp)
    teaspoonsOfSugar = math.ceil(sugar/4)

    eggs = math.ceil((2/8)*totalPancakes)                 #         Original recipe asks for 2 eggs per 8 pancakes

    butter = math.ceil((30/8)*totalPancakes)              #         Original recipe asks for 30g of melted and cooled butter
    butter = roundint(butter)

    milk = math.ceil((300/8)*totalPancakes)               #         Original recipe asks for 300ml of milk
    milk = roundint(milk)

    flour = math.ceil((225/8)*totalPancakes)              #         Original recipe asks for 225g of flour
    flour = roundint(flour)

    # Step 2: Print out recipe

    print("Since you are cooking for " + str(numberOfPeople) + " people, this recipe will make " + str(totalPancakes) + " pancakes, enough for " + str(perPerson) + " each.")

    time.sleep(1)

    print("In a blender, mix together:")

    print()
    time.sleep(0.5)
    print(str(bakingPowder) + " grams of baking powder")

    print()
    time.sleep(0.5)
    print(str(salt) + " pinch(es) of salt")

    print()
    time.sleep(0.5)
    print(str(teaspoonsOfSugar) + " teaspoon(s) of sugar")

    print()
    time.sleep(0.5)
    print(str(eggs) + " large egg(s)")

    print()
    time.sleep(0.5)
    print(str(butter) + " grams of butter, melted and cooled")

    print()
    time.sleep(0.5)
    print(str(milk) + " ml of milk")

    print()
    time.sleep(0.5)
    print(str(flour) + " grams of flour")
    
    print()
    print()
    print()
    time.sleep(2)
    print("This will make the perfect amount of batter. Once fully combined, generously ladle into a pan to create discs")
    print("around 15cm in diameter. Once bubbles appear, flip the pancakes and cook until golden and top with whatever you wish")




x = int(input("How many people are you cooking for? : "))
y = int(input("How many pancakes would you like per person? (2-3 recommended) : "))
pancakes(x,y)

