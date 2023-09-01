c = 0
num= int(input ("Quantos numero deseja verificar? : "))

maior = 0

while c < num:
    numeros = int (input("Digite o numero desejado: ")) 

    if numeros > maior:
        maior = numeros
        

    c +=1

print(maior)
