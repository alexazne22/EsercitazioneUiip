class Auto:
    def __init__(self, modello_p, cilindrata_p, cavalli_p, produttore_p, tipo_p):
        self.modello
        self.cilindrata
        self.cavalli
        self.produttore
        self.tipo

comando = input('Inserisci comando: ')
comando = int(comando)

lista = []
lista_test = [ Auto('x', 10, 5, 'y', 'u'), Auto('a', 5, 50, 'y', 'u')]
while comando != -1:
    if comando == 1: #Lettura
        print()
    if comando == 2: #Ricerca
        print()
    if comando == 3:#Occorrenza di un produttore
        print()
    if comando == 4:#Modello più cavalli
        print()
    if comando == 5: #Media delle cilindrate
        print()
    comando = input('Inserisci comando: ')
    comando = int(comando)