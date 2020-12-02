import matplotlib as plt

def tsne_plot(embedding, expression_value, cmaps="PuRd"):
    plt.scatter(embedding[:, 0], embedding[:, 1], lw=0.1, c=expression_value, cmap=plt.cm.get_cmap('PuRd'))
    plt.colorbar(label='expression value')
    plt.show()


