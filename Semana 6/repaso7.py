#Un multimillonario desea saber qué entradas de su nuevo 
# laberinto de arbustos llevan a la salida del mismo pero 
# solo dispone de un matriz con direcciones y un vector con 
# las posiciones de las entradas; por ello, el multimillonario 
# le ha contratado para que realice un algoritmo que determine qué 
# entradas llevan a la salida.
# Esta es la matriz de la cual dispone el multimillonario:

[
["DOWN","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"], 
["DOWN","DOWN","LEFT","LEFT","LEFT","LEFT","LEFT"], 
["DOWN","WALL","RIGHT","DOWN","DOWN","LEFT","LEFT"],
["RIGHT","RIGHT","UP","DOWN","DOWN","RIGHT","DOWN"], 
["WALL","DOWN","LEFT","LEFT","RIGHT","UP","DOWN"], 
["UP","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"], 
["UP","LEFT","LEFT","LEFT","LEFT","LEFT","EXIT"],
]

x = 0
y = 0 
#Y este es el vector: [[0,0],[6,5],[2,6],[0,1]]