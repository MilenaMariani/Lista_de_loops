ano = int (input("Digite o ano que queira saber: "))

if (ano % 4 ==0 or ano %100 !=0) or ano %400 ==0  :
    print (f"{ano} nao e bissexto")

else:
    print(f"{ano} e bissexto")    
