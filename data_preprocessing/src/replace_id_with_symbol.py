import os


def replace(emb_f="", map_f="", emb_with_gene_name=""):
    # build mapdict
    mapdict = {}

    embgene = []
    with open(map_f, 'r') as mapf:
        for line in mapf.readlines():
            gene, No_n = line.strip('\n').split('\t')
            mapdict[No_n] = gene

    with open(emb_f, 'r') as ef:
        meta_info = ef.readline()
        # num_feature = len(meta_info.split("\t")[1:])
        for line in ef.readlines():
            line = line.strip('\n')
            No_node, *features = line.split('\t')
            if No_node in mapdict:
                gene_name = mapdict[No_node]
                embgene.append([gene_name, features])
    with open(emb_with_gene_name, 'w') as egf:
        egf.write(meta_info)
        for item_i in embgene:
            egf.write(item_i[0])
            egf.write('\t')
            features = '\t'.join(item_i[1])
            egf.write(features)
            egf.write('\n')


if __name__ == '__main__':
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # ase_dir = os.path.join(base_dir_s, "data/reactome")

    map_f = ['data/consensus/name_to_numner.txt', 'data/reactome/gene_name_to_number.txt',
             'data/regnewworks/name_to_numner.txt']
    emb_f = ['data/consensus/vec_all_consensus.txt', 'data/reactome/vec_all_reactome.txt',
             'data/regnewworks/vec_all_regnetwork.txt']
    res_emb_f = ['data/consensus/vec_all_consensus_genename.txt', 'data/reactome/vec_all_reactome_genename.txt',
                 'data/regnewworks/vec_all_regnetwork_genename.txt']
    for i, mf in enumerate(map_f):
        replace(emb_f=os.path.join(base_dir_s, emb_f[i]), map_f=os.path.join(base_dir_s, map_f[i]),
                emb_with_gene_name=os.path.join(base_dir_s, res_emb_f[i]))
