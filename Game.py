import numpy as np

class TicTacToeGame:
    def __init__(self):
        # Simbolos para el jugador y la maquina
        self.MACHINE = "❌"
        self.HUMAN = "⭕"
        self.EMPTY_CELL = "⬜"
        self.INF = float('inf')
        self.BOARD_SIZE = 4
        # Crear un tablero vacio
        self.board = np.full((self.BOARD_SIZE, self.BOARD_SIZE), self.EMPTY_CELL)

    def find_empty_cells(self) -> list:
        """
        Encuentra y devuelve las celdas vacias en el tablero
        """
        empty_cells = []

        for row_index, row in enumerate(self.board):
            for col_index, cell in enumerate(row):
                if cell != self.MACHINE and cell != self.HUMAN:
                    empty_cells.append((row_index, col_index))
        return empty_cells

    def is_winner(self, player) -> bool:
        """
        Verifica si el jugador actual es el ganador siguiendo el patron en forma de "L"
        """
        for row_index, row in enumerate(self.board):
            if row_index != self.BOARD_SIZE - 1:
                for col_index, cell in enumerate(row):
                    if col_index != self.BOARD_SIZE - 1 and cell == player:
                        if (
                            self.board[row_index + 1][col_index] == player
                            and self.board[row_index + 1][col_index + 1] == player
                        ):
                            return True
        return False

    def evaluate(self) -> float:
        """
        Evalua el estado actual del tablero y devuelve un puntaje
        """
        score = 0
        if self.is_winner(self.MACHINE) and not self.is_winner(self.HUMAN):
            score += self.INF
        elif not self.is_winner(self.MACHINE) and self.is_winner(self.HUMAN):
            score -= self.INF

        return score

    def best_move(self):
        """
        Encuentra la mejor jugada posible para la maquina utilizando el algoritmo minimax con "pruning alpha-beta"
        """
        max_eval = -self.INF
        alpha = -self.INF
        beta = self.INF

        empty_cells = self.find_empty_cells()

        best_move = None

        for cell in empty_cells:
            self.board[cell[0]][cell[1]] = self.MACHINE
            # Llama al algoritmo minimax para evaluar la jugada
            evaluation = self.minimax(self.HUMAN, alpha, beta, 5)
            self.board[cell[0]][cell[1]] = self.EMPTY_CELL
            # Actualiza la mejor jugada si la evaluacion es mayor
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = cell

        return best_move

    def minimax(self, player, alpha, beta, depth) -> float:
        """
        Algoritmo minimax con "alpha-beta pruning" para saber cuale s la mejor jugada
        """
        if depth == 0 or self.is_winner(self.HUMAN) or self.is_winner(self.MACHINE):
            return self.evaluate()

        empty_cells = self.find_empty_cells()

        if player == self.MACHINE:
            max_eval = -self.INF
            for cell in empty_cells:
                self.board[cell[0]][cell[1]] = self.MACHINE
                # Llama recursivamente al algoritmo minimax con el siguiente jugador
                evaluation = self.minimax(self.HUMAN, alpha, beta, depth - 1)
                self.board[cell[0]][cell[1]] = self.EMPTY_CELL
                # Actualiza el puntaje máximo y los valores de alpha
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if alpha >= beta:
                    break

            return max_eval

        else:
            min_eval = self.INF
            for cell in empty_cells:
                self.board[cell[0]][cell[1]] = self.HUMAN
                # Llama recursivamente al algoritmo minimax con el siguiente jugador
                evaluation = self.minimax(self.MACHINE, alpha, beta, depth - 1)
                self.board[cell[0]][cell[1]] = self.EMPTY_CELL
                # Actualiza el puntaje mínimo y los valores de beta
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
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