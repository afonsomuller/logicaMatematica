from random import randint
print('Sumiram 5 balas do tambor do meu revolver. Quem morreu?')
lista_dicas = ['Mark Chapman Saiu de Casa.', 
               'Os Beatles estão gravando.', 
               'Em 6 de Junho de 1944 aconteceu uma coisa engraçada', 
               'O Livro O Apanhador no Campo de Centeio ainda não foi proibido', 
               '4 balas atingiram o alvo', 
               '', 
               '', 
               '', 
               '', 
               '']
dica = str(input('Você quer uma dica aleatória? [S/N]')).upper()
if dica == 'S':
    dica_aleatória = randint(0,4)
    print(lista_dicas[dica_aleatória])
    lista_dicas.pop(dica_aleatória)