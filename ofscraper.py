"""Scraper Orario Facile 7, by Eugenio Tampieri
MIT License
"""
import urllib2
from lxml import html
from sys import argv
from json import dumps
url = argv[1]
try:
    extended = argv[2]=="extended"
except:
    extended = False
search = urllib2.urlopen(url).read()
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
        a = giorno[0]
        b = giorno[1]
        try:
            a = a[0]
        except IndexError:
            pass
        try:
            b = b[0]
        except IndexError:
            pass
        res=a.text
        if extended:
            res=res+", "+b.text
        res=res.replace(u'\xa0', '').replace("\n",'')
        if res=='' or res==', ':
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
