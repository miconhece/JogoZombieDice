def contar_jogadores():
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
    numero = num_jogadores
    nomes = []
    if numero > 1:
        for i in range(numero):
            nome = input(f"Digite o nome do {i+1}º jogador: ").upper().strip()
            nomes.append(nome)
        print("="*80)
    return nomes


def salvar_nome(jogadores):
    nomes = jogadores
    nome = 0
    for i in range(len(nomes)):
        nome = nomes[i]
    return nome


def listar_jogadores(nomes):
    nome_jogadores = tuple(nomes)
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
    return nome_jogadores


def dado_dificil():
    vermelho = "TPTCTP"
    return vermelho


def dado_intermediario():
    amarelo = "PCTPCT"
    return amarelo


def dado_facil():
    verde = "CPCTCP"
    return verde


def receber_tubo():
    dado_vermelho = dado_dificil()
    dado_amarelo = dado_intermediario()
    dado_verde = dado_facil()

    tubo = [dado_vermelho, dado_vermelho, dado_vermelho,
            dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
            dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde]

    return tubo


def fazer_jogada():
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
