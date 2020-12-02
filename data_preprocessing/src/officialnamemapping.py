import mygene

# ref:https://nbviewer.jupyter.org/gist/newgene/6771106
'''
this function is to mapping the original symbol to all kinds of id!
https://nbviewer.jupyter.org/gist/newgene/6771106
'''


def getid(xli=[], field=''):
    # xli = ['DDX26B',
    #  'CCDC83',
    #  'MAST3',
    #  'FLOT1',
    #  'RPL11',
    #  'ZDHHC20',
    #  'LUC7L3',
    #  'SNORD49A',
    #  'CTSH',
    #  'ACOT8']
    # out = mg.querymany(xli, scopes='symbol', fields='entrezgene', species='human')
    mg = mygene.MyGeneInfo()
    return mg.querymany(xli, scopes='symbol', fields=field, species='human')


def getsymbol(xli=[], scope=""):
    mg = mygene.MyGeneInfo()

    return mg.querymany(xli, scopes=scope, fields='symbol', species='human')


if __name__ == '__main__':
    xli = ["ENSG00000145335", "ENSG00000136156", "abc", "abc"]
    res = getsymbol(xli, scope="ensembl.gene")
    print("-------" * 10)
    print(res)
'''
[{'query': 'ENSG00000145335', '_id': '6622', '_score': 18.832573, 'symbol': 'SNCA'}, {'query': 'ENSG00000136156', '_id': '9445', '_score': 19.916004, 'symbol': 'ITM2B'}, {'query': 'abc', 'notfound': True}]

'''
