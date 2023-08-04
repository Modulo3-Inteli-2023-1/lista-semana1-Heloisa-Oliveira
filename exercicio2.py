# Código feito por Heloisa Cavalcanti Oliveira

#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    nova_lista = []
    soma = 0

    for i in lista:
        soma += i 
        nova_lista.append(soma)
    
    return nova_lista

# Teste a sua função aqui (caso ache necessário)











