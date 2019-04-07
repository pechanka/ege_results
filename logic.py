import codecs
import json
import keyboard

def zapis(file, k):
    write_file = codecs.open('json/' + file + '.json', 'w', 'utf-8-sig')
    json.dump(k, write_file, ensure_ascii=False)

def form_message(message, user, file = 'message_history.json'):
    data  = json.load(codecs.open('json/' + file, 'r', 'utf-8-sig'))
    exams = json.load(codecs.open('json/decoding_exams.json', 'r', 'utf-8-sig'))
    dates = json.load(codecs.open('json/exams_dates.json', 'r', 'utf-8-sig'))

    if message.capitalize() in exams:
        data[user] = message.capitalize()
        zapis('message_history', data)
        text = 'Выбери дату экзамена:\n'
        m = dates[exams[message.capitalize()]]
        for t in m:
            text += t + '\n'
        return [text, keyboard.keyboard(m)]

    if user in data.keys():
        if message == 'стоп':
            del data[user]
            zapis('message_history', data)
            return ['Запись остановлена. Вы можете добавить новый экзамен.', keyboard.keyboard([])]
        if data[user] not in exams:
            if data[user] == 'Математика':
                if message in ['базовая', 'профильная']:
                    data[user] = data[user] + ' (' + message + ')'
                    zapis('message_history', data)
                    n = dates[exams[data[user]]]
                    return ['Выбери дату экзамена\n', keyboard.keyboard(n)]
                else:
                    return ['Ошибка', keyboard.keyboard([])]
            if data[user] == 'Иностранный язык':
                if message in ['английский', 'немецкий', 'французский', 'испанский', 'китайский']:
                    data[user] = message.capitalize() + ' язык'
                    zapis('message_history', data)
                    m = ['устно', 'письменно']
                    return ['Выберите вид\n', keyboard.keyboard(m)]
                else:
                    return ['Ошибка', keyboard.keyboard([])]
            if data[user] in ['Английский язык', 'Немецкий язык', 'Французский язык', 'Испанский язык', 'Китайский язык']:
                if message == 'устно' or 'письменно':
                    data[user] = data[user] + ' (' + message + ')'
                    zapis('message_history', data)
                    k = dates[exams[data[user]]]
                    return ['Выберите дату экзамена\n', keyboard.keyboard(k)]
                else:
                    return ['Ошибка', keyboard.keyboard([])]
        if message in dates[exams[data[user]]]:
            del data[user]
            zapis('message_history', data)
            return ['Экзамен успешно добавлен', keyboard.keyboard([])]
        else:
            return ['Ошибка', keyboard.keyboard([])]
    else:
        if message == 'математика':
            data[user] = message.capitalize()
            zapis('message_history', data)
            m = ['базовая', 'профильная']
            return ['Выбери уровень\n', keyboard.keyboard(m)]

        if message == 'иностранный язык':
            data[user] = message.capitalize()
            zapis('message_history', data)
            m = ['английский', 'немецкий', 'французский', 'испанский', 'китайский']
            return ['Выбери язык\n', keyboard.keyboard(m)]

        if message in ['английский', 'немецкий', 'французский', 'испанский', 'китайский']:
            data[user] = message.capitalize() + ' язык'
            zapis('message_history', data)
            m = ['устно', 'письменно']
            return ['Выбери вид\n', keyboard.keyboard(m)]

        if message in ['английский язык', 'немецкий язык', 'французский язык', 'испанский язык', 'китайский язык']:
            data[user] = message.capitalize()
            zapis('message_history', data)
            text = 'Выберите вид\n'
            m = ['устно', 'письменно']
            return [text, keyboard.keyboard(m)]

        if message == 'привет':
            return["Привет, друг. Чтобы получить список экзаменов, напиши мне 'список экзаменов'. Чтобы подписаться на рассылку о каком-то экзамене, напиши мне название предмета, а затем выбери дату из предложенных вариантов.", keyboard.keyboard([])]

        if message == 'список экзаменов':
            text = 'Ты можешь выбрать предмет:\n'
            for n in exams:
                text += n + '\n'
            return [text, keyboard.keyboard([])]

        if message == 'помощь':
            return ['Доступные команды', keyboard.keyboard([])]

        else:
            return ['Не понимаю', keyboard.keyboard([])]
