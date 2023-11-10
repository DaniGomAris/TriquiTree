import random

from Game import TicTacToeGame

class TicTacToeMenu:
    def __init__(self):
        self.game = TicTacToeGame()

    def print_board_and_status(self):
        """
        Imprime el tablero y el estado del juego
        """
        self.game.print_board()
        # Verifica si el juego termino en empate
        if len(self.game.find_empty_cells()) == 0:
            print("EMPATE")
        # Verifica si el jugador humano gano
        elif self.game.is_winner(self.game.HUMAN):
            print()
            print("¡GANASTE!")
        # Verifica si la maquina gano
        elif self.game.is_winner(self.game.MACHINE):
            print()
            print("¡PERDISTE!")

    def player_turn(self):
        """
        Turno del jugador humano
        """
        while True:
            try:
                row = int(input("Enter row (0-3): "))
                col = int(input("Enter col (0-3): "))
                print()

                # Verifica si lo que puso el jugador humano, es valido
                if 0 <= row < 4 and 0 <= col < 4 and self.game.board[row][col] == self.game.EMPTY_CELL:
                    # Realiza el movimiento del jugador humano
                    self.game.board[row][col] = self.game.HUMAN
                    break
                else:
                    print("Entrada invalida, intenta de nuevo")
            except ValueError:
                print("Entrada invalida, ingresa un numero")

    def machine_turn(self):
        """
        Turno de la maquina para realizar un movimiento aleatorio al principio del juego
        """
        if len(self.game.find_empty_cells()) == 15:
            while True:
                # Genera una posicion aleatoria para la maquina
                machine_row = random.randint(0, 3)
                machine_col = random.randint(0, 3)
                # Verifica si la celda esta vacia
                if self.game.board[machine_row][machine_col] == self.game.EMPTY_CELL:
                    # Realiza el movimiento de la maquina
                    self.game.board[machine_row][machine_col] = self.game.MACHINE
                    break
        else:
            # Turno de la maquina
            self.game.play_machine()

    def play(self):
        """
        Inicia el juego
        """
        print("---TIC-TAC-TOE---\n")
        current_player = self.game.HUMAN
        while True:
            # Imprime el tablero y el estado actual
            self.print_board_and_status()

            print()
            print(f"--- {current_player} Turn---")
            print()
            
            # Realiza el turno del jugador humano o de la maquina
            if current_player == self.game.HUMAN:
                self.player_turn()
            else:
                self.machine_turn()

            # Verifica si el juego termino y muestra el estado final
            if self.game.is_winner(current_player) or len(self.game.find_empty_cells()) == 0:
                self.print_board_and_status()
                break

            # Cambia al siguiente jugador
            current_player = self.game.MACHINE if current_player == self.game.HUMAN else self.game.HUMAN