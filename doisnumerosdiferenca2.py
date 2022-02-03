print("doisnumerosdiferenca2")
print("V:1.0")
print("digite um número")
a = int(input())
print("digite outro número")
b = int(input())
if  a > b:
    c = a - b
else: 
    c = b - a 
c2 = (c * c)
print("A diferença entre os números ao quadrado é de %d" %c2)
input("Pressione enter para sair")