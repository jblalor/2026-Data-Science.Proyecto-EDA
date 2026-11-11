# encoding: utf-8

# Funciones para el proyecto EDA del bootcamp de Ciencia de Datos con IA. 

# $Version: 1 $, $Fecha: 2026-11-09 (lun, 09 nov 2026). Por Julio Blanco Lorenzo. 


import pandas as pd
import inspect


def filtrar_registros(df_in, cols_cat, cols_num):
    """
    Filtra un dataset por filas de acuerdo a unos criterios especificados. 
    
    Entradas: 
       df_in: dataset de entrada. Tipo: DataFrame de Pandas. 
       cols_cat: diccionario en el que las claves son nombres de columnas 
                 del dataset, y los valores los criterios de filtrado. Se 
                 descartarán los registros en los que los valores de las 
                 columnas correspondientes no coincidan con alguno de los 
                 indicados aquí. Como valores se pueden dar valores 
                 individuales o listas de valores. 
       cols_num: diccionario en el que las claves son nombres de columnas 
                 del dataset (típicamente con datos numéricos continuos), 
                 y los valores son tuplas con los siguientes 3 elementos, 
                 por orden: 
                 1. Palabras clave 'mode', 'mean', 'max', 'min', ó 'median', 
                    o un número. 
                    Si es una de las palabras clave indicadas, se considera 
                    el agregado correspondiente de la columna (calculado en 
                    cada paso de filtrado) como criterio de filtrado. Si es 
                    un número, se considera el número como criterio de filtrado. 
                    Tipo: str ó float. 
                 2. Tanto por uno del límite inferior del rango de filtrado. 
                    El límite inferior se calcula como el número calculado o 
                    dado en el primer elemento de la tupla, por este valor. 
                    Tipo: float. 
                 3. Tanto por uno del límite superior del rango de filtrado. 
                    El límite superior se calcula como el número calculado o 
                    dado en el primer elemento de la tupla, por este valor. 
                    Tipo: float. 
                 Se descartarán los registros en los que los valores de las 
                 columnas correspondientes no se encuentren entre los límites 
                 inferior y superior del rango de filtrado. 
    
    Salidas:
       df_out: dataset filtrado. Tipo: DataFrame de Pandas. 
    
    """
    #
    
    # $Version: 1 $, $Fecha: 2026-11-09 (lun, 09 nov 2026). Por Julio Blanco Lorenzo. 
    
    
    nomfun = inspect.currentframe().f_code.co_name
    
    df_out = df_in.copy()
    try:
        df_out = df_out.fillna(0)
    except:
        pass
    print(f'\n-{nomfun}-: \nLongitud del dataset de entrada: {len(df_out)}')
    
    for k in cols_cat.keys():
        if k in df_out.columns:
            if type(cols_cat[k]) in [list, tuple]:
                lst_val = cols_cat[k]
            else:
                lst_val = [cols_cat[k]]
            msk = (df_out[k].isin(lst_val))
            df_out = df_out[msk]
            print(f'\n-{nomfun}-: \nLongitud del dataset tras filtrado por {k}: {len(df_out)}')
    
    for k in cols_num.keys():
        if k in df_out.columns:
            val = 0
            if cols_num[k][0] in ['mode', 'mean', 'median', 'max', 'min']:
                try:
                    val = df_out[k].agg(cols_num[k][0])
                    if cols_num[k][0] == 'mode':
                        val = val[0]
                except:
                    pass
            else:
                val = cols_num[k][0]
            
            lim_inf = cols_num[k][1] * val
            lim_sup = cols_num[k][2] * val
            msk = (df_out[k].between(lim_inf, lim_sup))
            df_out = df_out[msk]
            print(f'\n-{nomfun}-: \nLongitud del dataset tras filtrado por {k}: {len(df_out)}')
    
    return df_out


def encontrar_mas_parecido(regis, df, cols_cat, cols_num):
    """
    Devuelve el registro más parecido de un dataset a un registro de 
    entrada dado, teniendo en cuenta unos criterios especificados. 
    
    Entradas: 
       regis: fila de DataFrame de Pandas. Es decir, serie de Pandas. 
       df: Dataframe de Pandas en el que se buscará el registro más 
           parecido al de entrada (regis). 
       cols_cat: diccionario en el que cada clave es el nombre de una 
                 columna de regis y de df, y cada valor es el factor 
                 de ponderación /escalado a aplicar a la diferencia 
                 dif_k entre los valores de la columna correspondiente 
                 de regis y de df; w_k. Si el valor del registro de df 
                 coincide con el de regis en la columna k especificada 
                 en cols_cat, dif_k = 0, y si no, dif_k = 1. 
                 Los factores de ponderación deberían ser no negativos. 
       cols_num: diccionario en el que cada clave es el nombre de una 
                 columna con datos numéricos de regis y de df, y cada valor 
                 es el factor de ponderación/escalado a aplicar a la diferencia 
                 en valor absoluto dif_k entre los valores de la columna 
                 correspondiente de regis y de df; w_k. 
                 
    La métrica con la que se evalúa el grado de parecido entre cada registro 
    de df y regis se calcula como Sumatorio_k (w_k * dif_k), siendo como 
    mínimo igual a 0 (lo cual ocurrirá si los registros tienen los mismos 
    datos en todas las columnas especificadas cols_cat y cols_num). 
    
    Salidas: 
       regis_out: registro más parecido a regis encontrado en el dataset de 
                  entrada. Fila de DataFrame de Pandas. 
       dif: Sumatorio_k (w_k * dif_k) para regis_out. 
    
    """
    #
    
    # $Version: 1 $, $Fecha: 2026-11-09 (lun, 09 nov 2026). Por Julio Blanco Lorenzo. 
    
    
    nomfun = inspect.currentframe().f_code.co_name
    
    regis_out = None
    dif = None
    difs = pd.Series()
    
    ejec = True
    sigue = True
    fila = []
    
    for k in (list(cols_cat.keys()) + list(cols_num.keys())):
        if not (k in regis.index and k in df.columns):
            ejec = False
            print(f'\n-{nomfun}-: \nERROR: La columna {k} no se encuentra en regis y en df. \n')
    
    if ejec == True:
        regis_ = regis.copy()
        try:
            regis_ = regis_.fillna(0)
        except:
            pass
        i = 0
        while sigue == True and i < len(df) - 0.1:
            fila = df.iloc[i]
            fila = fila.fillna(0)
            dif_i = 0
            for k in cols_cat.keys():
                if regis[k] != fila[k]:
                    dif_i += cols_cat[k]
            for k in cols_num.keys():
                try:
                    dif_i += cols_num[k] * abs(regis_[k] - fila[k])
                except:
                    pass
            
            difs[i] = dif_i
            if dif_i == 0:
                sigue = False
            else:
                i += 1
        
        if sigue == False:
            regis_out = fila
            dif = 0
        else:
            regis_out = df.iloc[difs.idxmin()]
            dif = difs[difs.idxmin()]
    else:
        print(f'\n-{nomfun}-: \nERROR: No se ejecuta función por no encontrarse todas las columnas\
              \nde cols_cat y cols_num tanto en regis como en df. \n')
    
    return regis_out, dif


