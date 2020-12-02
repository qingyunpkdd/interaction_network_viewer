import os
import numpy as np
import pandas as pd
from collections import OrderedDict
import tqdm

# read gmt file and save it in a dict,the key is pathway and the element is a list of all genes in this pathway
class GmtDict(object):
    def __init__(self, file_name, seperater='\t', meta_column=[1]):
        self.fn = file_name
        self.sep = seperater
        self.meta_c = meta_column
        self.data_dict = OrderedDict()
        self.read_file()

    def read_file(self):
        with open(self.fn, 'r') as fn:
            for line in fn.readlines():
                line = line.strip('\n')
                ele_list = line.split(self.sep)
                # change to all gene name to upper case
                ele_list = [ele.upper() for ele in ele_list]
                ele_list = [ele for i, ele in enumerate(ele_list) if i not in self.meta_c]
                self.data_dict[ele_list[0]] = ele_list[1:]


class EmbeddedDict(object):
    def __init__(self, file_name, seperater='\t', with_head=True):
        self.fn = file_name
        self.sep = seperater
        self.with_head = with_head
        self.head = []
        self.data_dict = OrderedDict()
        self.read_file()

    def read_file(self):
        with open(self.fn, 'r') as fn:
            # if self.with_head:
            self.head = list(fn.readline().strip('\n').split(self.sep))
            for line in fn.readlines():
                line = line.strip('\n')
                ele_list = line.split(self.sep)
                self.data_dict[ele_list[0]] = ele_list[1:]


class MergeInColumn(object):
    def __init__(self, gmtdict_obj, embeddeddic_obj, filename=""):
        self.gmt = gmtdict_obj
        self.emb = embeddeddic_obj
        self.fn = filename

    def mergecolumn(self):

        df_emb = pd.DataFrame.from_dict(self.emb.data_dict)
        df_emb.index = self.emb.head[1:]
        df_merge = df_emb.T
        all_gene_in_emb = list(df_merge.index)

        for key, value in tqdm.tqdm(self.gmt.data_dict.items()):
            df_merge.loc[:, key] = 0
            for v in value:
                if v in all_gene_in_emb:
                    df_merge.loc[v, key] = 1

        #df_merge.fillna(0)
        df_merge.to_csv(self.fn, sep='\t')


if __name__ == '__main__':
    gmt_file = ".\\testdata\\c2.cp.reactome.v7.0.symbols.gmt"
    emb_file = "E:\\single_cell_experence\\graph_embedding\\OpenNE_mac\\result\\all_result\data\data_process_src\\testdata\\vec_all_sdne_with_genename.txt"
    out_file = "E:\\single_cell_experence\\graph_embedding\\OpenNE_mac\\result\\all_result\data\data_process_src\\testdata\\out.tsv"
    gmt_obj = GmtDict(gmt_file)
    emb_obj = EmbeddedDict(emb_file)
    merge_ic = MergeInColumn(gmt_obj, emb_obj, out_file)
    merge_ic.mergecolumn()
