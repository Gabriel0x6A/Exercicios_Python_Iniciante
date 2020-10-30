"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = input("Nota: ")
nota = float(nota)

while nota < 0 or nota > 10:
    print("Valor invalido, Tente novamente!")
    nota = input("Nota: ")
    nota = float(nota)
else:
    print(f"{nota} Correta!")





























