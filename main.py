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