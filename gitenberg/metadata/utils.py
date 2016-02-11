marc_rels = {
    'aut': 'author',
    "adp": "adapter",
    "aft": "author_of_afterword",
    "ann": "annotator",
    "arr": "arranger",
    "art": "artist",
    "aui": "author_of_introduction",
    "clb": "collaborator",
    "cmm": "commentator",
    "cmp": "composer",
    "cnd": "conductor",
    "com": "compiler",
    "ctb": "contributor",
    "dub": "dubious_author",
    "edt": "creator/editor",
    "egr": "engineer",
    "ill": "illustrator",
    "lbt": "librettist",
    "oth": "other_contributor",
    "pbl": "publisher_contributor",
    "pht": "photographer",
    "prf": "performer",
    "prt": "printer",
    "res": "researcher", 
    "trc": "transcriber",
    "trl": "translator",
    "unk": "unknown_contributor",
    }

inverse_marc_rels = {v:k for k,v in  marc_rels.items()}

def plural(key):
    if key.endswith('s'):
        return key+'es'
    else:
        return key+'s'

def reverse_name(name):
    tokens = name.split(' ')
    if len(tokens)>1:
        return tokens[-1] + ', ' + ' '.join(tokens[0:-1])
