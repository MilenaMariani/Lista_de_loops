num = float(input ("Digite um numero"))
i = 0
continuar = 's'
menor = num
while continuar == 's':
    num = float(input ("Digite um numero"))
    if menor > num:
        menor = num

    continuar = (input ("Deseja continuar? [s/n]")) 
        
print(f"O menor numero e {menor}")