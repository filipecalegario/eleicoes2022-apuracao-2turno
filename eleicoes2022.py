import urllib.request, json, time

hora_anterior = ""

while True: 
  with urllib.request.urlopen("https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json") as url:
      data = json.load(url)
      hora = data['hg']
      
      lula_nome = data['cand'][0]['nm']
      lula_votos = data['cand'][0]['vap']
      bozo_nome = data['cand'][1]['nm']
      bozo_votos = data['cand'][1]['vap']
      diff = int(bozo_votos) - int(lula_votos)

      if hora != hora_anterior:
        print(f"{lula_nome}: {lula_votos}")
        print(f"{bozo_nome}: {bozo_votos}")
        print(f"{hora} Diferença: {diff}")

      hora_anterior = hora
      time.sleep(5)
