import files

def change(file, i, examen, date, studentid):
    exam = examen + ', ' + date
    a = files.json_load(file)
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
    files.json_save('json/students', a)
    return res

def baza_exams_dates(mas):
    exams = {}
    for k in range(len(mas)):
        if mas[k][0] not in exams.keys():
            exams[mas[k][0]] = [mas[k][1]]
        else:
            exams[mas[k][0]] += [mas[k][1]]
    return exams

def baza_exams(mas):
    exams = {}
    for k in range(len(mas)):
            exams[mas[k][0]] = []
    return exams
