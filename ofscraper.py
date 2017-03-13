"""Scraper Orario Facile 7, by Eugenio Tampieri
MIT License
"""
import requests
from lxml import html
from sys import argv
from json import dumps
url = argv[1]
try:
    extended = argv[2]=="extended"
except:
    extended = False
search = requests.get(url,headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0", 'Accept-Encoding': ', '.join(('gzip', 'deflate')),'Accept': '*/*','Connection': 'keep-alive',}).text
tree = html.fromstring(search)
orario=[]
tree = tree[2][1][0]
for i in range(6):
    orario.append([None, None, None, None, None, None])
###########################################################
ora=0
for ore in tree:
    g=0
    if ora==0:
        ora=ora+1
        continue
    for giorno in ore:
        if g==0:
            g=g+1
            continue
        deltaOre=int(giorno.attrib["rowspan"])
        a = giorno
        res=""
        for p in a:
            try:
                res=res+p[0].text
            except:
                res=res+p.text
            res=res+" "
            if (not extended) and not res.strip()=="":
                break
        res=res.replace(u'\xa0', '').replace("\n",'').strip()
        if res=='' or res==', ' or res=="XX":
            res=None
        if orario[g-1][ora-1] == None:
            for h in range(ora-1,ora+deltaOre-1):
                orario[g-1][h]=res
        else:
            mg=g
            while not orario[mg][ora-1] == None:
                mg=mg+1
            for h in range(ora-1,ora+deltaOre-1):
                orario[mg][h]=res
        g=g+1
    ora=ora+1
###########################################################
gg=1
print dumps(orario)
