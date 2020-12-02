from interaction_preprocessing import Reactome
import os

if __name__ == '__main__':
    s_sepr = "\t"
    source_file = "human_inter.txt"
    name_map = "symbol"
    mapfile = "name_to_numner.txt"
    base_dir_s = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base_dir = os.path.join(base_dir_s, "data/regnewworks")

    source_file = os.path.join(base_dir, source_file)

    mapfile = os.path.join(base_dir, mapfile)
    inter_f = os.path.join(base_dir, "edge_list.txt")

    reac = Reactome(source_file=source_file, name_map=name_map, mapfile=mapfile, inter_f=inter_f)
    reac.read_file()
    reac.remove_dump()

    reac.write_interaction()
    reac.write_mapfile()
