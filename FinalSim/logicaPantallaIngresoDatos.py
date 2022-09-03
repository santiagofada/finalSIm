from PyQt5 import uic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QRegExp

import Main02
from logicaPantallaResultados import *

class PantallaIngresoDatos(QMainWindow):
    "Inicializar clase"

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("pantallaIngresoDatos.ui", self)
        self.btnSimular.clicked.connect(self.simular)



    def simular(self):

        vectorAcuerdo = [int(self.txtTA1.text()), int(self.txtTA2.text()), int(self.txtTA3.text()),
                         int(self.txtTA4.text())]

        vectorCostoAcuerdo = [int(self.txtC1.text()), int(self.txtC2.text()),
                         int(self.txtC3.text()), int(self.txtC4.text())]

        vectorCantTrabajos = [int(self.txtNT1.text()),
                         int(self.txtNT2.text()), int(self.txtNT3.text()), int(self.txtNT4.text()),
                         int(self.txtNT5.text())]

        vectorCantSemanas = [int(self.txtNS1.text()), int(self.txtNS2.text()),
                         int(self.txtNS3.text()), int(self.txtNS4.text()), int(self.txtNS5.text())]

        costoFueraCantAcordada = int(self.txtC5.text())

        duracion = int(self.txtTiempoSimulacion.text())

        if self.ValidarCamposNoVacios():


            Main02.simular(duracion, vectorAcuerdo, vectorCostoAcuerdo, vectorCantTrabajos
                           vectorCantSemanas, costoFueraCantAcordada)




    def mostrarResultados(self, tablaSimulacion, cantAtendiddos, cantDespachados, acordado1,
                 noAcordado1, costo1, prom1, acordado2, noAcordado2, costo2, prom2,
                 acordado3, noAcordado3 ,costo3, prom3, acordado4, noAcordado4,
                          costo4, prom4):
        self.pantallaResultados = PantallaResultados()
        self.pantallaResultados.mostrarResultados(tablaSimulacion, cantAtendiddos, cantDespachados, acordado1,
                 noAcordado1, costo1, prom1, acordado2, noAcordado2, costo2, prom2,
                 acordado3, noAcordado3 ,costo3, prom3, acordado4, noAcordado4,
                          costo4, prom4)

        self.pantallaResultados.show()


    def ValidarCamposNoVacios(self):
        vectorStrings = [self.txtTiempoSimulacion.text(), self.txtPrimeraFila.text(),
                         self.txtUnifA.text(), self.txtUnifB.text(),
                         self.txtTA1.text(), self.txtTA2.text(), self.txtTA3.text(),
                         self.txtTA4.text(), self.txtC1.text(), self.txtC2.text(),
                         self.txtC3.text(), self.txtC4.text(), self.txtNT1.text(),
                         self.txtNT2.text(), self.txtNT3.text(), self.txtNT4.text(),
                         self.txtNT5.text(), self.txtNS1.text(), self.txtNS2.text(),
                         self.txtNS3.text(), self.txtNS4.text(), self.txtNS5.text(),
                         self.txtC5.text()]

        for string in vectorStrings:
            if string == '' or string == " ":
                QMessageBox.warning(self, "Alerta", "Debe ingresar valores en los campos!")
                return False
                break
        return True


    

