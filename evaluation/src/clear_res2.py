import os
import shutil

dataset = ["reactome", "consensus", "regnetworks"]
res_dir = "../result_directory"
for ds in dataset:
    if os.listdir(os.path.join(res_dir, ds)):
        shutil.rmtree(os.path.join(res_dir, ds))
for ds in dataset:
    if not os.path.exists(os.path.join(res_dir, ds)):
        os.mkdir(os.path.join(res_dir, ds))

