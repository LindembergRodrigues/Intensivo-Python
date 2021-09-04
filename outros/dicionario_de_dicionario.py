
nomes = input("Nomes separados por vírgula: ").split(",")
dic = {}
for nome in nomes:
    dic_aux = {}
    print(nome)
    dic_aux["sobrenome"] = input("Sobrenome: ")
    dic_aux["idade"] = input("Idade: ")
    dic_aux["endereco"] = input("Endereco: ")
    dic[nome] = dic_aux

for chaves in dic:

    print("{nome} {sobrenome}, tem {idade} anos e mora em {endereco}".format(
            nome=chaves, sobrenome=dic[chaves]["sobrenome"],
            idade=dic[chaves]["idade"], endereco=dic[chaves]["endereco"]))
