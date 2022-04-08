import random
import iniciar


def exibir_status(jogada, vermelho, amarelo, verde):
    contar = iniciar.receber_tubo()
    controle = jogada + 1
    dificil = vermelho
    medio = amarelo
    facil = verde
    if controle == 1:
        print(f"Você recebeu um tubo com {len(contar)} dados. Sendo:")
        print(f"{contar.count(dificil)} dados vermelhos")
        print(f"{contar.count(medio)} dados amarelos")
        print(f"{contar.count(facil)} dados verdes")
        print(f"Boa sorte!")
    else:
        print(f"Restam {len(contar)} dados no seu tubo")
    print(f"Esta é a sua {controle}º rodada".upper())


def lancar_dados():
    tubo = iniciar.receber_tubo()
    dado_sorteado = random.choice(tubo)
    return dado_sorteado


def verificar_cor(sorteado, vermelho, amarelo, verde):
    cor = sorteado
    dado = vermelho, amarelo, verde
    if cor == "CPCTCP":
        cor = "Vermelho"
    elif cor == "PCTPCT":
        cor = "Amarelo"
    elif cor == "TPTCTP":
        cor = "Verde"
    return cor


def desenhar_dado(cor):
    cor_dado = cor
    if cor_dado == "Vermelho":
        print("   _________")
        print("  /\        \ ")
        print(" /  \  Verde \ ")
        print("/    \________\ ")
        print("\    /        / ")
        print(" \  /        / ")
        print("  \/________/")
    elif cor_dado == "Amarelo":
        print("   _________")
        print("  /\        \ ")
        print(" /  \ Amarelo\ ")
        print("/    \________\ ")
        print("\    /        / ")
        print(" \  /        / ")
        print("  \/________/")
    elif cor_dado == "Verde":
        print("   _________")
        print("  /\        \ ")
        print(" /  \Vermelho\ ")
        print("/    \________\ ")
        print("\    /        / ")
        print(" \  /        / ")
        print("  \/________/")
    return "Dado Sorteado".center(15)


def verificar_face(sorteado):
    dado_sorteado = sorteado
    face = random.choice(dado_sorteado)
    return face


def remover_dado(tubo_atual, sorteado, face):
    tubo = tubo_atual
    dado = sorteado
    tubo.remove(dado)
    return tubo


