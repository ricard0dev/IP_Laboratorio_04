
'''
                PROGRAMA 3

                                        '''
from itertools import filterfalse
from pickle import FALSE

menu = {1 : {'Descricao' : 'Café e bolo de arroz ', 'preco' : 1.3},
        2 : {'Descricao' : 'Dois cafés e meia torrada', 'preco' : 2.2},
        3 : {'Descricao' : 'Meia de leite e tosta com manteiga', 'preco' : 3},
        4 : {'Descricao' : 'Galão com tosta com manteiga', 'preco' : 3.5},
        }

titulo = 'Menu de Pequeno Almnoco'
print('\n\n\n\n\n\n', titulo.center(100),
      '\n\n\t\t\tNumero do Menu \t | \t\t\t\t Descricao \t\t\t\t | \t Prco Unitario',
      '\n\t\t\t+--------------------------------------------------------------------+')

for chave, valor in menu.items():
        print('\t\t\t\t', chave, '\t\t\t |\t', valor['Descricao'], '\t\t\t\t|', valor['preco'], '$')

total = None
n = True
sub_total = 0
while n == True:
    opcao_menu = int(input('\nDigita a opcao escolhida : '))
    quantidade = int(input('Quantidade : '))
    print('1 - Inserir mais opcoes \n 2 - Terminar e aprezentar o total a pagar')

    sub_total = sub_total + menu[opcao_menu]['preco'] * quantidade

    if int(input('') == '1'):
        continue
    else:
        total = sub_total
        n = None

print("A respectiva despesa do cliente a pagar é:", total)
