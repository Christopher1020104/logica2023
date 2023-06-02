class Triqui:
    def _init_(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X"
        self.movimientos = 0
        def mostrar_tablero(self):
        print("-------------")
        for i in range(3):
            print("|", end=" ")
            for j in range(3):
                print(self.tablero[i][j], "|", end=" ")
            print("\n-------------")