numeros = [7, 5, 3, -500, 1000]

# lista.sort()
# sorted(lista)

#print('Antes', numeros)
#numeros.sort(reverse=True)
#novos_numeros = sorted(numeros)

#print('Depois', novos_numeros)




















palavras = ['Valor', 'a', 'Roger', 'teste']


#print('Antes', palavras)
palavras.sort()
sorted(palavras)
#print('Depois', palavras)












listas_dentro_de_listas = [["roger", 22], ["teste", 99], ["valor", 10], ["truco", 33]]


from operator import itemgetter, attrgetter

from attr import attr
#print('Antes', listas_dentro_de_listas)
listas_dentro_de_listas.sort(key=itemgetter(1))
#print('Depois', listas_dentro_de_listas)









lista_de_mapas = [
    {"nome": "roger", "idade": 22},
    {"nome": "teste", "idade": 23},
    {"nome": "valor", "idade": 10}
]



#print('Antes', lista_de_mapas)
lista_de_mapas.sort(key=itemgetter('idade'))
#print('Depois', lista_de_mapas)






class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'<Class Pessoa {self.nome}, {self.idade}>'
     
lista_de_objetos = [
    Pessoa('Roger', 22),
    Pessoa('Romulo', 10),
    Pessoa('Jackson', 99),
]

print('Antes', lista_de_objetos)
lista_de_objetos.sort(key=attrgetter('idade'))
print('Depois', lista_de_objetos)