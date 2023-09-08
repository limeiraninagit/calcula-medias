def inputNotas():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    return [n1, n2, n3, n4]

def calculaMedia(notas):
    somaNotas = 0
    for nota in notas:
        somaNotas += nota # somaNotas = somaNotas + nota
    return somaNotas / len(notas)


notas = inputNotas()
media = calculaMedia(notas)

if media >= 7:
    print("APROVADO! Nota: " + str(media))
else:
    print("VOCE FOI PARA A FINAL!\n\n")
    notas = inputNotas()
    mediaAntiga = media
    media = calculaMedia(notas)
    novaMedia = (media + mediaAntiga) / 2

    if novaMedia >= 5:
        print("APROVADO! Media: " + str(novaMedia))
    else:
        print("REPROVADO! Media: " + str(novaMedia))
