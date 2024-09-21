from lib.automacao import Automacao

collect = Automacao()
df = collect.Leitura_csv_mostras()
print(collect.Criar_csv())