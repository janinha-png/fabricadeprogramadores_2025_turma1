L=[]
while True:
    n=(input("DIgite uma palavra(pare sai):"))
    if n == ("pare"):
        break
    L.append(n)
x=0
while x <len(L):
    print(L[x])
    x=x+1