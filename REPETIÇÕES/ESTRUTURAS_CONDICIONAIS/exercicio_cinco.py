num = int (input("Digite o primeiro lado: "))
num2 = int(input("Digite o segundo lado: "))
num3 = int (input("Digite o terceiro: "))

if num == num2 and num == num3:
    print("Esse triangulo e equilatero")

elif num == num2 and num != num3:
    print("Esse triangulo e isosceles")

elif num != num2 and num != num3:
    print("Esse triangulo e escaleno")        
