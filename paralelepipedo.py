print("Calculadora de equação do segundo grau")
print("V:1.0")
print("Insira a variável a")
a = float(input())
print("Insira a variável b")
b = float(input())
print("Insira a váriavel c")
c = float(input())
delta = (b*b) -( 4 * a * c)
import math
x1 = ((-b + math.sqrt((b*b)-4 * a * c)))/(2 * a)
x2 = ((-b - math.sqrt((b*b)-4 * a * c)))/(2 * a)
print("As raízes da equação serão %.2f e %.2f" %(x1, x2)) 