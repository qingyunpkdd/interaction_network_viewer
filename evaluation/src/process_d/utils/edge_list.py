import pandas as  pd
import numpy as np

def get_edge(edge_list_symbole_file = "", sep="\t", header=None):
    edge_list_symb = pd.read_csv(edge_list_symbole_file, sep=sep, header=header)
    edge_list_symb = np.array(edge_list_symb)
    edge = edge_list_symb.tolist()
    edge = [tuple(itm) for itm in edge]
    return edge

'''

edge example:
[('EEF2KMT', 'EEF2'),
 ('KCNK9', 'KCNK3'),
 ('ATXN3', 'RAD23A'),
 ('CAMK4', 'KPNA2'),
 ('EP300', 'UBE2I'),
 ('POLD3', 'UBE2B'),
 ('RRAGC', 'RRAGA'),
 ('GRIN2A', 'GRIN2D'),
 ('REV1', 'RPA2'),
 ('P2RY1', 'GNAQ')]

'''






