print("Calculadora de reajuste")
print("V:1.0")
print("Insira o salário")
p = int(input())
print("insira a porcentagem do reajuste:")
x = int(input())
v = 100
res = (p*x)/v
c = p - res
print("O valor final com desconto é R$ %d" % c)
input("Pressione enter para sair")