from multiprocessing import set_forkserver_preload


class Piso:
    def __init__(self,r,c,f,s) -> None:
        self.fila=r
        self.columna=c
        self.volteo=f
        self.intercambio=s
        self.siguiente=None