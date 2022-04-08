import documentacao
import zombie_dice

separador = "="


def principal():

    documentacao.apresentacao()

    iniciar_menu()


def menu_principal():
    """
    Menu Principal do Jogo, para controle de opções ou visualização do Regulamento (opcional)

    :return: retorna um operador para controlar chamada de função, conforme opção desejada.
    """
    print("Menu Principal".ljust(20).upper()+'\n')
    print(" 1. Ver Regulamento".rjust(20))
    print(" 2. Iniciar Partida".rjust(20))
    print(" 3. Sair".rjust(9))
    print("_" * 80)
    operacao = int(input("Informe a sua escolha: ".upper()))
    if operacao >= 1 or operacao <= 3:
        return operacao
    else:
        print("Escolha uma opção válida!".center(80))
    iniciar_menu()


def iniciar_menu():
    """
    Faz com que o menu seja sempre exibido e saia da operação caso receba valor inválido.

    :return: sem retorno.
    """
    operacao = menu_principal()
    while True:
        if operacao == 1:
            documentacao.regulamento()
            break
        elif operacao == 2:
            zombie_dice.jogar()
            break
        elif operacao == 3:
            print("Vá com Deus.")
            break
    return operacao


if __name__ == "__main__":
    principal()
