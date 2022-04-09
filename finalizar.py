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


def acumulado(placar):
    placar_atual = placar
    lista = []
    pontos_cerebro = placar_atual.get("cerebro")
    lista.append(pontos_cerebro)
    pontos_tiro = placar_atual.get("tiro")
    lista.append(pontos_tiro)
    pontos_passo = placar_atual.get("passo")
    lista.append(pontos_passo)
    receber_placar = tuple(lista)
    return receber_placar


def marcar_tiro(placar_atual):
    dano_sofrido = placar_atual.get("tiro")
    return dano_sofrido


def marcar_pontos(placar_atual):
    pontos = placar_atual.get("cerebro")
    return pontos


def mensagem_pontuacao(dano):
    dano = dano
    print("Você conseguiu até agora:".center(80))
    # Informa a parcial de dados sorteados até o momento #

# placar = {"cerebro": 0, "passo": 0, "tiro": 0}


def placar_cerebro(placar):
    pontuacao = placar
    while True:
        if pontuacao[0] == 1:
            print("Comer 1 cérebro!".center(80))
            break
        elif pontuacao[0] > 1:
            print(f"Comer {pontuacao[0]} cérebros!".center(80))
            break
        elif pontuacao[0] < 1:
            print("Não comer nenhum cérebro!".center(80))
            break
    return pontuacao


def placar_tiro(placar):
    pontuacao = placar
    while True:
        if pontuacao[2] > 0:
            print(f"Dano = {pontuacao[2]} de 3. Cuidado!".center(80))
            break
        elif pontuacao[2] == 0:
            print("Não levar dano! Parabéns!".center(80))
            break
    return pontuacao


def placar_passo(placar):
    pontuacao = placar
    while True:
        if pontuacao[1] == 1:
            print("Deixar 1 vítima fugir!".center(80))
            break
        elif pontuacao[1] > 1:
            print(f"Deixar {pontuacao[1]} vítimas fugirem!".center(80))
            break
        elif pontuacao[1] < 1:
            continue
    return pontuacao


def jogar_novamente():
    print("-"*80)
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


def final_turno(start):
    turno = start
    if not turno:
        print("Turno Encerrado. ")
        print("="*80)
    return turno


def pontuacao_final(jogador, pontos):
    pass
