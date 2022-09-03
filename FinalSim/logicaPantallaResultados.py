from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

class PantallaResultados(QMainWindow):
    "Inicializar Clase"

    def __init__(self):

        super().__init__()

        """Cargar GUI"""
        uic.loadUi("pantallaResultados.ui", self)

        
