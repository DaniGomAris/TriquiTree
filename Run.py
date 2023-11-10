from Menu import TicTacToeMenu

if __name__ == "__main__":
    option = int(input("""
----TIC-TAC-TOE----     
1. Run
2. Exite
option: """))
    print("-------------------")
    print()
    if option == 1: 
        triqui_menu = TicTacToeMenu()
        triqui_menu.play()

    if option == 2:
        pass