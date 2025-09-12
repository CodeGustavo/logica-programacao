import json
import senhas

cadastro = [
    {"nome": "Gustavo", "sobrenome": "Mesquita"},
    {"nome": "Isabelle", "sobrenome": "Souza"},
    {"nome": "Carlos", "sobrenome": "Almeida"},
    {"nome": "Fernanda", "sobrenome": "Silva"},
    {"nome": "João", "sobrenome": "Pereira"},
    {"nome": "Mariana", "sobrenome": "Oliveira"},
    {"nome": "Ricardo", "sobrenome": "Ferreira"},
    {"nome": "Beatriz", "sobrenome": "Costa"},
    {"nome": "André", "sobrenome": "Santos"},
    {"nome": "Juliana", "sobrenome": "Martins"},
    {"nome": "Paulo", "sobrenome": "Lima"},
    {"nome": "Camila", "sobrenome": "Barbosa"},
    {"nome": "Thiago", "sobrenome": "Ribeiro"},
    {"nome": "Larissa", "sobrenome": "Gomes"},
    {"nome": "Mateus", "sobrenome": "Carvalho"},
    {"nome": "Aline", "sobrenome": "Rocha"},
    {"nome": "Lucas", "sobrenome": "Araújo"},
    {"nome": "Patrícia", "sobrenome": "Mendes"},
    {"nome": "Felipe", "sobrenome": "Teixeira"},
    {"nome": "Renata", "sobrenome": "Batista"},
    {"nome": "Eduardo", "sobrenome": "Moura"}
]

user = input('Digite o Usuário: ')
password = input('Digite a senha: ')

if user == senhas.usuario1 and password == senhas.senha2 :
    while True:
            opcao = str(input('Adicionar ou remover cadastro ? A/R ')).upper()
            
            
            if opcao == 'A':

                nome = input('Digite o nome: ').capitalize()
                sobreNome = input('Digite o sobrenome: ').capitalize()
                novoCadastro = {'nome': nome, 'sobrenome': sobreNome}
                cadastro.append(novoCadastro)

                """with open("cadastro.json", "w", encoding="utf-8") as f:
                    print("Dados salvos em cadastro.json")"""
        
            elif opcao == 'R':
                while True:
                    remover = str(input('Remover qual cadastro? ')).capitalize()
                    if remover == 'N':
                                break
                    encontrado = False
                    for pessoa in cadastro:
                        if pessoa["nome"] == remover:
                            cadastro.remove(pessoa)
                            print(f'Cadastro de {remover} removido com sucesso!')
                            encontrado = True
                            break
                    if not encontrado:
                         print(f'Cadastro de {remover} não encontrado')

            elif opcao == 'N':
                 print('Saiu do sistema de cadastros')
                 break
            else:
                print(f"Opção inválida: {opcao}")
else:
     print('Você não tem permissão, só pode ver os usuários')            


entrada = input('Ver qual dado ? ')
campo = entrada.lower()


if campo in cadastro[0]:
    for pessoa in cadastro:       
       print(f"{campo.capitalize()}: {pessoa[campo]}")
elif campo == 'todos':
     for pessoa in cadastro:
          print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}")

else:
    print(f'Dado "{entrada}" inexistente')
