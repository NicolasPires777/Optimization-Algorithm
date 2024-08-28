pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'

voos = {('BRU', 'FCO') : ['15:44', '18:55', 382]}

for linha in open('C:/Users/nicol.DESKTOP-1V46I42/OneDrive/Documentos/Dev/optimization-algorithm/data/flights.txt'):
    print(linha)