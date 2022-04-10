import random
import iniciar


def exibir_status(tubo, jogada, vermelho, amarelo, verde):
    """
    O jogador pode realizar n jogadas em um mesmo turno. A função retorna a mensagem
    de acordo com a jogada do jogador.
    :param tubo: Recebe lista com dados do tubo
    :param jogada: Recebe o numero de vezes que o jogador fez jogada
    :param vermelho: Recebe dado vermelho
    :param amarelo: recebe dado amarelo
    :param verde: recebe dado verde
    :return: Não possui retorno
    """
    contar = iniciar.receber_tubo()
    tubo_atual = tubo
    controle = jogada
    dificil = vermelho
    medio = amarelo
    facil = verde

    if controle == 1:
        print(f"Você recebeu um tubo com {len(contar)} dados.         ".center(80))
        print(f"{contar.count(dificil)} dados \033[31mvermelhos\033[m   ".center(90))
        print(f"{contar.count(medio)} dados \033[33mamarelos\033[m    ".center(90))
        print(f"{contar.count(facil)} dados \033[32mverdes\033[m      ".center(90))
        print("=" * 80)
    else:
        print(f"Restam {len(tubo_atual)} dados no seu tubo".center(80))
        print(f"{tubo.count(dificil)} dados \033[31mvermelhos\033[m   ".center(90))
        print(f"{tubo.count(medio)} dados \033[33mamarelos\033[m    ".center(90))
        print(f"{tubo.count(facil)} dados \033[32mverdes\033[m      ".center(90))
        print("=" * 80)
    print(f"Esta é a sua {controle}º Jogada. Lance 3 dados!".center(80).upper())
    print("="*80)


def lancar_dados():
    """

    Recebe o tubo e sorteia aleatoriamente um dos seus dados.
    :return: Dado sorteado
    """
    tubo = iniciar.receber_tubo()
    dado_sorteado = random.choice(tubo)
    return dado_sorteado


def verificar_cor(sorteado, vermelho, amarelo, verde):
    """

    Recebe dado sorteado e as cores possíveis. Faz verificação da cor do dado, que pode ser: Vermelho, Amarelo ou Verde
    :param sorteado: recebe dado sorteado
    :param vermelho: recebe dado vermelho
    :param amarelo: recebe dado amarelo
    :param verde: recebe dado verde
    :return: Retorna tupla com a cor do dado
    """
    cor = sorteado
    dado = vermelho, amarelo, verde
    if cor == tuple("CPCTCP"):
        cor = "Verde"
    elif cor == tuple("PCTPCT"):
        cor = "Amarelo"
    elif cor == tuple("TPTCTP"):
        cor = "Vermelho"
    return cor


def desenhar_dado(cor):
    """

    Recebe a cor do dado sorteado e imprime um desenho com a cor do dado correspondente.
    :param cor: recebe a cor do dado
    :return: desenho com a cor do dado
    """
    cor_dado = cor
    while True:
        if input("Exibir a COR do dado? "
                 "Digite S para Sim e N para Não: ").upper().strip() == "S":
            if cor_dado == "Verde":
                print("\033[32m")
                print("   _________")
                print("  /\        \ ")
                print(" /  \  Verde \ ")
                print("/    \________\ ")
                print("\    /        / ")
                print(" \  /        / ")
                print("  \/________/")
                print("\033[m")
            elif cor_dado == "Amarelo":
                print("\033[33m")
                print("   _________")
                print("  /\        \ ")
                print(" /  \ Amarelo\ ")
                print("/    \________\ ")
                print("\    /        / ")
                print(" \  /        / ")
                print("  \/________/")
                print("\033[m")
            elif cor_dado == "Vermelho":
                print("\033[31m")
                print("   _________")
                print("  /\        \ ")
                print(" /  \Vermelho\ ")
                print("/    \________\ ")
                print("\    /        / ")
                print(" \  /        / ")
                print("  \/________/")
                print("\033[m")
        return "Dado Sorteado".center(15)


def verificar_face(sorteado):
    """

    Recebe dado sorteado e sorteia uma das faces possíveis. Que pode ser: T: Tiro, C: Cerebro ou P: Passo
    :param sorteado: dado sorteado
    :return: face sorteada.
    """
    dado_sorteado = sorteado
    face = random.choice(dado_sorteado)
    while True:
        if input("Ver a FACE do dado? "
                 "Digite S para Sim e N para Não: ").upper().strip() == "S":
            if face == "P":
                print("Sua vítima FUGIU!")
            elif face == "C":
                print("Você conseguiu comer um CEREBRO!")
            elif face == "T":
                print("Você levou um TIRO")
        print("-"*80)
        return face


def remover_dado(tubo_atual, sorteado):
    """

    Remove do tubo o dado sorteado
    :param tubo_atual: recebe tubo com todos os dados disponíveis.
    :param sorteado: dado a ser removido.
    :return: tubo com dado removido.
    """
    tubo = tubo_atual
    dado = sorteado
    tubo.remove(dado)
    return tubo


def parcial_tubo_cont(tubo):
    """

    Reinicia o tubo com a configuração inicial de dados.
    :param tubo: recebe tubo com dados disponíveis
    :return: Não possui retorno
    """
    tubo_atual = tubo
    for i in range(len(tubo_atual)):
        dado_restante = tubo_atual[i]
        if dado_restante == tuple("TPTCTP"):
            tubo_atual[i] = iniciar.dado_dificil()
        elif dado_restante == tuple("PCTPCT"):
            tubo_atual[i] = iniciar.dado_intermediario()
        elif dado_restante == tuple("CPCTCP"):
            tubo_atual[i] = iniciar.dado_facil()

