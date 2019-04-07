import re
import files
import baza

poisk=r'>(\w*-11).*?(\d\d[.]\d\d[.]\d\d\d\d).*?>[0-9]+?<.*?>([0-9]+?)<'

def regular(poisk, text):
    result=re.findall(poisk, text)
    return result

def sravnenie(dict1, dict2):
    slovar = {}
    for f in dict1.keys():
        if not dict1[f] == dict2[f]:
            slovar[f] = [dict1[f], dict2[f]]
    return slovar

def vk_id(examen, file):
    t = files.vivod(file)
    for ex in examen.keys():
        if ex in t.keys():
            for d in t[ex]:
                print(d, ' Экзамен:', ex, ' Было:', examen[ex][0], ' Стало:', examen[ex][1])
                print()

files.json_save('exams_dates', baza.baza_exams(regular(poisk, files.htmlpage())))
