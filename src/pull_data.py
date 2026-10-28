import numpy as np
import pandas as pd
from pathlib import Path


DATA_LIST = [ r"data\Axel T. Brunger Dataset (Dimensions).xlsx",
              r"data\Courtney A. Miller Dataset (Dimensions).xlsx",
              r"data\Jawahar Sudhamsu Datasets (Dimensions).xlsx",
              r"data\Ottmann C. Dataset (Dimensions).xlsx",
              r"data\Richard A. Cerione Dataset (Dimensions).xlsx"
            ]

USE_COLS = ["Publication ID",
            "DOI",
            "PMID",
            "PMCID",
            "Title",
            "Authors",
            "Research ID",
            "Authors (Raw Affiliation)",
            "Corresponding Authors",
            "Source Linkout"
            ]

def load_csv(paths):
    """
    Take in some collection of relative paths to author-specific data in .xlsx files and returns a list of dataframes, each containing: 
        - Publication ID
        - DOI
        - PMID
        - PMCID
        - Title
        - Authors
        - Research ID
        - Authors (Raw Affiliation)
        - Corresponding Authors
        - Source Linkout
    """
    ret_list = list()
    for i in range(len(paths)):
        
        df = pd.read_excel(paths[i], usecols=USE_COLS)
        ret_list.append(df)
    
    return ret_list


