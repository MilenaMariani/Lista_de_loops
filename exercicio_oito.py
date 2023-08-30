num = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))
num3 = int (input("Digite o terceiro numero: "))

if num > num2 and num > num3:
    print (f"{num} e o maior entre o {num2} e {num3}")

elif num > num2 and num < num3:
    print (f"{num3} e o maior entre o {num} e {num2}")

elif num < num2 and num2 > num3:
    print (f"{num2} e o maior entre o {num} e {num3}")




