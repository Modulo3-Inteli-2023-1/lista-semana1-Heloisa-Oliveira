#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    count = 0
    for i in lista:
        for j in lista:
            if(j == i):
                count += 1
    
    if (count > len(lista)):
        return True
    
    else: return False







# Teste a sua função aqui (caso ache necessário)











