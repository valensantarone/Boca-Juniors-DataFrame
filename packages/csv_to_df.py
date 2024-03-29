# Convert the specified '.csv' file to a DataFrame ready to use with pandas
def to_df(filename):
    import pandas as pd
    
    df = pd.read_csv(filename, sep=';')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df = df.reset_index(drop=True)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    return df