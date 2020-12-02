import evaluate_three
import os
from tqdm import tqdm

if __name__ == '__main__':
    data_dir = "../data"
    dataset = ["reactome", "consensus", "regnetworks"]
    embedded_dir = "embedded_vec_with_class"
    res_dir = "../result_directory"
    for ds in dataset:
        edge_file = os.path.join(data_dir, ds, "edge_list_symbole.tsv")
        embed_class_dir = os.path.join(data_dir, ds, embedded_dir)
        res_dir_each = os.path.join(res_dir, ds)
        file_name = True

        #kms = evaluate_three.KmeansC(edge_file=edge_file, max_clusters=10, emb_with_pathway="", res_dir="")
        print("processing {}".format(ds))

        for each_class in tqdm(os.listdir(embed_class_dir)):
            file_dir = os.path.join(embed_class_dir, each_class)
            res_dir_each_class = os.path.join(res_dir_each, each_class)


            if not os.path.exists(res_dir_each_class):
                os.mkdir(res_dir_each_class)
            if os.path.isfile(file_dir):
                kms = evaluate_three.KmeansC(edge_file=edge_file, max_clusters=10, emb_with_pathway="", res_dir="")
                kms.data_file = file_dir
                kms.res_dir = res_dir_each_class
                kms.initial()
                res = kms.run_all()
                kms.plt_all_res(res)
                kms.save_result()
