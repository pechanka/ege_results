import re
import files
import vkapi
import keyboard
from settings import token

poisk=r'>(\w*-11.*?\d\d[.]\d\d[.]\d\d\d\d).*?>[0-9]+?<.*?>([0-9]+?)<'

def regular(poisk, text):
    result=re.findall(poisk, text)
    return result

def sravnenie(dict1, dict2):
    slovar = {}
    for f in dict1.keys():
        if not dict1[f] == dict2[f]:
            slovar[f] = [dict1[f], dict2[f]]
    return slovar

def keys_values(mas, value):
    for m in mas.keys():
        if mas[m] == value:
            return m

def vk_id(dictionary, students_file):
    students = files.json_load(students_file)
    decoding = files.json_load('json/decoding_exams')
    for i in dictionary.keys():
        k = regular(r'\w*-11', i)
        date = regular(r'\d\d[.]\d\d[.]\d\d\d\d', i)
        text = "Привет! Обновились результаты экзамена " + keys_values(decoding, k[0]) + ". Ты можешь посмотреть их на сайте РЦОИ: res11.rcoi.net. \n\n Если ты узнал свой результат, ты можешь отписаться от этого экзамена, написав мне 'перестать следить' и выбрав соответствующий экзамен. Если результатов экзамена не видно в личном кабинете, возможно, они появятся чуть позже. Я сообщу тебе, как только узнаю об изменениях."
        for s in students[i]:
            vkapi.send(text, s, token, keyboard.keyboard([]))

