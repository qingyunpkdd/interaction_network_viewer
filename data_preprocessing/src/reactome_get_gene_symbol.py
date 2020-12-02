import officialnamemapping as mapf
import os


def id_to_symbol(s_f="", t_f="gene_name_to_number.txt"):
    with open(s_f, 'r') as sf:
        ensembles = []
        nums = []
        for line in sf.readlines():
            if line.strip('\n') != "":
                ensemble_id, num = line.strip("\n").split("\t")
                _, *ensemble_id = ensemble_id.split(":")
                if len(ensemble_id) != 1:
                    qid = " "
                else:
                    qid = ensemble_id[0]
                ensembles.append(qid)
                nums.append(num)
    xli = ensembles
    res = mapf.getsymbol(xli, scope="ensembl.gene")
    symbols = []
    mapdict = {}
    for item_i in res:
        if "symbol" in item_i:
            mapdict[item_i['query']] = item_i["symbol"]

    for i, ens in enumerate(ensembles):
        if ens in mapdict:
            symbols.append(mapdict[ens])
        else:
            symbols.append('notfind')

    with open(t_f, 'w') as tf:
        assert len(symbols) == len(nums)
        for i, symb in enumerate(symbols):
            tf.write(symb)
            tf.write("\t")
            tf.write(nums[i])
            tf.write('\n')


if __name__ == '__main__':
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base_dir = os.path.join(base_dir_s, "data/reactome")

    sourcefile = "name_to_number.txt"
    targetfile = "gene_name_to_number.txt"

    sourcefile = os.path.join(base_dir, sourcefile)
    targetfile = os.path.join(base_dir, targetfile)

    id_to_symbol(s_f=sourcefile, t_f=targetfile)
