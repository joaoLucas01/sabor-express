import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False},
                {'nome':'pizza suprema', 'categoria':'pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar/desativar restaurantes')
    print('4. sair\n')

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurantes
    
    Inputs:
    - Nome do rstaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('cadastro de novos restaurantes')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('listando restaurantes')

    print(f'{'nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | {'status'}')
    print('-------------------------------------------------------')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()   

def alternar_estado_restaurante():
    exibir_subtitulo('alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('finalizando app...')

def voltar_ao_menu_principal():
    input('\npressione enter para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


     

def opcao_invalida():
    print('opcao inválida!')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida =  int(input('escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()  
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

    #match opcao_escolhida:
        #case 1:
        #    print('Adicionar restaurante')
        #case 2:
        #    print('Listar restaurantes')
        #case 3:
        #    print('Ativar restaurante')
        #case 4:
        #    print('Finalizar app')
        #case _:
        #    print('Opção inválida!')


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()