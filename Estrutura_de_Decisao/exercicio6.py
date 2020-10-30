num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
num_3 = int(input("Digite o terceiro numero: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} é o maior entre os tres numeros.")
elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} é o maior entre os tres numeros.")
else:
    print(f"{num_3} é o maior entre os tres numeros.")

