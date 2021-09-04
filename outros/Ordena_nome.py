# recebe uma lista com n nomes e remove todos que possuei mais de 3 vogais

def verifica_nome(nome):
    ctd = 0
    for i in  nome:
        if i in "aeiouAEIOU":
            ctd += 1

    if ctd > 3:
        return True
    else:
        return False

def lista_a_verificar(nomes):
    for i in range(len(nomes)-1,-1,-1):
        if verifica_nome(nomes[i]):
            nomes.pop(i)
    return nomes

if __name__  == "__main__":
    lista_nomes = input("Informe os nomes a serem verificados: \nOs nomes devem ser preseguidos de vírgula e espaço"
                        " (Ex:Fulano, Ciclano) :").split(", ")

    print("Lista após a remoção dos nomes que estão contidos na regra>>", lista_a_verificar(lista_nomes[:]))
    print("Lista inicial>>", lista_nomes)