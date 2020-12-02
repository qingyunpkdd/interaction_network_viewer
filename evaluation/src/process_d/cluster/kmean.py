from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans

from sklearn import manifold, datasets

def kms(data_emb, n_clusters, random_state=1):
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=1).fit(data_emb)
    labels = kmeans_model.labels_
    return labels
