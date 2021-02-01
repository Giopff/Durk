import xml.etree.ElementTree as ET
from copy import copy



def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text and r.text[0:3]!='\n  ':
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d
# def listify(r,root=True):
#     if root:
#         return {r.tag : listify(r, False)}
#     d=copy(r.attrib)
#     # if r.text and r.text[0:3]!='\n  ':
#         # d["_text"]=r.text
#     for x in r.findall("./*"):
#         if x.tag not in d:
#             d[x.tag]=[]
#         d[x.tag].append(listify(x,False))
#     return d

# def parse_tags(fileName):
#     root = ET.parse(fileName).getroot()
#     return listify(root)

def parse(fileName):
    root = ET.parse(fileName).getroot()
    return dictify(root)

if __name__=="__main__":
    
    print(parse('thefile.html'))
    # print(parse_tags('thefile.html'))

