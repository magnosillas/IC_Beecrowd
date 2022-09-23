
notas_validas = 0
media = 0

while notas_validas < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        notas_validas = notas_validas + 1
        media = media + nota
    else:
        print("nota invalida")

print(f"media = {media/2:,.2f}")
