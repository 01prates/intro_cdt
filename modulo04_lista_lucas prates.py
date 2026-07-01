''' 
modulo04_lista_lucasprates.py





'''



frutas_delicia = ['mexerica', 'maça', 'uva', 'banana', 'laranja']

print('-' * 40)

print('\n bem vindo à nossa loja de frutas! \n')
print(frutas_delicia)  # ['mexerica', 'maça', 'uva', 'banana', 'laranja']

fruta_nova = input('Digite o nome da fruta que deseja adicionar: \n')

frutas_delicia.append(fruta_nova)  # adicionando a fruta digitada na lista frutas_delicia


print('-' * 40)

print(f'\n Fruta {fruta_nova} adicionada com sucesso! \n')
print(frutas_delicia)  # ['mexerica', 'maça', 'uva', 'banana', 'laranja', 'fruta_nova']
