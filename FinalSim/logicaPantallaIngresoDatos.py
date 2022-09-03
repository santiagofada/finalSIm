from PyQt5 import uic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QRegExp

import Main02
import logicaPantallaResultados

class PantallaIngresoDatos(QMainWindow):
    "Inicializar clase"

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("pantallaIngresoDatos.ui", self)
        self.btnSimular.clicked.connect(self.simular)



    def simular(self):

        vectorAcuerdo = [self.txtTA1.text(), self.txtTA2.text(), self.txtTA3.text(),
                         self.txtTA4.text()]

        vectorCostoAcuerdo = [self.txtC1.text(), self.txtC2.text(),
                         self.txtC3.text(), self.txtC4.text()]

        vectorCantTrabajos = [self.txtNT1.text(),
                         self.txtNT2.text(), self.txtNT3.text(), self.txtNT4.text(),
                         self.txtNT5.text()]

        vectorCantSemanas = [self.txtNS1.text(), self.txtNS2.text(),
                         self.txtNS3.text(), self.txtNS4.text(), self.txtNS5.text()]

        costoFueraCantAcordada = int(self.txtC5.text())

        duracion = int(self.txtTiempoSimulacion.text())

        if self.ValidarCamposNoVacios():


            Main02.simular(duracion, vectorAcuerdo, vectorCostoAcuerdo, vectorCantTrabajos
                           vectorCantSemanas, costoFueraCantAcordada)


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


    """FALTAN VALIDACIONES"""

