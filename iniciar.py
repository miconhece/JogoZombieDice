def contar_jogadores():
    """

        Condição para iniciar o jogo: Só é iniciado, caso seja informado que dois ou mais jogadores
        participarão.

        :return: Retorna o número de participantes.
        """
    while True:
        num_jogadores = int(input("Informe o número de jogadores: "))
        print("=" * 80)
        if num_jogadores <= 1:
            print("Necessário dois ou mais jogadores para iniciar a partida.".center(80))
            print("Convoque mais zumbis!".center(80))
            print("=" * 80)
            continue
        else:
            break
    return num_jogadores


def cadastrar_jogadores(num_jogadores):
    """

    Recebe o nome dos jogadores por input e armazena em uma lista.
    :param num_jogadores: Define quantidade de nomes que irá receber.
    :return: lista com nome dos jogadores.
    """
    nomes = []
    num = num_jogadores
    indice = 1
    while num > 0:
        nome = input(f"Informe o nome do {indice}º jogador: ").upper().strip()
        if nome in nomes:
            if input("Nome já cadastrado. Deseja alterar (s/n)? ").lower() == "n":
                continue
            else:
                nome = input(f"Informe o nome do {indice}º jogador: ").strip()
        nomes.append(nome)
        indice += 1
        num -= 1
    return nomes


def preparar_jogadores():
    """

    Exibe divisor zumbi para iniciar a partida.
    :return: Não possui retorno
    """
    print("            ______________            ".center(80))
    print("          /                \          ".center(80))
    print("  _____  |   ===      ===   |  _____  ".center(80))
    print(" /     \  \        \/       / /     \ ".center(80))
    print(" | | | <|  \    VVVVVVV    /  |> | | |".center(80))
    print(" V V V  \   |   |     |   |   /  V V V".center(80))
    print("     \   \  |   |     |   |  /   /    ".center(80))
    print("      \   \ \   \^^^^^/   | /   /     ".center(80))
    print("       \     -------------     /      ".center(80))
    print(f"      PREPAREM-SE PARA A PARTIDA!    ".center(80), '\n')
    print("="*80)


def dado_dificil():
    """

    Identifica o dado mais dificil de pontuar. Ele possui: 3 faces TIRO, 2 faces PASSO e apenas 1 face CEREBRO.
    :return: retorna com o nome correspondente a cor vermelha, carregando suas faces "TPTCTP"
    """

    return 'T', 'P', 'T', 'C', 'T', 'P'


def dado_intermediario():
    """

    Identifica o dado de dificuldade mediana. Ele possui 2 faces TIRO, 2 faces PASSO e 2 faces CEREBRO
    :return: retorna com o nome correspondente a cor amarela, carregando suas faces "PCTPCT"
    """

    return 'P', 'C', 'T', 'P', 'C', 'T'


def dado_facil():
    """

    Identifica o dado mais fácil de pontuar. Ele possui apenas 1 face TIRO, 2 faces PASSO e 3 faces CEREBRO
    :return: retorna com o nome correspondente a cor verde, carregando suas faces "CPCTCP"
    """

    return 'C', 'P', 'C', 'T', 'C', 'P'


def receber_tubo():
    """

    Constrói o tubo do jogo carregando os tipos de dado através das respectivas funções de cada dado. Armazena uma
    lista com 13 dados, sendo: 3 da cor VERMELHA, 4 da cor AMARELA e 6 da cor VERDE.
    :return: lista contendo os 13 dados.
    """
    dado_vermelho = dado_dificil()
    dado_amarelo = dado_intermediario()
    dado_verde = dado_facil()

    tubo = [dado_vermelho, dado_vermelho, dado_vermelho,
            dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
            dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde]

    return tubo


def iniciar_turno(jogador):
    """
    Informa o nome do jogador da rodada.
    :param jogador: Recebe a lista com o nome de todos os jogadores
    :return: Retorna o nome do jogador da vez.
    """
    nome = jogador
    print(f"Início do turno do zumbi \033[34m{nome}\033[m".center(90))
    print("="*80)


def fazer_jogada():
    """

    Recebe autorização para iniciar a partida.

    :return: Verdadeiro ou falso. Se falso, entra em looping.
    """
    jogando = True
    while True:
        lancar_dados = input("Iniciar jogada? Digite S para Sim e N para Não: ").upper().strip()
        print("="*80)
        if lancar_dados == "S":
            jogando = True
            break
        else:
            continue
    return jogando


if __name__ == "__main__":
    fazer_jogada()
