'''this module to visualize the gene expression by gene gene interaction graph embedding. '''
import pandas as pd
import numpy as np
import os


class LoadVec(object):
    def __init__(self, vec_f='', sepr='\t'):
        self.vec_f = vec_f
        self.sepr = sepr
        self.vecdata = None
        self.readdata()

    def readdata(self):
        self.vecdata = pd.read_csv(self.vec_f, index_col=0, sep=self.sepr)
        self.dropdump()

    def dropdump(self):
        self.vecdata['genename'] = list(self.vecdata.index)
        self.vecdata.drop_duplicates(subset=['genename'], keep='first', inplace=True)
        self.vecdata = self.vecdata[self.vecdata['genename'] != 'notfind']
        self.vecdata.drop(['genename'], axis=1, inplace=True)


class MergeExpress(object):
    def __init__(self, mergeby="class"):
        self.mergeby = mergeby
        self.exprdata = None
        self.vecdata = None
        self.final_df = None

        self.merged_df = None

    def loadexpr(self, exprdf):
        # assert type(exprdf) == pd.core.frame.DataFrame
        self.exprdata = exprdf.expr_df

    def loadvec(self, vecdata):
        self.vecdata = vecdata.vecdata

    def merge(self, method="all"):
        if method == "all":
            vdf = self.vecdata
            vdft = pd.DataFrame(vdf.values.T, index=vdf.columns, columns=vdf.index)

            all_genes = list(vdft.columns)

            group_sum = self.exprdata.groupby(self.exprdata[self.mergeby]).sum()
            group_max = self.exprdata.groupby(self.exprdata[self.mergeby]).max()
            group_mean = self.exprdata.groupby(self.exprdata[self.mergeby]).mean()
            group_median = self.exprdata.groupby(self.exprdata[self.mergeby]).median()

            group_sum.index = ["sum_" + i for i in group_sum.index]
            group_max.index = ["max_" + i for i in group_max.index]
            group_mean.index = ["mean_" + i for i in group_mean.index]
            group_median.index = ["median_" + i for i in group_median.index]

            group_sum = group_sum[set(all_genes).intersection(set(group_sum.columns))]
            group_max = group_max[set(all_genes).intersection(set(group_max.columns))]
            group_mean = group_mean[set(all_genes).intersection(set(group_mean.columns))]
            group_median = group_median[set(all_genes).intersection(set(group_median.columns))]

            print("{num} genes were found!".format(num=len(set(all_genes).intersection(set(group_sum.columns)))))

            df = pd.concat([group_sum, group_max, group_mean, group_median])
            self.final_df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)

            frames = [df, vdft[list(df.columns)]]
            mgd = pd.concat(frames)
            self.merged_df = pd.DataFrame(mgd.values.T, index=mgd.columns, columns=mgd.index)

    def save_to_csv(self, cells_merge_f, all_merge_f):
        self.final_df.to_csv('{}.csv'.format(cells_merge_f))
        self.merged_df.to_csv('{}.csv'.format(all_merge_f))


class LoadExpression(object):
    def __init__(self, expr_f='', sepr=","):
        self.expr_f = expr_f
        self.sepr = sepr
        self.expr_df = None
        self.loaddata()

    def loaddata(self):
        self.expr_df = pd.read_csv(self.expr_f)


if __name__ == '__main__':
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    vecf = "data/consensus/vec_all_consensus_genename.txt"

    exprdata = "data/expression/xin2016_pancreas_human.csv"

    cells_merge = "data/expression/cells_merge"
    all_merge = "data/expression/all_merge"

    all = [os.path.join(base_dir_s, i) for i in [vecf, exprdata, cells_merge, all_merge]]
    loadvec = LoadVec(all[0])

    loadexpr = LoadExpression(all[1])

    merg = MergeExpress(mergeby="class")
    merg.loadvec(loadvec)
    merg.loadexpr(loadexpr)
    merg.merge()

    merg.save_to_csv(all[2], all[3])
