def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Por favor, nao utilize zeros!")
    except:
        print("\033[91m Algo deu errado...")
    else:
        print(f"Seu resultado é: {result}")
    finally:
        print("\033[92m Vamos de novo?")
divide(13,0)
divide("a","b")
divide("a",1)
divide(-1,-2)
