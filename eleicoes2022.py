import urllib.request, json, time, sys

file = open('output.txt', mode='w')

def printout(out, writer):
  print(out)
  writer.write(out)

hora_anterior = ""
diff_anterior = 0

while True: 
  with urllib.request.urlopen("https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json") as url:
      data = json.load(url)
      hora = data['hg']

      apurado = data['pst']
      
      lula_nome = data['cand'][0]['nm']
      lula_votos = data['cand'][0]['vap']
      lula_porcent = data['cand'][0]['pvap']
      bozo_nome = data['cand'][1]['nm']
      bozo_votos = data['cand'][1]['vap']
      bozo_porcent = data['cand'][1]['pvap']
      diff = int(bozo_votos) - int(lula_votos)

      if hora != hora_anterior:
          printout(hora, file)
          printout(f"Urnas apuradas: {apurado}%", file)
          printout(f"{lula_nome}: {lula_votos} ({lula_porcent}%)", file)
          printout(f"{bozo_nome}: {bozo_votos} ({bozo_porcent}%)", file)
          printout(f"Diferença: {diff}", file)

      hora_anterior = hora
      diff_anterior = diff
      time.sleep(5)
