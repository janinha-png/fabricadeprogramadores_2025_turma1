def tabuada():
    n=int(input("Tabuada de:"))
    x=1
    while x <=100:
        print(n,"x",x,"=",x*n)
        x=x+1
tabuada()

s=0
while True:
    v=int(input("Digite um numero a somar ou 0 para sair:"))
    if v==0:
        break
    s=s+v
print(s)

