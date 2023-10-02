import pandas as pd

def leer_sheet(sheet_id, sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid={sheet_name}"
    df = pd.read_csv(url)
    print(df)

sheet_id = "1N87HbnPCoA_JqpLef9KkpPQcDYi4qA7Xy1DjKCsol9I"
sheet_name = "Personas"

leer_sheet(sheet_id, sheet_name)

#no funciona pandas (solucionado)
#problema con el archivo?