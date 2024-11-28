import os

restaurantes = ['Pizza', 'Sushi']

def exibirnome():
    print('🍧⟆Ꭿᑲᗝᖇ ᕮⲭᖰᖇ∈⟆⟆🍕\n')

def menu():
    print('1.Cadastre seu restaurante')
    print('2.Liste restaurante')
    print('3.Ative restaurante')
    print('4.Sair\n')

def invalida():
    print('Escolha apenas numeros de 1 ao 4\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('cadastro de novo restaurante🎉:\n')
    nome_do_restaurante = input('Qual o nome do restaurante que deseja cadastrar?')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!' )
    input('\nDigite uma tecla para voltar ao menu principal:')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes\n')
    for restaurante in restaurantes:
            print(f'.{restaurante}')


    input('\nDigite uma tecla para voltar ao menu principal:')
    main()


def ecolher():    
    try:  
        opçao = int(input('Escolha uma opção:'))

        def fin():
            os.system('cls')
            print('finalizando app')

        if opçao==1:
            cadastrar_restaurante()
        elif opçao==2:
            listar_restaurantes()
        elif opçao==3:
            print('ativar restaurante')
        elif opçao==4:
            fin()
        else:
            invalida()
    except:
        invalida()

def main():
    os.system('cls')
    exibirnome()
    menu()
    ecolher()


if __name__=='__main__':
    main()