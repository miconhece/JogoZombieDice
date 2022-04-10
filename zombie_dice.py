import controle_rodada
import iniciar
import finalizar
import painel


def introducao():
    painel.principal()


def jogar():
    ranking = {}
    boas_vindas()
    numero = iniciar.contar_jogadores()
    print(numero)
    jogadores = tuple(iniciar.cadastrar_jogadores(numero))
    print(jogadores)
    iniciar.preparar_jogadores()

    for i in range(len(jogadores)):
        # PEGAR TUBO #
        jogador = jogadores[i]
        ranking[jogador] = 0
        print(jogador)

        iniciar.iniciar_turno(jogador)

        vermelho = iniciar.dado_dificil()
        print(vermelho)
        amarelo = iniciar.dado_intermediario()
        print(amarelo)
        verde = iniciar.dado_facil()
        print(verde)
        tubo = iniciar.receber_tubo()
        print(tubo)

        dados = 3
        jogada = 0

        placar = {"cerebro": 0, "passo": 0, "tiro": 0}
        start = iniciar.fazer_jogada()
        print(start)

        while start:
            jogada = jogada + 1
            controle_rodada.exibir_status(tubo, jogada, vermelho, amarelo, verde)
            faces = []

            for _ in range(dados):

                sorteado = controle_rodada.lancar_dados()
                print(sorteado)
                cor = controle_rodada.verificar_cor(sorteado, vermelho, amarelo, verde)
                print(cor)
                controle_rodada.desenhar_dado(cor)

                face = controle_rodada.verificar_face(sorteado)
                print(face)
                faces.append(face)

                tubo = controle_rodada.remover_dado(tubo, sorteado)
                print(tubo)
                if face == "P":
                    tubo.append(sorteado)

                placar = finalizar.pontuar_jogada(placar, face)
                print(placar)

            controle_rodada.parcial_tubo_cont(tubo)

            dano = finalizar.marcar_tiro(placar)
            print(dano)
            pontuacao = finalizar.acumulado(placar)
            print(pontuacao)

            if dano < 3:
                finalizar.mensagem_pontuacao()
                finalizar.placar_cerebro(pontuacao)
                pontos = finalizar.marcar_pontos(placar)
                finalizar.placar_passo(pontuacao)
                finalizar.placar_tiro(pontuacao)

                continuar = finalizar.jogar_novamente()
                print(continuar)
                restam = len(tubo)

                if continuar == "S":
                    finalizar.contar_dados(restam)
                else:
                    start = False
            else:
                print("Morrer... de novo! Você perdeu todos os pontos. ")
                print("Aguarde o próximo turno para jogar. ")
                start = False
                placar = {"cerebro": 0, "tiro": 0, "passo": 0}
                pontos = 0

            ranking[jogador] = pontos
            placar_final = placar
            print(placar_final)
            finalizar.final_turno(start)
    print(ranking)


def boas_vindas():
    print("----- Bem vindo ao ZOMBIE DICE -----".center(80))
    print("=" * 80)


if __name__ == "__main__":
    introducao()
