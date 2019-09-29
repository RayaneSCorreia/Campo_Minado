from random import randint


class CampoMinado:

    def __init__(self, linha, coluna):
        self.__linha = linha
        self.__coluna = coluna
        self.__campo = self.__desenhoMatriz(linha, coluna)
        self.__total_bombas = self.__bombas(linha, coluna) #total de bombas a depender do nível
        self.__total_jogadas = (self.__linha * self.__coluna) - self.__total_bombas
        self.__posicoesBombas = self.__gerarBombas(linha, coluna) #vator com as tuplas de bombas armazenadas

    def __bombas(self, linha, coluna): #gera bombas a depender do nível escolhido
        if self.__linha == 4 and self.__coluna == 4:
            qte_bombas = 6
        elif self.__linha == 5 and self.__coluna == 5:
            qte_bombas = 9
        else:
            qte_bombas = 15
        return qte_bombas
    

    def __gerarBombas(self, linha, coluna):
        posicoesBombas = []
        bombas = self.__total_bombas
        while bombas > 0:
            posicao = (randint(0, linha - 1), randint(0, coluna - 1))
            if posicao not in posicoesBombas:
                posicoesBombas.append(posicao)
                bombas = bombas - 1
        return posicoesBombas

    def __desenhoMatriz(self, linha, coluna):
        return [["|_|" for c in range(coluna)] for l in range(linha)]

    def criarCampo(self): #retorna print de todas as posições da matriz criada no desenhoMatriz()
        for saidas in self.__campo:
            print(str(saidas))

    def marcar_escolha(self,linha, coluna):
        posicao = (linha, coluna)
        if posicao in self.__posicoesBombas:
            self.__campo[linha][coluna] = " X "
            self.criarCampo()
        elif self.__campo[linha][coluna] == " # ":
            print("Jogada já feita, repita o processo")
            return False
        else:
            self.__campo[linha][coluna] = " # "
            self.criarCampo()
        

    def validarPosicao (self, linha, coluna):
        if linha in range(0, self.__linha ) and coluna in range(0, self.__coluna):
            return True
        if linha not in range(0, self.__linha ) and coluna in range(0, self.__coluna ):
           print("Linha inválida ")
        if coluna not in range(0, self.__coluna ) and linha in range(0, self.__linha ):
           print("Coluna inválida")
        if coluna not in range(0, self.__coluna ) and linha not in range(0, self.__linha ):
            print("Linha e coluna inválidas")

        return False

    def verifica_jogada(self):
        return self.__total_jogadas

    def jogada(self, linha, coluna):
        if self.validarPosicao(linha,coluna):
           # print(f"Validou {linha}, {coluna}")
            posicao = (linha, coluna)
            if posicao in self.__posicoesBombas:
                self.marcar_escolha(linha, coluna)
                return "loser"
            elif self.__total_jogadas == 0:
                self.marcar_escolha(linha, coluna)
                return "win"
            else:
                if self.marcar_escolha(linha, coluna) == False:
                    return "Error 02"
                else:
                    self.__total_jogadas =  self.__total_jogadas - 1
                    return self.__total_jogadas
        else:
            return "Error 01"

    


    


    

   

