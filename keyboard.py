import json

def get_button(label, color = 'primary'):
    return {
        "action": {
            "type": "text",
            "label": str(label)
        },
        "color": color
    }

def keyboard(mas):
    r = []
    for m in mas:
        r += [[get_button(label = m)]]
    keyboard = {
        "one_time": True,
        "buttons": r
    }
    file = json.dumps(keyboard, ensure_ascii=False)
    return file



