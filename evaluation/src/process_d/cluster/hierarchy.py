# from sklearn import datasets
# import pandas as pd
# import numpy as np
# import  matplotlib.pyplot as plt
# from sklearn import preprocessing
# from sklearn.cluster import AgglomerativeClustering
# from scipy.cluster.hierarchy import linkage, dendrogram
#
# def cluster(data):
#     data = np.array(iris_data[:50,1:-1])
#     min_max_scaler = preprocessing.MinMaxScaler()
#     data_M = min_max_scaler.fit_transform(data)
#     print(data_M)
#
#     plt.figure(figsize=(20,6))
#     Z = linkage(data_M, method='single', metric='cosine')
#     p = dendrogram(Z, 0)
#     plt.show()

