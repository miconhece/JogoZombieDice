def jogo(ranking):
    """
    Transforma os valores do dicionario ranking em uma lista. Extrai os pontos da lista e
    verifica qual a maior pontuacao.
    :param ranking: dicionario com pontuacao de todos os jogadores.
    :return: maior pontuacao acumulada.
    """
    dic = ranking
    lista = dic.values()
    lista_pontos = []
    lista_pontos.extend(lista)
    maior = -10000
    for i in lista_pontos:
        if i > maior:
            maior = i
    return maior


def vencedor(score):
    """
    Verifica pontuacao e faz a parada do looping do jogo, caso algum jogador tenha atingido 13 pontos ou mais.

    :param score: maior pontuacao possivel
    """
    maior = score
    if maior > 12:
        partida = False
    else:
        partida = True
    return partida


def geral(ranking, partida, score):
    """

    Exibe uma lista com a pontuação de todos os jogadores.

    :param score: recebe a maior pontuacao do jogo
    :param ranking: Recebe dict com nome  e pontos de cada jogador.
    :param partida: Recebe o parametro de que a partida foi encerrada. FALSE
    :return: não possui retorno.
    """
    pontos = score
    jogadores = ranking
    jogando = partida
    print("Eba! Alguém já comeu 13 cérebros ou mais!".center(80).upper())
    print("Fim de Jogo!".center(80).upper())
    print("=" * 80)
    if not jogando:
        vencedores = []
        for jogador in jogadores:
            print(f"{jogador} - Fez {jogadores[jogador]} pontos")
        for jogador in jogadores:
            if jogadores[jogador] == pontos:
                print("=" * 80)
                print(f"O vencedor foi o zumbi {jogador}".upper().center(80))
    print("="*80)

    print("Obrigada por jogar Zombie Dice".center(80))




