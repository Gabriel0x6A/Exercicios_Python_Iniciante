"""
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("Digite seu nome, ele deve conter 4 ou mais caracteres:  ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade, deve estar entre 0 e 150: "))

salario = int(input("Digite seu salario: "))
while salario <= 0:
    salario = int(input("Digite seu salario novamente, ele deve ser maior que 0: "))

sexo = input("Informe seu sexo[f ou m]: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo invalido, Informe seu sexo novamente: ")

estado_civil = input("Informe seu estado civil[s, c, v, d]: ")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Informe seu estado civil apenas: s, c, v, d: ")
    
    




































