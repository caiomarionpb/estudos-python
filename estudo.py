#Exercícios de Python - nivel 1

#Crie uma variável chamada nome e atribua seu nome a ela. Em seguida, imprima essa variável.


name = "caio"
print(name)
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

#Crie as variáveis nome e idade e imprima ambas na mesma linha.

print("Digite seu nome e idade:")
name = str(input("Nome: "))
idade = int(input("Idade: "))
print(f"Olá {name}, você tem {idade} anos.")

#Atualize a variável idade para adicionar 1 ao valor atual e imprima o novo valor.

print("digite sua idade")
idade = int(input("Idade: "))
idade += 1  # Incrementa a idade em 1
print("você terá", idade, "anos no próximo ano")

#Crie uma variável altura com um valor decimal que represente sua altura. Imprima o valor e o tipo dessa variável.

print("digite sua altura")
altura = float(input("Altura: "))
print("sua altura é", altura, "metros")
print("o tipo da variável altura é", type(altura))

#Converta a variável idade para texto (string) e concatene com a frase " anos". Imprima o resultado.

idade = int(input("Digite sua idade: "))
idade_texto = str(idade)
print(f"você tem {idade_texto} anos")

#Crie duas variáveis primeiro_nome e sobrenome. Junte essas variáveis para formar o nome completo e imprima-o.

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = primeiro_nome + " " + sobrenome

print("Seu nome completo é:", nome_completo)

#Crie uma variável ano_nascimento, atribua seu ano de nascimento e calcule sua idade com base no ano atual (2025). Imprima o resultado.

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")

#Crie uma variável chamada frase com uma mensagem qualquer e imprima essa mensagem.

frase = "estudo de linguagem python usando variáveis"
print (frase)

#Crie uma variável com um número decimal e multiplique esse valor por 2. Imprima o resultado.

num1 = float (input("digite um numero decimal"))
resultado = num1 * 2
print(f"resultado: {resultado}")



#Estudo de Python - livel 2 (entrada de dados e e Operações Básicas)

#Peça para o usuário digitar seu nome e imprima uma mensagem de boas-vindas usando esse nome.

name = input("Digite seu nome: ")
print(f"Olá {name}, seja bem-vindo(a)!")

#Peça para o usuário digitar sua idade e mostre essa idade na tela.

idade = int(input("Digite sua idade: "))
print(f"Sua idade é {idade} anos.")

#Peça para o usuário digitar dois números inteiros e mostre a soma deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}.")

#Peça para o usuário digitar dois números decimais (float) e mostre a multiplicação deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
multiplicacao = num1 * num2
print(f"A multiplicação de {num1} e {num2} é {multiplicacao}.")

#Peça para o usuário digitar o ano de nascimento e calcule quantos anos ele tem (considerando o ano atual 2025). Imprima a idade.


ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")

#Peça para o usuário digitar a largura e a altura de um retângulo e calcule a área. Mostre o resultado.


largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = largura * altura
print(f"A área do retângulo é {area} metros quadrados.")

#Peça para o usuário digitar um número e informe se ele é positivo, negativo ou zero.


numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#Peça para o usuário digitar um número e mostre se ele é par ou ímpar.

num = int(input("Digite um número:"))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#Peça para o usuário digitar três números e mostre qual é o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num3
if num2 > maior: 
    maior = num2
if num1 > maior:
    maior = num1
print(f"o maior número é: {maior}")



#Peça para o usuário digitar seu salário e calcule um aumento de 10% se o salário for menor que 2000, caso contrário calcule um aumento de 5%. Mostre o novo salário.


salario = float(input("digite seu sálario: "))
porcentagem = salario

if salario < 2000:
    print("aumento de 10%")
    porcentagem += salario * 0.10
else:
    print("aumento de 5%")
    porcentagem += salario * 0.05



print(f"seu sálario com a porcentagem será de: {porcentagem}")










