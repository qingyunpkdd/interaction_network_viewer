import os
import embedded_gmt_merge as egmg
def runall():
    pass

#all_dir = ["consensus","reactome","regnewworks"]
all_dir = ["reactome"]
base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
all_dir = [os.path.join(base_dir_s, each_path) for each_path in all_dir]

gmt_files = [os.path.join(base_dir_s, 'gene_set', each_path) for each_path in os.listdir(os.path.join(base_dir_s, 'gene_set'))]

for each_dir in all_dir:
    each_path = [eachfile for eachfile in os.listdir(each_dir)]
    for file_a in each_path:
        file_i = os.path.join(each_dir, file_a)
        if os.path.isfile(file_i):
            if "vec_all" in str(file_i) and "_with_genename.txt" in str(file_i):
                emb_file = file_i
                for gmt_file in gmt_files:
                    merge_file = str(file_i).replace('.txt', '_merge_{}.txt'.format(os.path.split(gmt_file)[-1]))
                    gmt_obj = egmg.GmtDict(file_name=gmt_file)
                    emb_obj = egmg.EmbeddedDict(file_name=emb_file)
                    merge_ic = egmg.MergeInColumn(gmt_obj, emb_obj, merge_file)
                    merge_ic.mergecolumn()
                    del gmt_obj
                    del emb_obj
                    del merge_ic
                del file_i
                del file_a


