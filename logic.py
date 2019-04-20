import codecs
import json
import keyboard
import re
import baza
import files

def form_message(message, user, file = 'message_history.json'):
    data  = json.load(codecs.open('json/' + file, 'r', 'utf-8-sig'))
    exams = json.load(codecs.open('json/decoding_exams.json', 'r', 'utf-8-sig'))
    dates = json.load(codecs.open('json/exams_dates.json', 'r', 'utf-8-sig'))

    capital_message = message.capitalize()
    if 'гвэ' in capital_message:
        i = capital_message.find('(гвэ)')
        capital_message = capital_message[:i] + '(ГВЭ)'

    if message == 'привет':
        return["Привет. Чтобы добавить экзамен, просто напиши название предмета (названия всех доступных предметов ты можешь посмотреть, отправив сообщение 'помощь')", keyboard.keyboard([])]

    if message == 'помощь':
        text = 'Список предметов, доступных для отслеживания:\n\n'
        for n in ['Допуск к экзаменам', 'Русский язык', 'Математика', 'Физика', 'Химия', 'Информатика', 'Биология', 'История', 'География', 'Иностранный язык', 'Обществознание', 'Литература', 'ГВЭ']:
            text += n + '\n'
        text += "\nЧтобы перестать следить за экзаменом, просто напиши 'перестать следить'"
        return [text, keyboard.keyboard([])]

    if message == 'перестать следить':
        data[user] = [0, '-']
        files.json_save('json/message_history', data)
        text = 'Выбери предмет:\n\n'
        for n in ['Допуск к экзаменам', 'Русский язык', 'Математика', 'Физика', 'Химия', 'Информатика', 'Биология', 'История', 'География', 'Иностранный язык', 'Обществознание', 'Литература', 'ГВЭ']:
            text += n + '\n'
        return [text, keyboard.keyboard([])]

    if capital_message in exams.keys():
        if user in data:
            if data[user][1] == '-':
                data[user] = [capital_message, '-']
            else:
                data[user] = [capital_message, '+']
        else:
            data[user] = [capital_message, '+']
        files.json_save('json/message_history', data)
        text = 'Выбери дату экзамена:\n\n'
        m = dates[exams[capital_message]]
        for t in m:
            text += t + '\n'
        return [text, keyboard.keyboard(m)]

    if message == 'математика':
        m = ['Математика (базовая)', 'Математика (профильная)']
        text = 'Выбери уровень:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    if message == 'иностранный язык':
        m = ['Английский', 'Немецкий','Французский', 'Испанский', 'Китайский']
        text = 'Выбери язык:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    if message in ['английский', 'немецкий', 'французский', 'испанский', 'китайский']:
        m = [capital_message + ' язык (устно)', capital_message + ' язык (письменно)']
        text = 'Выбери вид:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    if message in ['английский язык', 'немецкий язык', 'французский язык', 'испанский язык', 'китайский язык']:
        m = [capital_message + ' (устно)', capital_message + ' (письменно)']
        text = 'Выбери вид:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    if message == 'гвэ':
        m = ['Русский язык (ГВЭ)', 'Математика (ГВЭ)', 'Информатика (ГВЭ)', 'Обществознание (ГВЭ)']
        text = 'Выбери экзамен:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    if message == 'допуск к экзаменам':
        m = ['Итоговое сочинение', 'Итоговое изложение']
        text = 'Выбери экзамен:\n\n'
        for q in m:
            text += q + '\n'
        return [text, keyboard.keyboard(m)]

    poisk = r'\d\d[.]\d\d[.]\d\d\d\d'
    result = re.findall(poisk, message)
    if result and message == result[0]:
        m = []
        if user in data.keys():
            if data[user][0] == 0:
                text = "Сначала выберите предмет (названия всех доступных предметов ты можешь посмотреть, написав 'помощь')"
            elif message in dates[exams[data[user][0]]]:
                if data[user][1] == '+':
                    p = baza.change('json/students', '+', exams[data[user][0]], message, user)
                    if p == 'Успешно':
                        text = 'Экзамен успешно добавлен'
                    else:
                        text = 'Этот экзамен уже есть в списке твоих экзаменов. Пожалуйста, выбери другой экзамен'
                else:
                    p = baza.change('json/students', '-', exams[data[user][0]], message, user)
                    if p == 'Успешно':
                        text = 'Экзамен успешно удалён'
                    else:
                        text = "Этого экзамена нет в списке твоих экзаменов. Если хочешь, чтобы я перестал следить за каким-то экзаменом, напиши мне 'перестать следить'"
                del data[user]
                files.json_save('json/message_history', data)
            else:
                text = 'В выбранную дату этот экзамен не проходит. Попробуй выбрать другую дату:\n\n'
                m = dates[exams[data[user][0]]]
                for t in m:
                    text += t + '\n'
        else:
            text = "Сначала выберите предмет (названия всех доступных предметов ты можешь посмотреть, написав 'помощь')"
        return [text, keyboard.keyboard(m)]

    else:
        return ['Не понимаю', keyboard.keyboard([])]
