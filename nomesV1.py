print("nomes")
print("V:1.0")
print("digite o nome")
nome = input()
print("digite a idade")
idade = int(input())
print("Digite o gênero")
genero = input()
linha = "%s tem %d anos e é do gênero %s" % (nome, idade, genero)
print(linha)
input("Pressione enter para sair")