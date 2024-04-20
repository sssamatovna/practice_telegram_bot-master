import json


def view_list(user_id, message_text):
    data = json.load(open(f'{user_id}.json', encoding='UTF-8'))

    if len(message_text) == 5:
        str = 'Ваши списки ✏\n'
        for i in data:
            for j in i:
                str += '    ' + j + '\n'
    else:
        list_name = message_text[message_text.find(' ') + 1:]
        str = f'{list_name} 📃\n'
        for i in data:
            for j in i:
                if j == list_name:
                    for key, value in i[j].items():
                        str += '    ' + key + ' = ' + value + '\n'
    return str
