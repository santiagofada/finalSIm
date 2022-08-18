import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Clases import Trabajo
from Distribuciones import trabajos, uniforme


def promediar(v):
    pv = [0]*len(v)
    pv[0] = v[0]

    for i in range(1,len(v)):
        pv[i] = (v[i]+(i)*pv[i-1])/(i+1)
    return pv
def column(matrix, i):
    return [row[i] for row in matrix]
def test():

    duracion = 1000
    acuerdo =  [2]#[2,4,6,8]#
    coste_Acordado = [500]#[500,950,1300,1600]#

    for opc in range(len(acuerdo)):
        print(f"{acuerdo[opc]} autos por {coste_Acordado[opc]}")

        Autos_atendidos,Autos_despachados,costoFinal,despachados_en_acuerdo,despachados_sin_acuerdo,data = simular(duracion,acuerdo[opc],coste_Acordado[opc])
        costos = column(costoFinal,1)
        semanas = column(costoFinal,0)
        y = promediar(costos)

        print(f"Autos atendidos: {Autos_atendidos}")
        print(f"Autos despachados: {Autos_despachados}")
        print(f"Autos despachados por lo acordado:{despachados_en_acuerdo}")
        print(f"Autos despachados fuerda de lo acordado:{despachados_sin_acuerdo}")

        print(f"costo final: {sum(costos)}\n")
        print(f"costo  prom: {y[-1]}")


        plt.plot(semanas[1:],y[1:],label=f"{acuerdo[opc]} autos por {coste_Acordado[opc]}")
        plt.xlabel("meses")
        plt.ylabel("promedio")
        plt.suptitle("Promedio costos por semana")
        plt.title("Simulacion UTN FRC")
        plt.legend()
        print(data)
    plt.show()



def simular(duracion=100,acuerdo=2,coste_acordado=500):
    Autos_atendidos = 0
    Autos_despachados = 0

    costoFinal = [[0,coste_acordado]]

    despachados_en_acuerdo = 0
    despachados_sin_acuerdo = 0

    restantes = acuerdo

    colaTrabajos = []
    dic = {"Semana":[],"Cola":[],"Arribos":[],"Autos":[],"Atenciones":[],"Atendidos":[],"Despachos":[],"Despachados":[],}
    data = pd.DataFrame(dic)
    for semana in range(1,duracion+1):

        line = pd.DataFrame({"Semana":[],"Cola":[],"Arribos":[],"Autos":[],"Atenciones":[],"Atendidos":[],"Despachos":[],"Despachados":[]})
        line.at[0,"Semana"] = semana
        line.at[0,"Cola"] = str([i.get_nombre() for i in colaTrabajos])



        if semana % 4 == 0:
            restantes = acuerdo
            costoFinal.append([semana/4,coste_acordado])


        print(f"------------------------{semana}------------------------")
        print(f"{len(colaTrabajos)} por atender")
        print([(ti.get_nombre(), ti.get_semana()) for ti in colaTrabajos],end="\n\n")


        #Cantidad de llegadas en dicha semana
        rnd_llegadas = random.random()
        llegadas = trabajos(rnd_llegadas)

        line.at[0,"Arribos"] = llegadas




        print(f"llegaron: {llegadas}")
        v = []
        for i in range(llegadas):
            t = Trabajo(semana)
            v.append(t)
            print(f"llego {t}")

        line.at[0,"Arribos"] = str([i.get_nombre() for i in v])
        colaTrabajos.append(v)
        print("\n")


        #Cantidad de trabajos atendidos en dicha semana
        rnd_resueltos = random.random()
        resueltos = int(uniforme(rnd_resueltos,a=3,b=7))
        print(f"se atendieron: {resueltos}")
        line.at[0,"Atenciones"] = resueltos

        v = []
        for i in range(resueltos):
            if len(colaTrabajos) != 0:
                print(f"se atendio {colaTrabajos[0]}")
                v.append(colaTrabajos[0])
                colaTrabajos.pop(0)

                Autos_atendidos += 1
        for i in range(len(v)):
            print(type(v))
            print("64218")
        #line.at[0,"Atendidos"] = str([i.get_nombre() for i in v])


        print("\n")


        despachados = [xi for xi in colaTrabajos if xi.get_semana()  < semana]
        colaTrabajos = [xi for xi in colaTrabajos if xi.get_semana()  >= semana]
        Autos_despachados += len(despachados)

        line.at[0,"Despachos"] = len(despachados)
        line.at[0,"Despachados"] = str([i.get_nombre() for i in despachados])


        if len(despachados) <= restantes:
            restantes -= len(despachados)
            despachados_en_acuerdo += len(despachados)
        else:
            restantes = 0
            costoFinal[-1][1] += (len(despachados) - restantes)*400
            despachados_en_acuerdo += restantes
            despachados_sin_acuerdo += len(despachados) - restantes
        data = pd.concat([data, line], ignore_index=True)


        """
        if len(despachados) <= acuerdo:
            en_acuerdo = len(despachados)
            despachados_en_acuerdo += en_acuerdo
            costo = coste_acordado

        else:
            en_acuerdo = acuerdo
            sin_acuerdo = len(despachados) - acuerdo
            despachados_en_acuerdo += en_acuerdo
            despachados_sin_acuerdo += sin_acuerdo
            costo = sin_acuerdo*400 + coste_acordado


        costoFinal.append(costo)
        """

    print(f"despachados: {len(despachados)}")
    for b in despachados:
        print(f"Se despacho {b}")
    print("\n")


    print(f"Quedaron: {len(colaTrabajos)}")
    print("\n\n")
    return Autos_atendidos,Autos_despachados,costoFinal,despachados_en_acuerdo,despachados_sin_acuerdo,data

if __name__=="__main__":
    test()


