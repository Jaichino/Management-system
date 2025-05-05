##############################################################################
# Fichero para realizar importación de base de datos vieja
##############################################################################

import sqlite3
import pandas as pd

def importar_datos():

    # Establecer conexión con la base de datos
    conn = sqlite3.connect("bla_estetica.db")

    # Leer archivos .csv a migrar
    df_clientes = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\clientes_bd.csv", sep=";")
    df_ventas = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\ventas.csv", sep=";")
    df_ccorriente = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\cuentacorriente.csv", sep=";")

    # Insertar datos en tabla existente

    df_clientes.to_sql("cliente", conn, if_exists='append', index=False)
    df_ventas.to_sql("venta", conn, if_exists='append', index=False)
    df_ccorriente.to_sql("cuentacorriente", conn, if_exists='append', index=False)

    conn.close()


if __name__ == '__main__':
    pass
    #importar_datos()
