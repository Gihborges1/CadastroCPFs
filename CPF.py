CPF=10
    
n=[]
R='Sim'
for i in range(CPF):
    CC=int(input("Insira o CPF "+str(i+1)+": "))
    n.append(CC)

#Ordenando
n.sort()
#Impressão
for i in range(CPF):
    print("CPF "+str(i+1)+":",n[i])
#Pesquisa
while R=='Sim':
    p=int(input("Qual CPF deseja consultar? "))
    acha=False
    comeco=0
    final=CPF-1
     
    while comeco<=final and acha==False:
        meio=(comeco+final)//2 
        if p==n[meio]:
            acha=True
        else:
            if p<n[meio]:
                final=meio-1
            else:
                comeco=meio+1
    if acha==True:
        print("O CPF "+str(p)+" foi localizada no elemento: ",meio+1)
    else:
        print("O CPF "+str(p)+" não foi localizada!")

    R=input("Deseja continuar? Responda com Sim ou Não: ")
print("Pesquisa Encerrada!")
