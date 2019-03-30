import re
import files
poisk=r'>(\w*-11.*?\d\d[.]\d\d[.]\d\d\d\d).*?>[0-9]+?<.*?>([0-9]+?)<'
def regular(poisk, text):
    result=re.findall(poisk, text)
    return result
#mas = regular(poisk, files.htmlpage())
#files.vvod('exams3', mas)
def sravnenie(dict1, dict2):
    slovar = {}
    for f in dict1.keys():
        if not dict1[f] == dict2[f]:
            slovar[f] = [dict1[f], dict2[f]]
    return slovar
#sravnenie(jsonfiles.vivod('exams'), jsonfiles.vivod('exams_new'))
def vk_id(examen, file):
    t = files.vivod(file)
    for ex in examen.keys():
        if ex in t.keys():
            for d in t[ex]:
                print(d, ' Экзамен:', ex, ' Было:', examen[ex][0], ' Стало:', examen[ex][1])
                print()
#vk_id(sravnenie(filesout('exams'), filesout('exams_new')), 'students')
def change(file, i, exam, studentid):
    a = files.vivod(file)
    if i == '+':
        if studentid in a[exam]:
            res = "Ошибка"
        else:
            a[exam] += [studentid]
            res = "Успешно"
    if i == '-':
        if studentid in a[exam]:
            a[exam].remove(studentid)
            res = "Успешно"
        else:
            res = "Ошибка"
    files.zapis('students', a)
    return res
#change('students', '-', 'СОЧИН-11, 06.02.2019', '000000')


