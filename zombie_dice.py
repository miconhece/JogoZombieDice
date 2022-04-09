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
    iniciar.listar_jogadores(jogadores)

    for i in range(len(jogadores)):
        nome = jogadores[i]
        # PEGAR TUBO #
        vermelho = iniciar.dado_dificil()
        amarelo = iniciar.dado_intermediario()
        verde = iniciar.dado_facil()
        tubo = iniciar.receber_tubo()

        dados = 3
        jogada = 0

        placar = {"cerebro": 0, "passo": 0, "tiro": 0}
        start = iniciar.fazer_jogada()

        while start:
            controle_rodada.exibir_status(jogada, vermelho, amarelo, verde)
            faces = []

            placar_final = {}
            for _ in range(dados):
                sorteado = controle_rodada.lancar_dados()
                cor = controle_rodada.verificar_cor(sorteado, vermelho, amarelo, verde)
                controle_rodada.desenhar_dado(cor)
                face = controle_rodada.verificar_face(sorteado)
                print(face)
                faces.append(face)
                tubo = controle_rodada.remover_dado(tubo, sorteado, face)
                if face == "P":
                    tubo.append(sorteado)
                placar = finalizar.pontuar_jogada(placar, face)
                print(placar)
                pontos = placar.get("cerebro")
                print(f"placar = {pontos}")
                placar_final[nome] = pontos
                print(f"Pontuação Final = {placar_final}")

            print(f"Restam {len(tubo)} dados!")
            print(tubo)
            print(placar)
            dano = finalizar.marcar_tiro(placar)
            print(f"DANO = {dano}")

            if dano < 3:
                finalizar.mensagem_pontuacao()
                finalizar.placar_cerebro(placar)
                finalizar.placar_passo(placar)
                finalizar.placar_tiro(placar)

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


def boas_vindas():
    print("----- Bem vindo ao ZOMBIE DICE -----".center(80))
    print("=" * 80)


if __name__ == "__main__":
    introducao()
