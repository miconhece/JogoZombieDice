import painel

separador = "=" * 80
linha = "-" * 80


def apresentacao():
    """
    Apresenta dados gerais da disciplina e aluna responsável pelo código.

    :return: Não possui retorno
    """

    descricao = {
        "titulo": "Zombie Dice",
        "disciplina": "Disciplina: Raciocínio Computacional",
        "aluna": "Aluna: Michele Cristina da Silva Santos",
        "curso": "Curso: Tecnologia em Análise e Desenvolvimento de Sistemas"
    }
    print(descricao["disciplina"].ljust(80))
    print(descricao["curso"].ljust(80))
    print(descricao["aluna"].ljust(80) + '\n')
    print(separador)
    print(" ______               _     _        _____  _           ".center(80))
    print("|___  /              | |   (_)      |  __ \(_)          ".center(80))
    print("   / / ___  _ __ ___ | |__  _  ___  | |  | |_| ___ ___  ".center(80))
    print("  / / / _ \| '_ ` _ \| '_ \| |/ _ \ | |  | | |/ __/ _ \ ".center(80))
    print(" / /_| (_) | | | | | | |_) | |  __/ | |__| | | (_|  __/ ".center(80))
    print("/_____\___/|_| |_| |_|_.__/|_|\___| |_____/|_|\___\___| ".center(80), '\n')
    print(separador + '\n')


def regulamento():
    """
    Exibe regulamento do jogo, como Regras, objetivo, pontuação e finalização do tuno.

    :return: Não possui retorno.
    """
    print(separador)
    print("Regulamento do Jogo".center(80).upper()+'\n')
    print("Objetivo Principal:".ljust(25)+"Este jogo conta com 13 dados e um tubo para guardá-los."+'\n' +
          " ".ljust(25) + "Você precisa marcar seus pontos de alguma maneira."+'\n'
          " ".ljust(26) + "Dois ou mais jogadores podem jogar.".ljust(55))
    print(linha.ljust(110))
    print("No seu turno:".ljust(25) + "Pegue 3 dados do tubo (aleatoriamente)." + '\n' +
          " ".ljust(25) + "Cada dado representa uma pobre vítima a ser atacada." + '\n' +
          " ".ljust(25) + "Os dados vermelhos são os mais difíceis, dados verdes são " + '\n' +
          " ".ljust(25) + "os mais fáceis e os dados amarelos médios.".ljust(55)+'\n')
    print(" ".ljust(25) + "Simbolos dos dados".upper()+'\n')
    print(" ".ljust(25) + "Os dados possuem 3 símbolos:" + '\n' +
          " ".ljust(25) + "Cérebro - Significa que você devorou um cérebro e marcou 1 ponto." + '\n' +
          " ".ljust(25) + "Pegadas - Significa que sua vítima escapou e você não marca ponto." + '\n' +
          " ".ljust(25) + "Espingarda - Significa que sua vítima revidou e você perdeu um ponto.".ljust(55)+'\n')
    print(" ".ljust(25) + "Jogadas".upper() + '\n')
    print(" ".ljust(25) + "Você pode fazer quantas jogadas quiser. Considerando que:" + '\n' +
          " ".ljust(25) + "Dados com a face cérebro não voltam para o tubo antes do final do seu turno." + '\n' +
          " ".ljust(25) + "Dados com a face tiro também não voltam para o tubo antes do final do seu turno." + '\n' +
          " ".ljust(25) + "Você sempre precisará lançar 3 dados".ljust(55) + '\n')
    print(" ".ljust(25) + "Fim do Turno".upper() + '\n')
    print(" ".ljust(25) + "O seu turno se encerra, caso:" + '\n' +
          " ".ljust(25) + "Não tenha 3 dados sobrando no tubo" + '\n' +
          " ".ljust(25) + "Se você levar 3 tiros com a espingarda, você morre." + '\n' +
          " ".ljust(25) + "Você pode decidir parar de jogar e encerrar o turno quando quiser.".ljust(55) + '\n')
    print(linha.ljust(110))
    print("Vencedor:".ljust(25) + "Faça suas jogadas." + '\n' +
          " ".ljust(25) + "Ao encerrar seu turno, começa o de outro jogador. Todos precisam jogar." + '\n' +
          " ".ljust(25) + "Ganha quem chegar a 13 cérebros até o final da rodada. " + '\n' +
          " ".ljust(25) + "Se houver empate, apenas os líderes jogam para desempatar.".ljust(55) + '\n')
    if input("Retornar ao MENU PRINCIPAL? Digite S para Sim e N para SAIR DO JOGO: ").upper().strip() == "S":
        print(separador)
        painel.principal()
    else:
        print("Que a sorte esteja sempre a seu favor!")


if __name__ == "__main__":
    apresentacao()
