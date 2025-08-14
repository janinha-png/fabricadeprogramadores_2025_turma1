def oloko():
    L=[0,2,4,6,8,10,12,14,16,18]
    for joana in L:
        print(joana)

def caraca():
    L=["gato","vaca","cachorro"]
    for animais in L:
        for letra in animais:
            print(letra)


L=[3,6,10,8,-2,4,-23,9,-5,-90]
minimo=L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)

L=[3,6,10,8,-2,4,-23,9,-5,-90]
maximo=L[0]
for e in L:
    if e > maximo:
        maximo = e
print(maximo)

#for e in range(5,8):
#   print(e)

#for e in range(3,33,3):
#    print(e,end=" ")

nome= "joana"
idade= 15
grana= 51.34
print("%20s tem %010d anos e R$%f no bolso."%(nome,idade,grana))

