def vencedor(ranking, rodada):
    n_rodada = rodada
    if n_rodada > 0:
        dic = ranking
        lista = dic.values()
        lista_pontos = []
        lista_pontos.extend(lista)
        maior = -10000
        for i in lista_pontos:
            if i > maior:
                maior = i
        if maior > 12:
            partida = False
            print("Jogo Encerrado! Já temos um ganhador".center(80).upper())
            print("="*80)
        else:
            partida = True
        return partida


def classificacao_geral(ranking, partida):
    jogadores = ranking
    jogando = partida
    if not jogando:
        for jogador in jogadores:
            print(f"{jogador} - Fez {jogadores[jogador]} pontos")
    print("="*80)
    print("Obrigada por jogar Zombie Dice".center(80))




