"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
usuario = str(input("Digite o usuario: "))
senha = str(input("Digite sua senha: "))

while usuario == senha:
    print("Usuario e senha nao podem ser iguais! Tente novamente.")
    usuario = str(input("Digite o usuario: "))
    senha = str(input("Digite sua senha: "))
else:
    print("Cadastrado com sucesso.")
    

























