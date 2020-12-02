from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
from sklearn import manifold, datasets

def reduce_tsne(data_emb, n_components=2, initx='pca' ,random_state=501):
    tsne = manifold.TSNE(n_components=n_components, 
                        init=initx, 
                        random_state=random_state)
    data_emb = tsne.fit_transform(data_emb)
    return data_emb








