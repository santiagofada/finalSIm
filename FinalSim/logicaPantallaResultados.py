from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

class PantallaResultados(QMainWindow):
    "Inicializar Clase"

    def __init__(self):

        super().__init__()

        """Cargar GUI"""
        uic.loadUi("pantallaResultados.ui", self)

    def mostrarResultados(self, tablaSimulacion, cantAtendiddos, cantDespachados, acordado1,
                 noAcordado1, costo1, prom1, acordado2, noAcordado2, costo2, prom2,
                 acordado3, noAcordado3 ,costo3, prom3, acordado4, noAcordado4,
                          costo4, prom4):

        self.cargarTabla(tablaSimulacion)

        self.cargarDatos(cantAtendiddos, cantDespachados, acordado1,
                 noAcordado1, costo1, prom1, acordado2, noAcordado2, costo2, prom2,
                 acordado3, noAcordado3 ,costo3, prom3, acordado4, noAcordado4,
                         costo4, prom4)

    def cargarTabla(self, datos):

        fila = 0

        self.tablaResultados.setRowCount(len(datos))

        for i in range(len(datos)):
            self.tablaResultados.setItem(fila, 0, QTableWidgetItem(str(datos.at[i, "Semana"])))
            self.tablaResultados.setItem(fila, 1, QTableWidgetItem(str(datos.at[i, "Longitud cola"])))
            self.tablaResultados.setItem(fila, 2, QTableWidgetItem(str(datos.at[i, "Cola"])))
            self.tablaResultados.setItem(fila, 3, QTableWidgetItem(str(datos.at[i, "Arribos"])))
            self.tablaResultados.setItem(fila, 4, QTableWidgetItem(str(datos.at[i, "Autos"])))
            self.tablaResultados.setItem(fila, 5, QTableWidgetItem(str(datos.at[i, "Atenciones"])))
            self.tablaResultados.setItem(fila, 6, QTableWidgetItem(str(datos.at[i, "Atendidos"])))
            self.tablaResultados.setItem(fila, 7, QTableWidgetItem(str(datos.at[i, "Despachos"])))
            self.tablaResultados.setItem(fila, 8, QTableWidgetItem(str(datos.at[i, "Despachados"])))
            self.tablaResultados.setItem(fila, 9, QTableWidgetItem(str(datos.at[i, "Costo opc 1"])))
            self.tablaResultados.setItem(fila, 10, QTableWidgetItem(str(datos.at[i, "Costo opc 2"])))
            self.tablaResultados.setItem(fila, 11, QTableWidgetItem(str(datos.at[i, "Costo opc 3"])))
            self.tablaResultados.setItem(fila, 12, QTableWidgetItem(str(datos.at[i, "Costo opc 4"])))

            fila = fila + 1


    def cargarDatos(self, cantAtendiddos, cantDespachados, acordado1,
                 noAcordado1, costo1, prom1, acordado2, noAcordado2, costo2, prom2,
                 acordado3, noAcordado3 ,costo3, prom3, acordado4, noAcordado4,
                    costo4, prom4):

        self.txtAtendidos.setText(str(cantAtendiddos))
        self.txtDespachados.setText(str(cantDespachados))

        self.txtAcordado1.setText(str(acordado1))
        self.txtnoAcordado1.setText(str(noAcordado1))
        self.txtCosto1.setText(str(costo1))
        self.txtProm1.setText(str(prom1))

        self.txtAcordado2.setText(str(acordado2))
        self.txtnoAcordado2.setText(str(noAcordado2))
        self.txtCosto2.setText(str(costo2))
        self.txtProm2.setText(str(prom2))

        self.txtAcordado3.setText(str(acordado3))
        self.txtnoAcordado3.setText(str(noAcordado3))
        self.txtCosto3.setText(str(costo3))
        self.txtProm3.setText(str(prom3))

        self.txtAcordado4.setText(str(acordado4))
        self.txtnoAcordado4.setText(str(noAcordado4))
        self.txtCosto4.setText(str(costo4))
        self.txtProm4.setText(str(prom4))



        
