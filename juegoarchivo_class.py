import os
import random

from videojuego import Juego, string_laberinto

# miJuego = Juego(string_laberinto)
# miJuego.__main__()

def mapaAleatorio(path_dir):
    list_files = os.listdir(path_dir)
    random_file = random.choice(list_files)
    path_completo = path_dir + "\\" + random_file
    # import pdb;pdb.set_trace()
    f = open(path_completo, "r")
    return f.read()

class JuegoArchivo(Juego):
    def __init__(self, path_dir):    
        self.path_dir = path_dir        
        file = mapaAleatorio(self.path_dir)
        super().__init__(file) 


jueguito = JuegoArchivo(r"C:\Users\brian\OneDrive\Documentos\Proyecto_integrador_python\Proyecto_integrador_parte1\files_mapas")
jueguito.__main__()
