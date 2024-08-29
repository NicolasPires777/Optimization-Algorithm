pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'

voos = {}

for linha in open('C:/Users/nicol.DESKTOP-1V46I42/OneDrive/Documentos/Dev/optimization-algorithm/data/flights.txt'):
    origem, fim, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, fim), [])
    voos[(origem,fim)].append((saida, chegada, int(preco)))

print(voos)