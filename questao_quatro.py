c  = 0 
num_par = 2
num_impar = 1
numero =  int (input ("Quantos numeros da lista voce deseja verificar: "))
while c < numero:
    num = int (input("Digite o numero: "))
    
    if numero  % 2 == 0:
        print ("Esse numero e par")
        num_par += 1    

    else:
        print ("Esse numero e impar")
        num_impar += 1
    
    c+=1

print ("A quantidade de numeros pares e {num_par} e numeros impares e {num_impar}")