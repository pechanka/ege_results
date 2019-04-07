import vk_api
import random

def send(message, uservk, token, keyboard):
    vk = vk_api.VkApi(token = token)
    rand = random.randint(1, 2147483600)
    par = {
        'user_id':uservk,
        'random_id':str(rand),
        'message': message,
        'keyboard': keyboard
        }
    vk.method('messages.send', par)