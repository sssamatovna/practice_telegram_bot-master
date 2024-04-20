import json

def new_list(user_id, text):
    list_name = text[text.find(' ') + 1:]
    data = {list_name : {}}

    if _write_new_list(user_id, data):
        return True
    else:
        return False

def _write_new_list(user_id, dict):
    flag = True
    try:
        data = json.load(open(f'{user_id}.json', encoding='UTF-8'))
        for i in data:
            for j in i:
                if j in dict:
                    flag = False
    except:
        data = []

    if flag:
        data.append(dict)

        with open(f'{user_id}.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    return flag

def del_list(user_id, text):
    list_name = text[text.find(' ') + 1:]

    if _delete_list(user_id, list_name):
        return True
    else:
        return False

def _delete_list(user_id, list_name):
    data = json.load(open(f'{user_id}.json', encoding='UTF-8'))
    flag = False
    for i in data:
        for j in i:
            if j == list_name:
                data.remove(i)

                with open(f'{user_id}.json', 'w', encoding='UTF-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)
                flag = True
    return flag

def add_to_list(user_id, text):
    list_name = text[text.find(' ') + 1:text.find(',') + 1 - 1]
    terms = text[text.find(',') + 2:].split(', ')

    terms_dict = {}
    for i in terms:
        terms_dict[i.split(' = ')[0]] = i.split(' = ')[1]

    flag = False
    if _write_new_term(user_id, list_name, **terms_dict):
        flag = True
    return flag

def _write_new_term(user_id, list_name, **terms):
    data = json.load(open(f'{user_id}.json', encoding='UTF-8'))

    flag = False
    for i in data:
        for j in i:
            if j == list_name:
                for key, value in terms.items():
                    i[j].update({key:value})

                with open(f'{user_id}.json', 'w', encoding='UTF-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)
                flag = True
    return flag

