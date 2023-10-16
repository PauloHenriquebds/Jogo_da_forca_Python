from biblioteca import frase
rept = 's'
while rept == 's':
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]

    import random
    palavra = random.choice(palavras)

    tentativas = 6
    letras_corretas = []
    letras_erradas = []

    while tentativas > 0:
        print(frase(palavra, letras_corretas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if set(letras_corretas) == set(palavra):
                print("Parabéns! Você venceu. A palavra é:", palavra)
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letras erradas:", " ".join(letras_erradas))
            print("Tentativas restantes:", tentativas)

    if tentativas == 0:
        print("Você perdeu. A palavra era:", palavra)
    rept = input("Deseja repetir?: ").lower()
else:
    print("Jogo finalizado")
