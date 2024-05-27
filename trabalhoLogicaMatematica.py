from random import randint
from time import sleep
def darDica(lista):
    dica_aleatória = randint(0,4)
    print(lista_dicas[dica_aleatória])
    lista_dicas.pop(dica_aleatória)

pontuacao = 100
opcao_correta = 'C'
print('DETETIVE: VOCÊ CONSEGUE ADIVINHAR?')
sleep(2)
print(f'Regras \n'
      '1. Você inicia com 100 pontos. Cada vez que você pede uma dica, perde 9 pontos.\n'
      '2. A cada rodada, você pode pedir uma dica ou tentar adivinhar. Caso você erre, perde 50 pontos.\n'
      '3. Caso você acerte, você ganha 150 pontos.\n')
print('Sumiram 5 balas do tambor do meu revolver. Quem morreu?')
sleep(2)
lista_dicas = ['Mark Chapman Saiu de Casa.', 
               'São aproximadamente 22h e 50 minutos em Nova York',
               'A vítima é um cantor famoso', 
               'A motivação por trás do assassinato se dá por conta da discondância quanto à opiniões politicas e religiosas',
               'O assassino é um fã do cantor assassinado', 
               'O assassino não fugiu do local do crime. Ele esperou a polícia chegar, sentado na calçada.', 
               '4 balas atingiram o alvo', 
               'Alan Turing era Ateu e Homossexual', 
               'O Assassinato foi em frente ao predio onde a vitima morava', 
               'Esse caso aconteceu em 1980', 
               'Certa vez, em um show, um cantor mordeu a cabeça de um morcego.', 
               'A Arma usada no crime foi um revólver calibre 38']
lista_deducoes = ['Se Mark Chapman saiu de casa e são 22h e 50 minutos em Nova York, então 4 balas atingiram o alvo.',
                  'Se a vítima é um cantor famoso e'
                  'a motivação por trás do assassinato se dá por conta da discondância quanto à opiniões politicas e religiosas,'
                  'então o assassino é um fã do cantor assassinado.',
                  'O Assassino é fã do cantor assasinado e A arma usada no crime foi um revólver calibre 38',
                  'Se Alan Turing era Ateu e Homossexual, então um cantor mordeu a cabeça de um morcego em um show.',]
while pontuacao > 0:
    print(f'Sua pontuação atual é: {pontuacao}')
    if pontuacao <= 50:
        print(f'Atenção, sua pontuação está baixa. Caso você não consiga acertar logo, pode perder o jogo.')
    opcao = str(input('Você quer: \n [D] Uma dica aloeatória OU\n [A] Tentar adivinhar\n')).upper()
    if opcao == 'D':
        darDica(lista_dicas)
        pontuacao -= 9
    elif opcao == 'A':
        print(f'---'*20)
        print('Quem morreu? Digite a letra correspondente a sua resposta:')
        print('A) Papa João Paulo II', ' '*15, 'B) Alan Turing')
        print('C) John Lennon', ' '*22, 'D) Elvis Presley')
        resposta = str(input('Digite sua resposta: ')).upper()
        if resposta == opcao_correta:
            pontuacao += 150
            print(f'Parabéns, você acertou! Sua pontuação final foi: {pontuacao}')
            break
        else:
            pontuacao -= 50
            print(f'Opção errada! Perdeu 50 pontos:')

print('Fim do jogo!')
print(f'Pontuação final: {pontuacao}')
