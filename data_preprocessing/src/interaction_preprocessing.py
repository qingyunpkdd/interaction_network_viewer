import os


class Reactome(object):
    def __init__(self, source_file, s_sepr="\t", inter_f="edge_list.txt", name_map="Entrez", t_sepr=" ",
                 mapfile="name_to_number.txt"):
        self.s_f = source_file
        self.t_f = inter_f
        self.map_f = mapfile
        self.s_sepr = s_sepr
        self.t_sepr = t_sepr
        self.name_map = name_map

        self.map_dict = {}
        self.map_dict_recnum = -1
        self.interaction = []

    def read_file(self):
        with open(self.s_f, 'r') as sf:
            headinfo = list(sf.readline().split(self.s_sepr))
            name_to_map_index = [headinfo.index(name) for name in headinfo if self.name_map in name]
            for line in sf.readlines():
                line = line.strip('\n')
                contents = line.split(self.s_sepr)
                interactor1 = contents[name_to_map_index[0]]
                interactor2 = contents[name_to_map_index[1]]
                if interactor1 not in self.map_dict:
                    self.map_dict_recnum += 1
                    self.map_dict[interactor1] = self.map_dict_recnum
                if interactor2 not in self.map_dict:
                    self.map_dict_recnum += 1
                    self.map_dict[interactor2] = self.map_dict_recnum

                item_interaction = [self.map_dict[interactor1], self.map_dict[interactor2]]
                self.interaction.append(item_interaction)

    def write_interaction(self):
        with open(self.t_f, 'w') as tf:
            for item_i in self.interaction:
                line = self.t_sepr.join([str(item_i[0]), str(item_i[1])])
                tf.write(line)
                tf.write('\n')

    def write_mapfile(self):
        with open(self.map_f, 'w') as mf:
            for item_i, num in self.map_dict.items():
                line = self.s_sepr.join([item_i, str(num)])
                mf.write(line)
                mf.write('\n')

    def remove_dump(self):
        tem_list = []
        tem_dic = {}
        for index, item_i in enumerate(self.interaction):
            if item_i[0] not in tem_dic:
                tem_dic[item_i[0]] = []
            if item_i[1] not in tem_dic:
                tem_dic[item_i[1]] = []
            if item_i[0] != item_i[1] and (item_i[1] not in tem_dic[item_i[0]]) and (
                    item_i[0] not in tem_dic[item_i[1]]):
                tem_list.append(item_i)
                tem_dic[item_i[0]].append(item_i[1])
                tem_dic[item_i[1]].append(item_i[0])
                self.interaction = tem_list


if __name__ == '__main__':
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base_dir = os.path.join(base_dir_s, "data")

    reactome_file = "reactome.homo_sapiens.interactions.tab-delimited.txt"
    reactome_file = os.path.join(base_dir, reactome_file)

    mapfile = os.path.join(base_dir, "name_to_number.txt")
    inter_f = os.path.join(base_dir, "edge_list.txt")

    name_map = "Ensembl"
    reac = Reactome(source_file=reactome_file, name_map=name_map, mapfile=mapfile, inter_f=inter_f)
    reac.read_file()
    reac.remove_dump()

    reac.write_interaction()
    reac.write_mapfile()
