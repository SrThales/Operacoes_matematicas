tempo = int(input('Informe o tempo de viagem (em min):'))
velocidade = float(input('informe a velocidade média durante a viagem (em km/h):'))

horas = tempo/60
distancia = horas * velocidade

print('A distância percorrida foi de', distancia, 'km')
print('E o volume de combustível gasto foi de:', distancia/12)