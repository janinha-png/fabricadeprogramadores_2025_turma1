tupla = ("a", "b", "c")
tupla
('a','b','c')
print(tupla)

tupla = 100,200,300
tupla
(100,200,300)
print(tupla)

L = [5,9,13,4,98,2,10,3,43,8]
for x, e in enumerate(L):
    print("%d / %d = %f" % (x, e, x/e))
    
for x, e in enumerate(L):
    print("%d X %d = %d" % (x, e, x*e))

for x, e in enumerate(L):
    print("%d - %d = %d" % (x, e, x-e))

for x, e in enumerate(L):
    print("%d + %d = %d" % (x, e, x+e))