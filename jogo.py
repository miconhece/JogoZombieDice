import controle_rodada
import iniciar


def jogar():
    numero = iniciar.contar_jogadores()
    jogadores = tuple(iniciar.cadastrar_jogadores(numero))
    iniciar.listar_jogadores(jogadores)
    for i in range(len(jogadores)):
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
            cores = []
            for _ in range(dados):
                sorteado = controle_rodada.lancar_dados()
                cor = controle_rodada.verificar_cor(sorteado, vermelho, amarelo, verde)
                cores.append(cor)
                controle_rodada.desenhar_dado(cor)
                face = controle_rodada.verificar_face(sorteado)
                tubo = controle_rodada.remover_dado(tubo, sorteado, face)
                print(len(tubo))
                placar_atual = pontuar_jogada(placar, face)
                print(placar_atual)
                dano = marcar_tiro(placar_atual)
                if dano < 3:
                    placar = placar_atual

                else:
                    print("Mensagem fim de turno e reinicializacao")

            break


def pontuar_jogada(placar, face):
    face_sorteada = face
    placar_atual = placar
    if face_sorteada == "C":
        placar_atual["cerebro"] += 1
    elif face_sorteada == "T":
        placar_atual["tiro"] += 1
    elif face_sorteada == "P":
        placar_atual["passo"] += 1
    return placar_atual


def marcar_tiro(placar_atual):
    dano_sofrido = placar_atual.get("tiro")
    return dano_sofrido


def mensagem_pontuacao(start, placar_atual):
    placar = placar_atual
    cerebro = placar.get("cerebro")
    tiro = placar.get("tiro")
    passo = placar.get("passo")
    print(cerebro)
    print(tiro)
    print(passo)
    start = False



if __name__ == "__main__":
    jogar()
