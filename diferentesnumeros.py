print("númerosdiferentes")
print("V:1.0")
print("digite um número")
a = int(input())
print("digite outro número")
b = int(input())
c = (a * a)
d = (b * b)
if  c > d:
    e = c - d
else: 
    e = d - c 
print("A diferença entre os números ao quadrado é de %d" %e)
input("Pressione enter para sair")