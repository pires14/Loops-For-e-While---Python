#Conta se um número é par ou ímpar para possíveis crianças que ainda não sabem se um número é par um ímpar

print("\n")
print("Seja bem vindo")
print("\n")

numero = int(input("Por favor, digite um número: "))

if numero % 2 == 0: 
    print(f"O número digitado {numero} é par.")
else:
    print(f"O número digitado {numero} é ímpar.")