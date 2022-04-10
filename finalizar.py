def pontuar_jogada(placar, face):
    """

    Recebe a face sorteada e atribui um ponto por tipo.
    :param placar: dicionario para armazenar pontuacao
    :param face: carrega face sorteada
    :return: placar_atual = placar com atribuição de pontos.
    """
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
    """

    Armazena em uma tupla, a pontuação acumulada do turno do jogador.
    :param placar: recebe o placar com os pontos da jogada
    :return: Retorna pontuacao em forma de tupla.
    """
    placar_atual = placar
    lista = []
    pontos_cerebro = placar_atual.get("cerebro")
    lista.insert(0, pontos_cerebro)
    pontos_tiro = placar_atual.get("tiro")
    lista.insert(2, pontos_tiro)
    pontos_passo = placar_atual.get("passo")
    lista.insert(1, pontos_passo)
    receber_placar = tuple(lista)
    return receber_placar


def marcar_tiro(placar):
    """

    Armazena isoladamente a pontuacao de tiros, para verificacao do dano do jogador.
    :param placar: Recebe o placar com todos os pontos da rodada.
    :return: Retorna quantidade de dano sofrido.
    """
    dano_sofrido = placar.get("tiro")
    return dano_sofrido


def marcar_pontos(placar):
    """
    Armazena isoladamente a pontuacao de cerebros, para verificacao dos pontos no turno do jogador.
    :param placar: Recebe o placar com todos os pontos da rodada.
    :return: Retorna quantidade de pontos acumulados.
    """
    pontos = placar.get("cerebro")
    return pontos


def mensagem_pontuacao():
    """
    Mensagem da pontuação ao final da jogada.
    :return: Não possui retorno
    """
    print("Você conseguiu até agora:".center(80))


# placar = {"cerebro": 0, "passo": 0, "tiro": 0}


def placar_cerebro(placar):
    """

    Verifica no dicionário de pontuacao, os pontos correspondentes a face cerebro.
    Retorna mensagem conforme pontuação

    :param placar: dicionário com a pontuação do turno
    :return: Não possui retorno
    """
    pontuacao = placar
    while True:
        if pontuacao[0] == 1:
            print("Comer 1 cérebro!".center(80))
            break
        elif pontuacao[0] > 1:
            print(f"Comer {pontuacao[0]} cérebros!".center(80))
            break
        elif pontuacao[0] < 1:
            print("Não comer nenhum cérebro".center(80))
            break
    return pontuacao


def placar_tiro(placar):
    """

     Verifica no dicionário de pontuacao, os pontos correspondentes a face tiro
     Retorna mensagem conforme pontuação
    :param placar: dicionário com a pontuação do turno
    :return: não possui retorno
    """
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
    """

     Verifica no dicionário de pontuacao, os pontos correspondentes a face tiro
     Retorna mensagem conforme pontuação
    :param placar: dicionário com a pontuação do turno
    :return: Não possui retorno
    """
    pontuacao = placar
    while True:
        if pontuacao[1] == 1:
            print("Deixar 1 vítima fugir!".center(80))
            break
        elif pontuacao[1] > 1:
            print(f"Deixar {pontuacao[1]} vítimas fugirem!".center(80))
            break
        elif pontuacao[1] < 1:
            break
    return pontuacao


def jogar_novamente():
    """

    Verifica se o jogador deseja continuar jogando. Através das opções "S" para sim e "N" para não.
    :return: Retorna "S" ou "N"
    """
    print("-"*80)
    continuar = input("Deseja jogar novamente? Digite S para sim e N para não: ").strip().upper()
    print("-" * 80)
    return continuar


def contar_dados(restam):
    """

    Verifica a quantidade de dados restantes no tubo/copo e verifica se jogador pode continuar jogando.
    :param restam: variavel que faz leitura dos dados no copo
    :return: start para verdadeiro ou falso.
    """
    dados_restantes = restam
    if dados_restantes <= 3:
        start = False
        print("Dados insuficientes para mais uma rodada. Aguarde o seu próximo turno!")
    else:
        start = True
    return start


def final_turno(start):
    """

    Mensagem de encerramento do turno.
    :param start: recebe a condicional de permanecer jogando ou encerramento.
    :return: retorna start
    """
    turno = start
    if not turno:
        print("Turno Encerrado. ")
        print("="*80)






