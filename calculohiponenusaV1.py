print("Calculadora de hipotenusa")
print("V:1.0")
print("Insira cateto oposto")
c1 = int(input())
print("insira o cateto adjacente:")
c2 = int(input())
c1q = (c1 * c1)
c2q = (c2 * c2)
hip2 = c1q + c2q
import math
hip = math.sqrt(hip2)
print ("A hipotenusa é igual á %d" %hip)
input("Pressione enter para sair")