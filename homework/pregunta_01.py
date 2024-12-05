"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
      lines = file.readlines()

    # for i in range(6):
    #     print(i, lines[i])

    info = lines[4:]

    data = [["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]]

    listAux = []
    primera = True
    for linea in info:
        linea.strip()
        linea = linea.split()
        if len(linea) > 0 and primera:
          listAux.append(int(linea[0]))
          listAux.append(int(linea[1]))
          listAux.append(float(linea[2].replace(',','.')))
          listAux.append(" ".join(linea[4:]))
          primera = False

        elif len(linea) > 0:
          listAux.append(" ".join(linea))

        else:
          primera = True
          listAux[3] = ' '.join(listAux[3:]).replace('.','')
          data.append(listAux[:4])
          listAux = []

    return pd.DataFrame(data[1:], columns= data[0])

#print(pregunta_01())
