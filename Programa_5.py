
'''
                PROGRAMA 4

                                        '''

'''
Escreva a função conta_vogais, que recebe uma cadeia de caracteres correspondente ao
nome de um ficheiro, lê esse ficheiro, linha a linha, e calcula quantas vezes aparece cada
uma das vogais. A função devolve um dicionário cujas chaves são as vogais e os valores
associados correspondem ao número de vezes que a vogal aparece no ficheiro. Por
exemplo,

>>> conta_vogais(‘testevogais.txt’)
{‘a’: 36, ‘u’: 19, ‘e’: 45, ‘i’:16, ‘o’: 28}

PROGRAMA 5

Rua Patrice Lumumba, CP 648 – 2110 Mindelo – São Vicente – CABO VERDE
https://um.edu.cv – e-mail geral@um.edu.cv – Telefone: +238.2326810 – Fax: +238.2325132

NIF: 562770755 mod 00X.24

Enunciado
Escreva a função junta_ficheiros_ordenados, que recebe três cadeias de caracteres, que
correspondem a nomes de ficheiros. Os dois primeiros ficheiros, contêm números,
ordenados por ordem crescente, contendo cada linha dos ficheiros apenas um número. A
função produz um ficheiro ordenado de números (contendo um número por linha)
correspondente à junção dos números existentes nos dois ficheiros. Este ficheiro
corresponde ao terceiro argumento da função. Para cada um dos ficheiros de entrada, a
função só lê uma linha de cada vez. A sua função não pode utilizar algoritmos de
ordenação. Por exemplo, se o ficheiro fich1 contiver:
37
38
5
123.0
789
1200
2345
e o ficheiro fich2 contiver:
1
2
123
456.0
e se for produzida a interacção:
>>> junta_ficheiros_ordenados (‘fich1’, ‘fich2’, ‘fich3’)
>>>
O ficheiro fich3 conterá:
1
2
5
123.0
123
456.0
789
1200
2345
'''

def conta_vogais(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
