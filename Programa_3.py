
'''
                PROGRAMA 2             

                                        '''

menu = {'1' : {'Descricao' : 'Café e bolo de arroz ', 'preco' : '1.3 €'},
        '2' : {'Descricao' : 'Dois cafés e meia torrada', 'preco' : '2.2 €'},
        '3' : {'Descricao' : 'Meia de leite e tosta com manteiga', 'preco' : '3€'},
        '4' : {'Descricao' : 'Galão com tosta com manteiga', 'preco' : '3.5€'},
        }

titulo = 'Menu de Pequeno Almnoco'
print('\n\n\n\n\n\n', titulo.center(100),
      '\n\n\t\t\tNumero do Menu \t | \t\t\t\t Descricao \t\t\t\t | \t Prco Unitario',
      '\n\t\t+------------------------------------------------------------------+')

for chave, valor in menu.items():
        print('\t\t\t\t', chave, '\t\t\t |\t', valor['Descricao'], '\t\t\t\t|', valor['preco'])
