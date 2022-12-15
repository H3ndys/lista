menor_de_idade=[]
faixa_ideal=[]
idade_superior=[]
var=(input("informe seu nome:"))
var1=int(input("informe sua idade por favor:"))
if var1<=18:
    menor_de_idade.append(var)
    print("seu nome foi adicionado á lista de menor de idade:",menor_de_idade)
elif var1<=45:
    faixa_ideal.append (var)
    print("seu nome foi adicionada á lista faixa ideal:", faixa_ideal)
elif var>60:
    idade_superior.append(var)
    print("seu nome foi adivionado á lista de idade superior:", idade_superior)
elif var1>45 and var1<60:
    print("Idade invalida")