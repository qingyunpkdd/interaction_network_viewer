from sklearn import metrics

#silhouette_score
def silhouette_score(data_emb, labels, metric):
    r = metrics.silhouette_score(data_emb, labels, metric=metric)
    return r



