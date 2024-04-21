import math


def minMax(self,estado,jugadorIA):
    puntuacionJugador=self.jugador
    iaJugador='O' if jugadorIA == 'X' else 'X'

    if(self.terminal):
        return{'position':None, 'score': 1*(len(self.actions(estado))+1)
        if iaJugador == puntuacionJugador else -1*(len(self.actions(estado))+1)}
    elif self.tableroLleno(estado):
        return {'position':None, 'score':0}

    if jugadorIA==puntuacionJugador:
        best = {'position':None, 'score':-math.inf}
    else:
        best = {'position':None, 'score':math.inf}

    for posible_movimiento in self.accion(estado):
        nuevoEstado = self.resultado(estado,posible_movimiento)
        sim_puntuacion = self.minimax(nuevoEstado,iaJugador)

        sim_puntuacion['position'] = posible_movimiento

        if jugadorIA == puntuacionJugador:
            if sim_puntuacion['score'] > best['score']:
                best = sim_puntuacion
        else:
            if sim_puntuacion['score'] < best['score']:
                best = sim_puntuacion

    return best


def ia_movimiento(self,estado):
    cuadrado = self.minimax(estado,self.iaJugador)['position']
    return cuadrado