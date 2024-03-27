import pandas as pd
import convert_to_df

df = convert_to_df.to_df('Boca_DF.csv')

rival = 'River'

df = df.query(f"`Equipo Local` == '{rival}' or `Equipo Visitante` == '{rival}'")
df = df.reset_index(drop=True)

df.to_csv('Superclasico_DF.csv', sep=';')