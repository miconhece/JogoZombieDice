import controle_rodada
import iniciar
import finalizar
import painel


def introducao():
    painel.principal()


def jogar():
    boas_vindas()
    numero = iniciar.contar_jogadores()
    jogadores = tuple(iniciar.cadastrar_jogadores(numero))
    iniciar.preparar_jogadores()

    for i in range(len(jogadores)):
        # PEGAR TUBO #
        jogador = jogadores[i]

        turno = iniciar.iniciar_turno(jogador)

        vermelho = iniciar.dado_dificil()
        amarelo = iniciar.dado_intermediario()
        verde = iniciar.dado_facil()
        tubo = iniciar.receber_tubo()

        dados = 3
        jogada = 0

        placar = {"cerebro": 0, "passo": 0, "tiro": 0}
        start = iniciar.fazer_jogada()

        while start:
            jogada = jogada + 1
            controle_rodada.exibir_status(tubo, jogada, vermelho, amarelo, verde)
            faces = []

            placar_final = {}
            for _ in range(dados):

                sorteado = controle_rodada.lancar_dados()
                cor = controle_rodada.verificar_cor(sorteado, vermelho, amarelo, verde)
                controle_rodada.desenhar_dado(cor)

                face = controle_rodada.verificar_face(sorteado)
                faces.append(face)

                tubo = controle_rodada.remover_dado(tubo, sorteado, face)
                if face == "P":
                    tubo.append(sorteado)

                placar = finalizar.pontuar_jogada(placar, face)

            controle_rodada.parcial_tubo_cont(tubo)

            dano = finalizar.marcar_tiro(placar)
            pontuacao = finalizar.acumulado(placar)

            if dano < 3:
                finalizar.mensagem_pontuacao(dano)
                finalizar.placar_cerebro(pontuacao)
                finalizar.placar_passo(pontuacao)
                finalizar.placar_tiro(pontuacao)

                continuar = finalizar.jogar_novamente()
                restam = len(tubo)

                if continuar == "S":
                    finalizar.contar_dados(restam)
                else:
                    start = False
                    placar["tiro"] = 0
                    placar["passo"] = 0
            else:
                print("Morrer... de novo! Você perdeu todos os pontos. ")
                print("Aguarde o próximo turno para jogar. ")
                start = False
                placar = {"cerebro": 0, "tiro": 0, "passo": 0}

            placar_final = placar
            print(placar_final)
            finalizar.final_turno(start)


def boas_vindas():
    print("----- Bem vindo ao ZOMBIE DICE -----".center(80))
    print("=" * 80)


if __name__ == "__main__":
    introducao()
