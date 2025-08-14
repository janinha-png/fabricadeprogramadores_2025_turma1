import random
Value = random.randint(0,2)

match Value:
    case 0:
        print("Zero!")
    case 1:
        print("Um!")
    case _:
        print("Inesperado!")
