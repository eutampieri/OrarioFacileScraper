"""Scraper Orario Facile 7, by Eugenio Tampieri
MIT License
"""
import requests
from lxml import html
from sys import argv
from json import dumps
url = argv[1]
try:
    extended = argv[2] == "extended"
except:
    extended = False
search = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0",
                      'Accept-Encoding': ', '.join(('gzip', 'deflate')), 'Accept': '*/*', 'Connection': 'keep-alive', }).text
tree = html.fromstring(search)
orario = [[None for i in range(6)] for i in range(6)]
orainizio = []
tree = tree[2][1][0]
###########################################################
ora = 0
for ore in tree:
    g = 0
    if ora == 0:
        ora = ora+1
        continue
    for giorno in ore:
        if g == 0:
            orainizio.append(ore[0].text.strip())
            g = g+1
            continue
        deltaOre = int(giorno.attrib["rowspan"])
        a = giorno
        res = []
        for p in a:
            try:
                p_res = p[0].text
            except:
                p_res = p.text
            p_res = p_res.replace(u'\xa0', '').replace("\n", '').strip()
            if p_res != "":
                res.append(p_res)
            if (not extended) and not "".join(res).strip() == "":
                res = "".join(res)
                break
        if "".join(res) == '' or "".join(res) == ', ' or "".join(res) == "XX":
            res = None
        if orario[g-1][ora-1] == None:
            for h in range(ora-1, ora+deltaOre-1):
                orario[g-1][h] = res
        else:
            mg = g
            while not orario[mg][ora-1] == None:
                mg = mg+1
            for h in range(ora-1, ora+deltaOre-1):
                orario[mg][h] = res
        g = g+1
    ora = ora+1
###########################################################
gg = 1
print(dumps({"orario": orario, "ore": orainizio}))
