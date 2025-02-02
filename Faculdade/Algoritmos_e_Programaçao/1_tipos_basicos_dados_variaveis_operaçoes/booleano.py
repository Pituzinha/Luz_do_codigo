#Crie um programa que verifique se uma pessoa é maior de idade ou não, considerando a idade inserida pelo usuario. Usando a variavel boolean (verdadeira ou falsa).

idade = int (input ("Digite sua idade:"))
maioridade = idade >= 18
if maioridade:
    print ("Você é maior de idade.")
else:
    print("Você é menor de idade.")


#Peça ao usuario para inserir a idade e diga se ele é maior de idade (True) ou menor de idade (False).
idade = int (input ("Digite a sua idade:"))
maior_de_idade = idade >= 18
print (f"Maior de idade? {maior_de_idade}")
