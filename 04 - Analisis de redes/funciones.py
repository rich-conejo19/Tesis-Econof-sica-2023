import pandas as pd

def ranking(data_file, pais=None):
    
    '''
    Calcula un dataframe con las clasificaciones de cada una de 
    las columnas de otro dataframe dado previamente en el 
    parámetro 'data_file'
    
    
    Parámetros
    ----------
    data_file : Un diccionario o un DataFrame de la librería pandas
      El archivo que contiene los datos.

    pais : string, opcional (default=None)
      Si el argumento 'data_file' es un diccionario, este parámetro es necesario,
      ya que actuará como una clave del diccionario
      
    Resultados
    -------
    ranked_dataframe : Dataframe de la libreria Pandas
      Un dataframe de pandas con la información rankeada
    
    '''
    
    #Checa si tengo un data frame
    if isinstance(data_file, pd.core.frame.DataFrame):
        dataframe = data_file
    
    #Si no, entonces obtenemos del diccionario el dataframe
    else:
        dataframe = data_file[pais]
    
    #Estas seran las columnas del dataframe
    columns = dataframe.columns[1:]
    sort_dfs=[]
    
    for vector in list(columns):
        #Para cada variable economica, creamos un dataframe donde se ordenan los sectores
        df= pd.DataFrame({'Sector' : list(dataframe['Sector']),
                          vector     : list(dataframe[vector]) })
        df= df.sort_values(by=vector, ascending= False).reset_index(drop=True)
        df.index+=1
        sort_dfs.append(df)
        
    #Finalmente se juntan todos en uno con columnas jerárquicas
    return pd.concat(sort_dfs, keys=columns, axis=1)



def medidas_dispersion_muestral(data_file, pais=None):
    
    '''
    Esta función obtiene un dataframe con las medidas muestrales de tendencia central y dispersión
    de cada una de las columnas de otro dataframe dado previamente en el  parámetro 'data_file'
        
    
    Parámetros
    ----------
    data_file : Un diccionario o un dataframe de pandas
      El archivo que contiene los datos
      
    pais : string, opcional (default=None)
      Si el parámetro 'data file' es un diccionario, entonces este parámetro  se usará
      como llave para del diccionario

      
    Resultados
    -------
    dataframe : Un dataframde  la libreria pandas
      Un dataframe de pandas con las tendencias centrales y la dispersión.
      
    Notas
    -------
    Las medidas centrales y de dispersión utilizadas en esta función son: 
    media, mediana, varianza, desviación estándar, asimetría, curtosis

    '''
    
    if isinstance(data_file, pd.core.frame.DataFrame):
        dataframe = data_file
    
    else:
        dataframe = data_file[pais]
    
    
    df = pd.DataFrame(columns=['Datos','Media','Mediana', 'Varianza', 'Desviacion estandar', 
                               'Asimetria', 'Curtosis'])

    nombres_lista= list(dataframe.columns)
    nombres_lista.remove('Sector')
    
    for i in range(len(nombres_lista)):
        medidas=[dataframe[nombres_lista[i]].mean() , dataframe[nombres_lista[i]].median(), 
                            dataframe[nombres_lista[i]].var()  , dataframe[nombres_lista[i]].std(), 
                            dataframe[nombres_lista[i]].skew() , dataframe[nombres_lista[i]].kurt()]
        
        df.loc[i] = [nombres_lista[i]] + medidas

    return df

