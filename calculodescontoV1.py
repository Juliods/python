print("Calculadora de desconto")
print("V:1.0")
print("Insira o preço")
p = int(input())
print("insira a porcentagem desconto:")
x = int(input())
v = 100
res = (p*x)/v
c = p - res
print("O valor final com desconto é R$ %d" % c)
input("Pressione enter para sair")