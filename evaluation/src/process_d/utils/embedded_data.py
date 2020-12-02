import numpy as np
import pandas as pd



def read_embdata_with_pathway(filename="", sep="\t", index_col=0):
    data = pd.read_csv(filename,
                        sep=sep, 
                        index_col=index_col)
    try:
        data.drop(labels=["notfind"], inplace=True)
    except:
        print("all gene were find!")
    data_emb = data.iloc[:, :128]
    data_pathway = data.iloc[:, 128:]
    return data_emb, data_pathway

