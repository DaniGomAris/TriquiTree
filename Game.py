import numpy as np

class TicTacToeGame:
    def __init__(self):
        # Simbolos para el jugador y la maquina
        self.MACHINE = "❌"
        self.HUMAN = "⭕"
        self.EMPTY_CELL = "⬜"
        self.INF = float('inf') #(-∞) o (+∞)
        self.BOARD_SIZE = 4
        self.board = [[self.EMPTY_CELL] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]

    def find_empty_cells(self) -> list:
        """
        Encuentra y devuelve las celdas vacias en el tablero
        """
        empty_cells = []

        # Se va moviendo entre las filas del tablero
        for current_row, row in enumerate(self.board):
            # Se va moviendo entre las columnas de ;as filas
            for current_col, col in enumerate(row):
                if col != self.MACHINE and col != self.HUMAN:
                    empty_cells.append((current_row, current_col))
        return empty_cells

    def is_winner(self, player) -> bool:
        """
        Verifica si el jugador actual es el ganador siguiendo el patron en forma de "L"
        """
        # Se va moviendo entre las filas del tablero
        for current_row, row in enumerate(self.board):
            if current_row != self.BOARD_SIZE - 1:
                # Se va moviendo entre las columnas de ;as filas
                for current_col, col in enumerate(row):
                    if current_col != self.BOARD_SIZE - 1 and col == player:
                        # Analiza primero la posicion actual (1,1) luego analiza (1,1)(2,1) y luego (1,1)(2,1)(2,2), que pertenezcan al mismo jugador
                        if (
                            self.board[current_row + 1][current_col] == player
                            and self.board[current_row + 1][current_col + 1] == player
                        ):
                            return True
        return False

    def evaluate(self) -> float:
        """
        Evalua el estado actual del tablero y devuelve un puntaje
        """
        score = 0

        # Si la maquina gano y el jugador perdio
        if self.is_winner(self.MACHINE) and not self.is_winner(self.HUMAN):
            score += self.INF # +∞

        # Si el jugador gano y la maquina perdio
        if self.is_winner(self.HUMAN) and not self.is_winner(self.MACHINE):
            score -= self.INF # -∞

        return score

    def best_move(self):
        """
        Encuentra la mejor jugada posible para la maquina utilizando el metodo minimax
        """
        max_eval = -self.INF
        alpha = -self.INF
        beta = self.INF

        empty_cells = self.find_empty_cells()

        best_play = None

        # Recorre las celdas vacias para evaluar las posibles jugadas
        for cell in empty_cells:
            
            self.board[cell[0]][cell[1]] = self.MACHINE

            # Llama a  minimax para evaluar la mejor posible jugada
            evaluation = self.minimax(self.HUMAN, alpha, beta, 5) 

            self.board[cell[0]][cell[1]] = self.EMPTY_CELL

            if evaluation > max_eval:
                max_eval = evaluation
                best_play = cell

        # Retorna la mejor jugada encontrada
        return best_play

    def minimax(self, player, alpha, beta, depth) -> float:
        """
        Algoritmo minimax con "alpha-beta pruning" para saber cual es la mejor jugada
        """
        # Nodos hoja del árbol
        if depth == 0 or self.is_winner(self.HUMAN) or self.is_winner(self.MACHINE):
            return self.evaluate()

        empty_cells = self.find_empty_cells()

        # Jugador MAX (máquina)
        if player == self.MACHINE:  
            max_eval = -self.INF

            for cell in empty_cells:
                self.board[cell[0]][cell[1]] = self.MACHINE

                evaluation = self.minimax(self.HUMAN, alpha, beta, depth - 1)
                
                self.board[cell[0]][cell[1]] = self.EMPTY_CELL

                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)

                if alpha >= beta:
                    break

            return max_eval
        
        # Jugador MIN (humano)
        else:  
            min_eval = self.INF

            for cell in empty_cells:
                self.board[cell[0]][cell[1]] = self.HUMAN
                evaluation = self.minimax(self.MACHINE, alpha, beta, depth - 1)
                self.board[cell[0]][cell[1]] = self.EMPTY_CELL

                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)

                if alpha >= beta:
                    break

            return min_eval


    def play_machine(self):
        """
        Realiza el movimiento de la maquina en el tablero
        """
        best_move = self.best_move()
        if best_move is not None:
            self.board[best_move[0]][best_move[1]] = self.MACHINE

    def print_board(self):
        """
        Imprime el estado actual del tablero
        """
        for row in self.board:
            print("  ".join(row))