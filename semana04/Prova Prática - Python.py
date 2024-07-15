def posicao(longi_inicia, longi_destino, vel, g_longi = 111):
  longi_viagem = longi_destino - longi_inicia
  dist_viagem = longi_viagem * g_longi
  horas_viagem = dist_viagem / vel
  dias_int = horas_viagem // 24


  kmD = vel * 24
  grausD = kmD / g_longi

  dia = 1
  while dia <= dias_int:
    posicao_dia = longi_inicia + grausD * dia
    print(f'No final do dia {dia}, a posição do navio é {posicao_dia:.2f} graus de longitude.')
    dia += 1
  
  print(f'No final do dia {dia}, a posição do navio é {longi_destino} graus de longitude.')

posicao(10, 210, 100)
print()
posicao(10, 360, 200)