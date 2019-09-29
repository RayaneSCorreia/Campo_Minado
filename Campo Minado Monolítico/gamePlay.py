from cm_negocio import CampoMinado
import sys




def menu():
    print("------------------------------------------------------------")
    print("|                      CAMPO MINADO                        |")
    print("------------------------------------------------------------")
    ##print("                    1 - INICIAR                   ") - Adicionar evolução de fases
    print("                   1 - ESCOLHER NÍVEL                       ")
    print("                       2 - SAIR                               ")
    print("------------------------------------------------------------\n")

    choice = int(input(" Escolha a opção desejada: "))


    if choice == 1:
        print("\n                      Níveis            \n")
        print("       ( 1 )        Fácil               Campo com 4 x 4 ")
        print("       ( 2 )        Ousadx              Campo com 5 x 5")
        print("       ( 3 ) Coragem, porque noção...   Campo com 8 x 8 \n")

        choiceTwo = int(input(" Escolha a opção desejada: "))

        if choiceTwo == 1:
            camp = CampoMinado(4,4)
            iniciar(camp)
        elif choiceTwo == 2:
            camp = CampoMinado(5,5)
            iniciar(camp)
        elif choiceTwo == 3:
            camp = CampoMinado(8,8)
            iniciar(camp)
            
        else:
            pass
    else:
       exit

def iniciar(camp):
    print(" A contagem linhas/colunas começa por 0 e não 1!")
    camp.criarCampo()
    play(camp)

def reiniciar():
    print("Deseja reiniciar? ")
    print(" 1 - Sim")
    print(" 2 - Não")
    choice = int(input(":Responda: "))
    if choice == 1:
        menu()
    else:
        exit


def play(camp):
    if camp.verifica_jogada() > 0:
        linha = int(input("Escolha a linha : "))
        coluna = int(input("Escolha da coluna : "))
        result = camp.jogada(linha, coluna)
        qtde_jogadas = camp.verifica_jogada()
        if result == "loser":
            print("------------------BOOOOOM----------------------")
            print("-----------------------------------------------")
            print("-----------------(========)--------------------")
            print("--------------------||||-----------------------")
            print("------------------######## --------------------")
            print("----------------############-------------------")
            print("---------------##############------------------")
            print("---------------##############------------------")
            print("----------------############-------------------")
            print("------------------########---------------------")
            print("-----------------------------------------------")
            print("-----------------VOCÊ PERDEU-------------------")
            

            reiniciar()
            
        elif result == "Error 01":
            print("Se atente aos limites de linha/coluna! \n")
            print(f"Você ainda tem {qtde_jogadas} jogadas!")
            play(camp)
        elif result == "Error 02":
            print("Posições ká escolhidas anteriormente! Selecione novas posições: \n")
            print(f"Você ainda tem {qtde_jogadas} jogadas!\n")
            print(":Responda: ")
            play(camp)

        else:
            print(f'Você ainda tem {result} jogadas, continue! ')
            play(camp)
    else:
        print("---------------CAMPO DESARMADO-----------------")
        print("--###-----------------------------------###----")
        print("--########-------------------------########----")
        print("--#########################################----")
        print("---#####---------(========)---------#####------")
        print("-----#####----------||||----------#####--------")
        print("--------#####-----######## --- #####-----------")
        print("----------#####-############-#####-------------")
        print("---------------##############------------------")
        print("---------------##############------------------")
        print("----------------############-------------------")
        print("------------------########---------------------")
        print("------------------########---------------------")
        print("------------------########---------------------")
        print("------------------########---------------------")
        print("------------------########---------------------")
        print("------------------########---------------------")
        print("###############################################")
        print("----------------VOCÊ VENCEU!!!-----------------")
        reiniciar()


menu()