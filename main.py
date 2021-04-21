class Auto:
    def __init__(self, modello_p, cilindrata_p, cavalli_p, produttore_p, tipo_p):
        self.modello = modello_p
        self.cilindrata = cilindrata_p
        self.cavalli = cavalli_p
        self.produttore = produttore_p
        self.tipo = tipo_p

comando = input('Inserisci comando: ')
comando = int(comando)

lista = []
lista_test = [ Auto('x', 10, 5, 'y', 'u'), Auto('a', 5, 50, 'b', 'c')]
while comando != -1:
    if comando == 1: #Lettura
        print()

    if comando == 2: #Ricerca
        print()
    if comando == 3:#Occorrenza di un produttore
        print()
    if comando == 4:#Modello più cavalli
        cavalli_max = 0
        modello_max_cavalli = ''
        for c in lista_test:
            if c.cavalli > cavalli_max:
                cavalli_max = c.cavalli
                modello_max_cavalli = c.modello
        print('Il modello con più cavalli è ' + modello_max_cavalli)
    if comando == 5: #Media delle cilindrate
        print()
    comando = input('Inserisci comando: ')
    comando = int(comando)