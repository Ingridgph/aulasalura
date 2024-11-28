import os

restaurantes = ['Pizza', 'Sushi']

def exibirnome():
    print('🍧⟆Ꭿᑲᗝᖇ ᕮⲭᖰᖇ∈⟆⟆🍕\n')

def finalizar():
    exbir_subtitulos('Finalizando app')

def menu():
    print('1.Cadastre seu restaurante')
    print('2.Liste restaurante')
    print('3.Ative restaurante')
    print('4.Sair\n')

def exbir_subtitulos():
    os.system('cls')
    print(texto)
    print()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def invalida():
    print('Escolha apenas numeros de 1 ao 4\n')
    voltar_menu()

def cadastrar_restaurante():
    exbir_subtitulos('cadastrando restaurantes')
    nome_do_restaurante = input('Qual o nome do restaurante que deseja cadastrar?')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!' )
    voltar_menu()

def listar_restaurantes():
    exbir_subtitulos('listando restaurantes')
    for restaurante in restaurantes:
            print(f'.{restaurante}')
    voltar_menu()

def ecolher():    
    try:  
        opçao = int(input('Escolha uma opção:'))
        if opçao==1:
            cadastrar_restaurante()
        elif opçao==2:
            listar_restaurantes()
        elif opçao==3:
            print('ativar restaurante')
        elif opçao==4:
            finalizar()
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