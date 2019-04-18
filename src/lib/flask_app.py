from flask import Flask, request, json
from settings import confirmation_token, token
import vkapi
import logic

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        user_id = data['object']['user_id']
        message = data['object']['body'].lower()
        z = logic.form_message(message, str(user_id))[0]
        y = logic.form_message(message, str(user_id))[1]
        vkapi.send(z, str(user_id), token, keyboard = y)
        return 'ok'
