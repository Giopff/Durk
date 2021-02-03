import xml.etree.ElementTree as ET
from copy import copy



def dictify(r,root=True):

    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    # print(d)
    # d['times']=times
    if r.text and r.text[0:3]!='\n  ':
        d["_text"]=r.text
        
    for x in r.findall("./*"):
        # print(x.tag)
        # print(r.findall("./*"))
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

def parse(fileName):
    root = ET.parse(fileName).getroot()
    return dictify(root)

if __name__=="__main__":
    
    print(parse('thefile.html'))

