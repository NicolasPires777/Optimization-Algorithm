from data.voos import voos
from main import pessoas, destino

def fitness_function(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo+=1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    return total_preco

agenda = [1,0, 3,2 ,7,1, 6,3, 2,4, 5,3]
var = fitness_function(agenda)
print(var)
# import sys
# print(sys.path)