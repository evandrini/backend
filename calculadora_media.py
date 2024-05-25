def calcular_media(notas):
  soma_notas = sum(notas)
  media = soma_notas / len(notas)
  return media

#Verificar se foi aprovado ou reprovado

def verificar_situacao(media):
  if media == 10:
    return "Parabéns, sua média é 10!"
  elif media >= 7:
    return "Aprovado"
  else:
    return "Reprovado"

notas = []

while True:
  nota = float(input("Digite uma nota entre 0 e 10: "))
  if 0 <= nota <= 10:
    notas.append(nota)
    continuar = input("Deseja adicionar outra nota? (s/n): ")
    if continuar.lower() != 's':
      break
  else:
    print("Erro. Digite uma nota entre 0 e 10.")

media_calculada = calcular_media(notas)
status_aluno = verificar_situacao(media_calculada)

print(f"As notas digitadas foram: {notas}")
print(f"A média do aluno é: {media_calculada:.2f}")
print(f"Situação do aluno: {status_aluno}")
