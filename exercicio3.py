# Código feito por Heloisa Cavalcanti Oliveira

#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista_de_listas):
    soma = 0

    for lista in lista_de_listas:
        for i in lista:
            soma += i

    return soma

# Teste a sua função aqui (caso ache necessário)











