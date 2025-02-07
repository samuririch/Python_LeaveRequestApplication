import pandas as pd
import openpyxl
from st_aggrid import AgGrid
import os

def loadMainBook(option):
    directory = "C:/Users/bigra/Documents"
    filename = 'employeeRecords.xlsx'
    filepath = os.path.join(directory, filename)
    try:
        dataframe1 = pd.read_excel(filepath)
        print(dataframe1)
        df_user = dataframe1[dataframe1["Employee Name"] == option]
        AgGrid(df_user)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found in the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


