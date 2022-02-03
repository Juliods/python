print("Calculadora de salário")
print("V:1.0")
print("Insira a quantidade do salário")
s = int(input())
print("Gratificação de 10%")
a = (10 * s) / 100 
st1 = a + s
#st1 = salário total mais os 10% de gratificação
b = (20 * st1) / 100
st2 = st1 - b
#st2 = salário total menos o imposto 
print("O salário total com os fatores considerados será de R$ %d" %st2)
input("Pressione enter para sair")