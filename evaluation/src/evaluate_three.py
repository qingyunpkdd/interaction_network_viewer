import pandas as pd
import numpy as np
import os
from process_d.utils.edge_list import get_edge
from process_d.utils.embedded_data import read_embdata_with_pathway
from process_d.cluster import kmean
from metrics import cluster_interaction, cluster_only, supervise_pathway_class
from process_d.utils.dimention_reduce import reduce_tsne

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class KmeansC(object):
    def __init__(self, edge_file="", emb_with_pathway="", min_clusters=3, max_clusters=100, res_dir=""):
        self.edge_file = edge_file
        self.data_file = emb_with_pathway
        self.res = None
        self.min_clusters = min_clusters
        self.max_clusters = max_clusters
        self.res_dir = res_dir

    def initial(self):
        self.edge = get_edge(self.edge_file, sep="\t", header=None)
        self.data_emb, self.data_pathway = read_embdata_with_pathway(self.data_file, sep="\t", index_col=0)
        self.all_genes = list(self.data_emb.index)

    def run_all(self):
        res_tem = {}
        res_tem["cluster_interaction_score"] = []
        res_tem["cluster_only_score"] = []
        res_tem["cluster_pathway_class_score"] = []
        self.data_emb = reduce_tsne(self.data_emb)

        if not self.res:
            for i in range(self.min_clusters, self.max_clusters + 1):
                labels = kmean.kms(self.data_emb, i, random_state=1)

                # for cluster_interaction_score
                ri = cluster_interaction.rand_index(self.edge, self.all_genes, cluster_labels=labels)
                res_tem["cluster_interaction_score"].append((i, ri))

                # for cluster_only_score
                sil_sc = cluster_only.silhouette_score(self.data_emb, labels=labels, metric="euclidean")
                res_tem["cluster_only_score"].append((i, sil_sc))

                # for cluster_pathway_class_score
                labels_index = supervise_pathway_class.get_labels_index(labels)
                purity = supervise_pathway_class.purity_pathway(self.data_pathway, labels_index=labels_index)
                res_tem["cluster_pathway_class_score"].append((i, purity))
                self.res = res_tem

        else:
            for i in range(self.min_clusters, self.max_clusters + 1):
                labels = kmean.kms(self.data_emb, i, random_state=1)

                # for cluster_pathway_class_score
                labels_index = supervise_pathway_class.get_labels_index(labels)
                purity = supervise_pathway_class.purity_pathway(self.data_pathway, labels_index=labels_index)
                res_tem["cluster_pathway_class_score"].append((i, purity))
                self.res["cluster_pathway_class_score"] = res_tem["cluster_pathway_class_score"]
        return self.res


    def plt_all_res(self, res):

        for k, v in res.items():
            x_lab = "Number of clusters"
            y_lab = "Score"
            titleplt = k
            ax_x = [va[0] for va in v]
            data_x = [va[1] for va in v]
            self.plt_one(ax_x, data_x, title=titleplt, x_lab=x_lab, y_lab=y_lab)

    def plt_one(self, ax_x, data, title="", x_lab="", y_lab=""):
        plt.plot(ax_x, data)
        plt.title(title)
        plt.xlabel(x_lab)
        plt.ylabel(y_lab)
        out_fie = os.path.join(self.res_dir, "{}".format(title))
        plt.savefig(out_fie, dpi=500)
        # plt.show()

        plt.close()

    def save_result(self):
        res_file_a = {}
        res_file_b = {}
        index_a = None
        index_b = None
        for k, v in self.res.items():
            data = [vi[1] for vi in v]

            if k != "cluster_pathway_class_score":
                index_a = [vi[0] for vi in v]
                res_file_a[k] = data
            else:
                index_b = [vi[0] for vi in v]
                res_file_b[k] = data
        self.df_to_csv(res_file_a,
                       index_a,
                       file_name="cluster_and_interaction_evaluation.tsv")
        self.df_to_csv(res_file_b,
                       index_b,
                       file_name="class_cluster_evaluation.tsv")

    def df_to_csv(self, res_file, index_, file_name):
        df = pd.DataFrame.from_dict(res_file)
        if index_:
            df.index = index_
        file_name = os.path.join(self.res_dir, file_name)
        df.to_csv(file_name, sep='\t')


if __name__ == "__main__":
    edge_file = "../data//edge_list_symbole.tsv"
    emb_with_pathway = "../data/vec_all_node2vec_with_genename_merge_c2.cp.reactome.v7.0.symbols.gmt.txt"
    res_dir = "../result_directory"
    kms = KmeansC(edge_file=edge_file, emb_with_pathway=emb_with_pathway, res_dir=res_dir)
    kms.initial()
    res = kms.run_all()
    kms.plt_all_res(res)
