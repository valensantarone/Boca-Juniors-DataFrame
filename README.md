# Boca Juniors DataFrame

## DataFrame with all the official Boca Juniors matches played.

Usando la página web [Historia de Boca](https://www.historiadeboca.com.ar), scrapea todos los partidos en la lista que devuelve la página cuando buscamos por una competición y año en específico.

El archivo [scrap_url.ipynb](scrap_url.ipynb) tiene la funciones con las que se creó el Boca_DF, que contiene la información y URL de la propia página de Historia de Boca de todos los partidos oficiales de la historia del club ordenados por fecha.

El módulo [covert_to_df.py](convert_to_df.py) convierte el archivo '.csv' para que sea un DataFrame válido para ser usado con pandas.

El archivo [historiales.ipynb](historiales.ipynb) utiliza la librería de matplotlib para crear gráficos de barra que muestran la evolución en el historial de Boca contra un equipo indicado en partidos oficiales de toda la historia.

La carpeta [fonts](fonts/) contiene fuentes de Helvetica, algunas se usaron para estilizar el gráfico de matploblib.

Pronto se añadirán más funciones y la posibilidad de incluír partidos amistosos.