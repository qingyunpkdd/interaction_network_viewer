import numpy as np
import sklearn
import pandas as pd
from collections import Counter
from scipy.special import comb
import itertools


#edge's node as symbole or name
def rand_index(edge, all_gene, cluster_labels):
    TP=0
    for edgex in edge:
        if cluster_labels[all_gene.index(edgex[0])] == cluster_labels[all_gene.index(edgex[1])]:
            TP += 1

    FP=len(edge) - TP


    TN=0
    counteach = Counter(list(cluster_labels))
    for k, v in counteach.items():
        TN += comb(int(v), 2)

    Totle = comb(len(edge), 2)

    FN = Totle - TP - FP -TN
    #print(TP, FP, TN, FN)
    TP = TP/(len(edge)/(Totle-len(edge)))
    FP = FP/(len(edge)/(Totle-len(edge)))

    TN = TN/((Totle-len(edge))/len(edge))
    FN = FN/((Totle-len(edge))/len(edge))


    #print(TP, FP, TN, FN)

    RI = (TP + TN)/(TP + FP +TN + FN)
    return RI


def get_distance(data_emb, edge_file=""):
    n_samples = data_emb.shape[0]

    distance_array = np.ones((n_samples, n_samples))

    edge_list_symb = pd.read_csv(edge_file, header=None)
    edge = edge_list_symb.tolist()
    edge = [tuple(itm) for itm in edge]

    all_gene = data_emb.index

    error_list = 0
    for edgex in edge:
        try:
            x = all_gene.index(edgex[0])
            y = all_gene.index(edgex[1])
            distance_array[x,y] = 0
        except:
            error_list +=1
    return distance_array


def silhouette_score(distance_array, labels, metric="precomputed"):
    score = sklearn.metrics.silhouette_score(distance_array, 
                                            labels, 
                                            metric="precomputed")
    return score





