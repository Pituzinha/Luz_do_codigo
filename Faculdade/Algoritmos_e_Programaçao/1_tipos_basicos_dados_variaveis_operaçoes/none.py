#Crie um programa que defina uma variavel como none inicialmente e depois verifique se ela contém algum valor. Se não atribua um valor a ela e imprima o novo valor.

variavel = None
if variavel is None:
    print ("A variável não tem valor.")
    variavel = "Agora tem um valor!"
    print (f"A variável agora é: {variavel}")
else:
    print (f"A variável já tem um valor: {variavel}")


#Crie uma variavel com o valor none e depois atribua um nome a ela.
nome = None
print(f"Valor inicial: {nome}")
nome = input("Digite seu nome:")
print(f"Agora o nome tem valor: {nome}")