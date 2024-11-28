def atividade1():
    #1 - Imprima a frase: Python na Escola de Programação da Alura.
    print('Python na Escola de Programação da Alura')

    #2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
    nome='Ingrid'
    ida=18
    print(f'Meu nome é {nome} e tenho {ida} anos')

    #3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
    print('A','L','U','R','A',sep='\n')

    #4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
    pi = 3.14159
    # Abordagem de f-string
    print(f'O valor arredondado de pi é: {pi:.2f}')
    # Abordagem de .format()
    print('O valor arredondado de pi é: {:.2f}'.format(pi))
    # Utilizando a função round()
    print('O valor arredondado de pi é:', round(pi, 2))


def atividade2():
    #1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
    a = int(input('insira um numero:'))
    if a%2==0:
        print('seu número é par!')
    else:
        print('seu número é ímpar!')

    #2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
    b=int(input('qual sua idade:'))
    if b <=12:
        print("vc ainda é nenem")
    elif 12<b<18:
        print("vc é muito chato")
    else:
        print('vc ja pode ser preso!')

    #3 - Solicite um nome de usuário e uma senha e use uma 
    # estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
    usuario_correto = "alura"
    senha_correta = "alura123"

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem sucedido!")
    else:
        print("Credenciais inválidas. Tente novamente.")
        
    #4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
    #Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    #Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    #Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    #Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    #Caso contrário: o ponto está localizado no eixo ou origem.
    x=int(input('de o valor de X:'))
    y=int(input('de o valor de Y:'))
    if x>0 and y>0:
        print('Seu plano cartesiano esta no primeiro quadrante')
    elif x<0 and y>0:
        print('Seu plano cartesiano esta no segundo quadrante')
    elif x<0 and y<0:
        print('Seu plano cartesiano esta no terceiro quadrante')
    elif x>0 and y<0:
        print('Seu plano cartesiano esta no quarto quadrante')
    else:
        print('seu ponto esta no ponto de origem')
