#Contador de caracteres em textos. Importante para conferir caracteres em textos ou senhas grandes.

print("\n")
print("Seja bem vindo ao contador de caracteres em textos")
print("\n")

texto = input("Por favor, digite o texto você deseja contar os caracteres: ")
contagem = 0
for caractere in texto:
    contagem+=1
print("\n")
print(f'Esse texto "{texto} tem {contagem} caracteres')
print("\n")
print('Gostou? Volte sempre quando precisar :)')