import json
import codecs
import requests
def zapis(file, k):
    with open(file+ '_json.json', "w") as write_file:
        json.dump(k, write_file)
def vvod(file, mas):
    exams = {}
    for m in range(len(mas)):
        exams[mas[m][0]] = mas[m][1]
    zapis(file, exams)
def vivod(file):
    data = json.load(codecs.open(file+'_json.json', 'r', 'utf-8-sig'))
    return data
def htmlpage(n = 'internet'):
    page = ''
    if n == 'internet':
        s = requests.Session()
        page = s.get('http://res11.rcoi.net/res_exams.aspx').text
    else:
        inf = codecs.open(n, 'r', 'utf-8-sig')
        for line in inf:
            page += line.strip()
    return page
