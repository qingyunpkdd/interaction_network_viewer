import numpy as np
import pandas as pd

def purity_pathway(data_pathway, labels_index):
    cluster_i_max = {}
    for k, v in labels_index.items():
        class_i = k
        cluster_count = len(v)
        cluster_i_reactome = data_pathway.iloc[v,:]
        max_pathway = cluster_i_reactome.sum(axis=0)
        max_pathway = int(np.array(max_pathway).max())
        cluster_i_max[k] = max_pathway
    purity = sum([v for v in cluster_i_max.values()])/len(labels_index)
    return purity

def get_labels_index(labels):
    labels_index = {}
    for i, la in enumerate(labels):
        if not labels_index.get(la, None):
            labels_index[la] = []
            labels_index[la].append(i)
        else:
            labels_index[la].append(i)
    return labels_index

