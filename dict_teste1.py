lista = {"nome":"Gustavo","sobreNome":"Mesquita"}
campo = input("Adicione a um campo: ")
valorCampo = input(f"{campo} : ")

lista[campo] = valorCampo

verTipo = input("Ver o tipo de lista? (S/N)").upper()


if verTipo == "S":
    tipoLista = type(lista)
    print(f'A lista é do tipo: ',tipoLista)
elif verTipo == 'N':
    print('Você não quis ver o tipo de lista')
print(lista)