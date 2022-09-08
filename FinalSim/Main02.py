import random
import sys

import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QApplication

from Clases import Trabajo
from Distribuciones import trabajos, uniforme
import time
from logicaPantallaIngresoDatos import *


def promediar(v):
    pv = [0]*len(v)
    pv[0] = v[0]

    for i in range(1,len(v)):
        pv[i] = (v[i]+(i)*pv[i-1])/(i+1)
    return pv
def column(matrix, i):
    return [row[i] for row in matrix]
def test(duracion=100, acuerdo=(2,4,6,8), coste_Acordado=(500,950,1300,1600), resolver=(3,7),trab=(5, 6, 7, 8, 9), freq=(3, 8, 9, 6, 4),penalizacion =400, primeraFila=0):

    """ duracion = int(input("Ingrese laduracion en dias: "))
    start = time.time()
    duracion //= 7
    trab = [5,6,7,8,9]
    freq = [3,8,9,6,4]
    acuerdo =  [2,4,6,8]#[2]#
    coste_Acordado = [500,950,1300,1600]#[500]#
    penalizacion = 400
    normal = [3,7]
    """



    Autos_atendidos,Autos_despachados,costoFinal,despachados_en_acuerdo,despachados_sin_acuerdo,data = simular(duracion=duracion,acuerdo=acuerdo,
                                                                                                               coste_acordado = coste_Acordado,resolver = resolver
                                                                                                               ,trab = trab,freq = freq,penalizacion = penalizacion)
    costos =[ [],[],[],[]]


    for opc in range(len(acuerdo)):
        print(f"{acuerdo[opc]} autos por {coste_Acordado[opc]}")


        costos[opc] = column(costoFinal[opc],1)
        semanas = column(costoFinal[opc],0)
        y = promediar(costos[opc])
        #data.to_csv(rf'C:\Users\Usuario\AppData\Local\Programs\Python\finalSIm\FinalSim\data_2.csv',sep=',',index=False)
        data.to_csv(rf"C:\Users\Usuario\AppData\Local\Programs\Python\finalSIm\FinalSim\aaa.csv", sep=',', index=False)

        ##
        print(f"Autos atendidos: {Autos_atendidos[opc]}")
        print(f"Autos despachados: {Autos_despachados[opc]}")
        print(f"Autos despachados por lo acordado:{despachados_en_acuerdo[opc]}")
        print(f"Autos despachados fuerda de lo acordado:{despachados_sin_acuerdo[opc]}")

        print(f"costo final: {sum(costos[opc])}")
        print(f"costo  prom: {y[-1]}\n")

        plt.plot(semanas,y,label=f"{acuerdo[opc]} autos por {coste_Acordado[opc]}")
        plt.xlabel("semanas")
        plt.ylabel("promedio")
        plt.suptitle("Promedio costos por semana")
        plt.title("Simulacion UTN FRC")
        plt.legend()
        #print(data[opc])


    plt.show()
    end = time.time()
    #print(f"DURACION: {end-start}")

def simular(duracion=100, acuerdo=(2,4,6,8), coste_acordado=(500,950,1300,1600), resolver=(3,7),trab=(5, 6, 7, 8, 9), freq=(3, 8, 9, 6, 4),penalizacion =400, primeraFila=0):

    Autos_atendidos = [0]*len(acuerdo)
    Autos_despachados = [0]*len(acuerdo)

    costoFinal = [ [[1,i]] for i in coste_acordado ]
    despachados_en_acuerdo = [0]*len(acuerdo)
    despachados_sin_acuerdo = [0]*len(acuerdo)

    restantes = [i for i in acuerdo]

    colaTrabajos = [[],[],[],[]]


    dic = {"Semana":[],"Longitud cola":[],"Cola":[],"Arribos":[],"Autos":[],"Atenciones":[],
           "Atendidos":[],"Despachos":[],"Despachados":[],
           "Costo opc 1": [], "Costo opc 2": [], "Costo opc 3": [], "Costo opc 4": []}

    data = pd.DataFrame(dic)


    for semana in range(1,duracion+1):

        costoSem = [0,0,0,0]

        #Cantidad de llegadas en dicha semana
        rnd_llegadas = random.random()
        llegadas = trabajos(rnd_llegadas,trab = trab ,freq = freq)
        autos = []
        for i in range(llegadas):
            t = Trabajo(semana)
            autos.append(t)

        # Cantidad de trabajos atendidos en dicha semana
        rnd_resueltos = random.random()
        resueltos = int(uniforme(rnd_resueltos, a=resolver[0], b=resolver[1]))

        atendidos = [[], [], [], []]
        for idx in range(len(acuerdo)):

            if idx == 3:
                line = pd.DataFrame(
                    {"Semana": [], "Longitud cola": [], "Cola": [], "Arribos": [], "Autos": [], "Atenciones": [],
                     "Atendidos": [], "Despachos": [], "Despachados": [],
                     "Costo opc 1":[],"Costo opc 2":[],"Costo opc 3":[],"Costo opc 4":[] })

                line["Semana"] = line["Semana"].astype(int)
                line.at[0, "Semana"] = semana
                line.at[0, "Longitud cola"] = len(colaTrabajos[idx])
                line["Cola"] = line["Cola"].astype(object)
                line.at[0, "Cola"] = [i.get_nombre() for i in colaTrabajos[idx]]

            for i in range(len(autos)):
                colaTrabajos[idx].append(autos[i])

            if semana % 4 == 1:
                restantes[idx] = acuerdo[idx]
                costoSem[idx] = coste_acordado[idx]
                costoFinal[idx].append([semana, coste_acordado[idx]])

            for i in range(resueltos):
                if len(colaTrabajos[idx]) != 0:
                    atendidos[idx].append(colaTrabajos[idx][0])
                    colaTrabajos[idx].pop(0)
                    Autos_atendidos[idx] += 1


            despachados = [xi for xi in colaTrabajos[idx] if xi.get_semana()  < semana]
            colaTrabajos[idx] = [xi for xi in colaTrabajos[idx] if xi.get_semana()  >= semana]
            Autos_despachados[idx] += len(despachados)



            if len(despachados) <= restantes[idx]:
                restantes[idx] -= len(despachados)
                despachados_en_acuerdo[idx] += len(despachados)
            else:
                costoFinal[idx][-1][1] += (len(despachados) - restantes[idx])*penalizacion
                costoSem[idx] += (len(despachados) - restantes[idx])*penalizacion
                despachados_en_acuerdo[idx] += restantes[idx]
                despachados_sin_acuerdo[idx] += len(despachados) - restantes[idx]
                restantes[idx] = 0


            if idx ==3:
                line.at[0,"Arribos"] = llegadas
                line.at[0,"Despachos"] = len(despachados)
                line["Despachados"] = line["Despachados"].astype(object)
                line.at[0, "Despachados"] = [i.get_nombre() for i in despachados]
                line["Atendidos"] = line["Atendidos"].astype(object)
                line.at[0, "Atendidos"] = [i.get_nombre() for i in atendidos[idx]]
                line.at[0, "Atenciones"] = resueltos
                line["Autos"] = line["Autos"].astype(object)
                line.at[0, "Autos"] = [i.get_nombre() for i in autos]
                line.at[0,"Costo opc 1"] = costoSem[0]
                line.at[0, "Costo opc 2"] = costoSem[1]
                line.at[0, "Costo opc 3"] = costoSem[2]
                line.at[0, "Costo opc 4"] = costoSem[3]
                data = pd.concat([data, line], ignore_index=True)

    return Autos_atendidos,Autos_despachados,costoFinal,despachados_en_acuerdo,despachados_sin_acuerdo,data

if __name__=="__main__":

    app = QApplication(sys.argv)
    GUI = PantallaIngresoDatos()
    GUI.show()
    sys.exit(app.exec_())


