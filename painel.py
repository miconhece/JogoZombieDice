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
    print("Menu Principal".center(80).upper()+'\n')
    print(" 1. Ver Regulamento ".center(80))
    print(" 2. Iniciar Partida ".center(80))
    print(" 3. Sair            ".center(80), '\n')
    operacao = int(input("Informe a sua escolha >>>>>>>>  ".upper()))
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
            print(separador*80)
            zombie_dice.jogar()
            break
        elif operacao == 3:
            print("Que a força esteja com você!")
            break
    return operacao


if __name__ == "__main__":
    principal()
