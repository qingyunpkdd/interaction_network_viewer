from interaction_preprocessing import Reactome
import os


class Consensus(Reactome):
    def read_file(self):
        with open(self.s_f, 'r') as sf:
            metainfo = sf.readline()
            headinfo = list(sf.readline().split(self.s_sepr))
            index_inter = [headinfo.index(name) for name in headinfo if self.name_map in name]
            for line in sf.readlines():
                line = line.strip('\n')
                contents = line.split(self.s_sepr)
                interaction = contents[index_inter[0]]
                inter_1, *inter_2 = interaction.split(',')
                if len(inter_2) != 1:
                    continue
                interactor1, *sp1 = inter_1.split('_')
                interactor2, *sp2 = inter_2[0].split('_')
                if sp2[0] != sp2[0] or sp1[0] != "HUMAN":
                    continue
                if interactor1 not in self.map_dict:
                    self.map_dict_recnum += 1
                    self.map_dict[interactor1] = self.map_dict_recnum
                if interactor2 not in self.map_dict:
                    self.map_dict_recnum += 1
                    self.map_dict[interactor2] = self.map_dict_recnum

                item_interaction = [self.map_dict[interactor1], self.map_dict[interactor2]]
                self.interaction.append(item_interaction)


if __name__ == '__main__':
    s_sepr = "\t"
    source_file = "ConsensusPathDB_human_PPI.txt"
    name_map = "interaction_participants"
    mapfile = "name_to_numner.txt"
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base_dir = os.path.join(base_dir_s, "data/consensus")

    source_file = os.path.join(base_dir, source_file)

    mapfile = os.path.join(base_dir, mapfile)
    inter_f = os.path.join(base_dir, "edge_list.txt")

    reac = Consensus(source_file=source_file, name_map=name_map, mapfile=mapfile, inter_f=inter_f)
    reac.read_file()
    reac.remove_dump()

    reac.write_interaction()
    reac.write_mapfile()
    
