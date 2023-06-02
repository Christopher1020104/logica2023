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
def realizar_moviemiento(self, fila, columna):
    if self.tablero[fila][columna] == "":
        self.tablero[fila][columna] =
self.jugador_actual
        self.moviemientos += 1

if self.verificar_ganador(self.jugador_actual):
     self.mostras_tablero()
     print("¡jugador",self.jugador_actual,"ha ganado!")
     return True

if self.movimientos ==9:
     self.mostras_tablero()
     print("¡empate!")
     return True

self.jugador_actual = "O" IF self.jugador_actual === "X" else "X"
       else:
print(" ese espacio esta ocupado, seleciona otro")
return False
 if self.movimientos == 9:
                self.mostrar_tablero()
                print("¡Empate!")
                return True

            self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")
        
        return False

    def verificar_ganador(self, triqui):
        # Verificar filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == triqui:
                return True

        # Verificar columnas
        for i in range(3):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] == triqui:
                return True

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == triqui:
            return True

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == triqui:
            return True

        return False


# Función para jugar
def jugar_triqui():
    juego = Triqui()

    while True:
        juego.mostrar_tablero()

        fila = int(input("Ingresa el número de fila (0-2): "))
        columna = int(input("Ingresa el número de columna (0-2): "))

        if juego.realizar_movimiento(fila, columna):
            break

jugar_triqui()