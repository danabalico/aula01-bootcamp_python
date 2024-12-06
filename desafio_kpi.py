# Escreva um programa em Python que solicita ao 
# usuário para digitar seu nome, o valor do seu salário mensal 
# e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e 
# informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

nome_usuario = input("Digite seu nome: ")
salario_usuario = float(input("Qual seu salario mensal? "))
bonus_usuario= float(input ("Qual a porcentagem do bonus que recebeu? "))
valor_do_bonus= CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")