import requests
import re
import json
import codecs
def htmlpage():
    s = requests.Session()
    page = s.get('http://res11.rcoi.net/res_exams.aspx').text
    return page
poisk=r'>(\w*-11.*?\d\d[.]\d\d[.]\d\d\d\d).*?>[0-9]+?<.*?>([0-9]+?)<'
def regular(poisk, text):
    result=re.findall(poisk, text)
    return result
mas = regular(poisk, htmlpage())
exams = {}
def jsonfilesin(file, mas):
    for m in range(len(mas)):
        exams[mas[m][0]] = mas[m][1]
    with open(file+ '_json.json', "w") as write_file:
        json.dump(exams, write_file)
def jsonfilesout(file):
    data = json.load(codecs.open(file+'_json.json', 'r', 'utf-8-sig'))
    return data
def sravnenie(dict1, dict2):
    slovar = {}
    for f in dict1.keys():
        if not dict1[f] == dict2[f]:
            slovar[f] = [dict1[f], dict2[f]]
    return slovar
#print(sravnenie(jsonfilesout('exams'), jsonfilesout('exams_new')))
def vk_id(examen, file):
    students = []
    t = jsonfilesout(file)
    for ex in examen.keys():
        if ex in t.keys():
            for d in t[ex]:
                print(d, ' Экзамен:', ex, ' Было:', examen[ex][0], ' Стало:', examen[ex][1])
                print()
vk_id(sravnenie(jsonfilesout('exams'), jsonfilesout('exams_new')), 'students')        
        


