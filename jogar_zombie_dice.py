import controle_rodada
import iniciar
import finalizar
import painel
import classificacao


def introducao():  # Apresenta os dados da disciplina e aluna responsável pelo jogo #
    painel.principal()  # Carrega um painel com opções como iniciar o jogo ou ler regulamento e sair do jogo #


def jogar():  # Função que carrega toda a estrutura do jogo #
    ranking = {}  # Vai receber a pontuação dos jogadores na forma de dicionário #
    boas_vindas()  # Mensagem de saudação #
    numero = iniciar.contar_jogadores()  # Inicia com a verificação do número de jogadores #
    jogadores = tuple(iniciar.cadastrar_jogadores(numero))  # Cadastra jogadores de acordo com o nº informado #

    rodada = 0  # Rodada vai informar se é a primeira rodada ou posteriores #
    partida = True  # Condição do looping do jogo #

    while partida:  # Looping da partida #

        rodada = rodada + 1  # Recebe o nº da rodada, conforme novo turno #
        iniciar.preparar_jogadores()  # Exibe um zumbi ao iniciar um novo turno #

        for i in range(len(jogadores)):  # Looping para percorrer jogador a jogador por turno #
            # PEGAR TUBO #
            jogador = jogadores[i]  # Nome do jogador do turno #
            if rodada == 1:
                ranking[jogador] = 0  # atribui 0 como valor inicial ao dicionário. Cria o dicionário)
            else:
                pontos = ranking[jogador]  # Se nova rodada, pontos = pontuacao da rodada anterior #
                ranking[jogador] = pontos  # reinicia pontuacao do dicionario com pontos da rodada anterior #

            iniciar.iniciar_turno(jogador)  # Mensagem de inicio do turno #

            vermelho = iniciar.dado_dificil()   # Construção dos dados conforme dificuldade  #
            amarelo = iniciar.dado_intermediario()
            verde = iniciar.dado_facil()
            tubo = iniciar.receber_tubo()   # Recebe tubo com todos os dados #

            dados = 3  # Informa quantidade de dados a ser lançado por vez #
            jogada = 0  # Inicia o número de tentativas do jogador #

            placar = {"cerebro": 0, "passo": 0, "tiro": 0}  # Dicionário que armazena pontos por face do dado #
            start = iniciar.fazer_jogada()  # Autorização do jogador para iniciar o seu turno. #

            while start:  # Looping do turno #
                jogada = jogada + 1  # Recebe quantidade de jogadas do jogador #
                controle_rodada.exibir_status(tubo, jogada, vermelho, amarelo, verde)  # Informa dados e status do tubo#
                faces = []  # Recebe as faces sorteadas a cada lançamento de dados #

                for _ in range(dados):  # Percorre cada um dos 3 dados a ser sorteado #

                    sorteado = controle_rodada.lancar_dados()  # Faz uma escolha aleatoria do dado no tubo #
                    cor = controle_rodada.verificar_cor(sorteado, vermelho, amarelo, verde)  # Verifica a cor sorteada #
                    controle_rodada.desenhar_dado(cor)  # Desenha um dado conforme a cor sorteada #

                    face = controle_rodada.verificar_face(sorteado)  # Verifica a face sorteada #
                    faces.append(face)  # Adiciona a face sorteada na lista de faces #

                    tubo = controle_rodada.remover_dado(tubo, sorteado)  # Remove o tubo sorteado do tubo #
                    if face == "P":
                        tubo.append(sorteado)  # Se face sorteada == P, devolve dado ao tubo "

                    placar = finalizar.pontuar_jogada(placar, face)  # Contabiliza os pontos por face #

                controle_rodada.parcial_tubo_cont(tubo)  # Reinicia o tubo com dados restantes e config original #

                dano = finalizar.marcar_tiro(placar)  # Armazena os pontos de dano == face tiro #
                pontuacao = finalizar.acumulado(placar)  # Insere a pontuação acumulada em forma de tupla #

                cerebros = faces.count("C")  # Verifica quantas faces "C" foi sorteadas na JOGADA

                if dano < 3:  # VERIFICA SE JOGADOR NÃO MORREU #
                    finalizar.mensagem_pontuacao()  # mensagem com o status do turno #
                    finalizar.placar_cerebro(pontuacao)
                    finalizar.placar_passo(pontuacao)
                    finalizar.placar_tiro(pontuacao)
                    continuar = finalizar.jogar_novamente()  # Verifica se jogador deseja jogar novamente #
                    ranking[jogador] += cerebros  # Adiciona no dicionário ranking os pontos de cada JOGADA #
                    restam = len(tubo)  # Lê o tamanho do tubo #

                    if continuar == "S":
                        finalizar.contar_dados(restam)  # Verifica se ha dados suficientes para mais jogadas #
                    else:
                        start = False  # Encerra turno #
                else:  # CASO JOGADOR TENHA MORRIDO #
                    print("Morrer... de novo! Você perdeu todos os pontos. ")
                    print("Aguarde o próximo turno para jogar. ")
                    placar = {"cerebro": 0, "tiro": 0, "passo": 0}  # ELE PERDE SEUS PONTOS #
                    ranking[jogador] = 0  # ELE PERDE TODOS OS PONTOS ACUMULADOS #
                    start = False  # ELE PERDE O TURNO #

                finalizar.final_turno(start)  # Mensagem de encerramento do tuno #
                score = classificacao.jogo(ranking)  # Recebe o ranking e verifica maior pontuacao #
                partida = classificacao.vencedor(score)  # Caso score > 13, encerra a partida #

        if not partida:  # Caso partida encerrada #
            score = classificacao.jogo(ranking)  # Recebe pontuacao máxima #
            classificacao.geral(ranking, partida, score)  # informa classificação e vencedor # 


def boas_vindas():
    print("----- Bem vindo ao ZOMBIE DICE -----".center(80))
    print("=" * 80)


if __name__ == "__main__":
    introducao()
