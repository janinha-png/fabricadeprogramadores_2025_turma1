def while1():
    x=1 
    while x<=3:
        print(x)
        x=x+1

def while2():
     x=1 
     while x<=100:
        print(x)
        x=x+1
def while3():
    x=50
    while x<=100:
        print(x)
        x=x+1

def while4():
    x=10
    while x>=0:
        print(x)
        x-=1
    print("fogo!")


def while5():
    fim=int(input("Digite o ultimo numero a imprimir:"))
    x=0
    while x<=fim:
        if x % 2==0:
            print(x)
        x=x+1

fim=int(input("Digite o ultimo numero a imprimir:"))
x=0
while x<= fim:
    if x % 2 == 1:
        print(x)
    x=x+1