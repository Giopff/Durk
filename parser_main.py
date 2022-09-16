import xml.etree.ElementTree as ET
from copy import copy
import tinycss2
import re


def dictify(r,root=True):

    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text and r.text[0:3]!='\n  ':
        d["_text"]=r.text
        
    for x in r.findall("./*"):
        # print(x.tag)
        # print(r.findall("./*"))
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

def isolation(item,List):
  Output=[]
  for thing in List:
    if thing==item:
      Output.append(thing)
  return Output

def order(root):
    elemList = []
    parsed=parse('thefile.html')
    for elem in root.iter():
        elemList.append(elem.tag)
    
    elemList=elemList[elemList.index("body")+1:]
    # print(elemList)
    # for some in elemList:
    #     # print(L)
    #     if some not in parsed['html']['body'][0].keys():
    #         # print("entered",L)
    #         elemList.remove(some)

    # print(elemList)
    # for i in range(0,len(elemList)):
    #     for z in parsed['html']['body'][0][elemList[i]]:
    for i in list(set(elemList)):
        # print(i)
        try:
            z=len(isolation(i,elemList))-len(parsed['html']['body'][0][i])
            for rand in range(0,z):
                elemList.remove(i)
        except:
            pass


    return elemList

    
def parse(fileName):
    root = ET.parse(fileName).getroot()
    return dictify(root)
def parse_order(fileName):
    root = ET.parse(fileName).getroot()
    return order(root)
def orderify(order,unordered):
    arr=[]

    for i in range(0,len(order)):
        try:
            arr.append({order[i]:unordered['html']['body'][0][order[i]][func(i,order,order[i])]})
            # print(order[i])
            # print(unordered['html']['body'][0][order[i]][func(i,order,order[i])])
        # print(func(i,order,order[i]))
        except:
            pass

    return arr
        
    

def func(index,List,item):
  times=0
  for number in range(0,index):
    if List[number]==item:
      times+=1
  return times




def cssParse(name):
    with open(name) as idk:
        rules = tinycss2.parse_stylesheet(idk.read(),skip_whitespace=True)
    dicti={}
    for rule in rules:
        x=rule.serialize()
        z=x.find("{")
        parsed=re.sub("\n","",x)[z+1:-1].split(";")[:-1]
        dicti[x.split(" ")[0]]=None
        idkman={}
        for i in parsed:
            idkman[i.strip().split(":")[0].strip()]=i.strip().split(":")[1].strip()
        dicti[x.split(" ")[0]]=idkman
    return dicti
if __name__=="__main__":
    
    # print(parse('thefile.html'))
    # print(parse_order('thefile.html'))
    print(orderify(parse_order('thefile.html'),parse('thefile.html')))
    # print(order(ET.parse('thefile.html').getroot()))
