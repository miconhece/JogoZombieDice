def pontuar_jogada(placar, face):
    face_sorteada = face
    placar_atual = placar
    if face_sorteada == "C":
        placar_atual["cerebro"] += 1
    elif face_sorteada == "T":
        placar_atual["tiro"] += 1
    elif face_sorteada == "P":
        placar_atual["passo"] += 1
    return placar_atual


def marcar_tiro(placar_atual):
    dano_sofrido = placar_atual.get("tiro")
    return dano_sofrido


def mensagem_pontuacao():
    print("Você conseguiu até agora:")
    # Informa a parcial de dados sorteados até o momento #


def placar_cerebro(placar):
    pontuacao = placar.get("cerebro")
    while True:
        if pontuacao == 1:
            print("Comer 1 cérebro!")
            break
        elif pontuacao > 1:
            print(f"Comer {pontuacao} cérebros!")
            break
        elif pontuacao < 1:
            print("Não comer nenhum cérebro!")
            break
    return pontuacao


def placar_tiro(placar):
    pontuacao = placar.get("tiro")
    while True:
        if pontuacao == 1:
            print("Levar 1 tiro!")
            break
        elif pontuacao > 1:
            print(f"Levar {pontuacao} tiros!")
            break
        elif pontuacao < 1:
            print("Não levar tiro! Parabéns!")
            break
    return pontuacao


def placar_passo(placar):
    pontuacao = placar.get("passo")
    while True:
        if pontuacao == 1:
            print("Deixar 1 vítima fugir!")
            break
        elif pontuacao > 1:
            print(f"Deixar {pontuacao} vítimas fugirem!")
            break
        elif pontuacao < 1:
            continue
    return pontuacao


def jogar_novamente():
    continuar = input("Deseja jogar novamente? Digite S para sim e N para não: ").strip().upper()
    print("-" * 80)
    return continuar


def contar_dados(restam):
    dados_restantes = restam
    if dados_restantes <= 3:
        start = False
        print("Dados insuficientes para mais uma rodada. Aguarde o seu próximo turno!")
    else:
        start = True
    return start
