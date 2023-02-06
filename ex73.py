#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
#Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')

for t in times:
    print(t)
    print('-=' * 15)

print(f'Os 5 primeiro são {times[0:5]}')

print(f'Os ultimos colocados são {times[-4:]}')

print(f'Times em ordem Alfabetica{sorted(times)}')

print(f'O Chapecoense está na {times.index("Chapecoense")+1} Posição')