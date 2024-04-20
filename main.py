import config
import listedit
import listview
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start_info(update, context):
    str = ''
    if update.message.text == '/start':
        str += f'Привет, {update.message.from_user.username} 👨‍💻\n' + \
               'Я помогу тебе с запоминанием информации ♾\n\n\n'
    str += 'Ты можешь создать новый список - /new <название списка> 🤬\n\n' + \
           'И добавить в него новый термин или понятие вместе с определением - ' + \
           '/add <название списка>, <термин = определение>, ... (можно добавлять несколько пар за раз) 🐈\n\n' + \
           'Команда /view покажет тебе все созданные тобой списки ✏\n\n' + \
           'А написав /view <название списка>, ты увидишь, что находится в выбранном списке 👁\n\n' + \
           '/del <название списка> удалит выбранный список 🗑\n\n' + \
           '/help для просмотра всех комманд 🖱'

    update.message.reply_text(str)

def new(update, context):
    if update.message.text == '/new':
        update.message.reply_text('Вы не ввели название списка 🙀')
    elif listedit.new_list(update.message.from_user.id, update.message.text):
        update.message.reply_text('Новый список успешно создан 👌')
    else:
        update.message.reply_text('Такой список уже создан 🛑\n')

def delete(update, context):
    if listedit.del_list(update.message.from_user.id, update.message.text):
        update.message.reply_text('Список успешно удален 🗑\n')
    else:
        update.message.reply_text('Проверьте введенные данные 🛑\n')

def add(update, context):
    if listedit.add_to_list(update.message.from_user.id, update.message.text):
        update.message.reply_text('Новые термины успешно добавлены 👌')
    else:
        update.message.reply_text('Проверьте введенные данные 🛑\n' + 'Вы не создавали такого списка или неверно ввели понятия 🙊')

def view(update, context):
        update.message.reply_text(listview.view_list(update.message.from_user.id, update.message.text))

def text_message(update, context):
    update.message.reply_text('Не знаю, как вам ответить 😿')

def main():
    '''start the bot'''
    updater = Updater(config.TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # commands
    dp.add_handler(CommandHandler('start', start_info))
    dp.add_handler(CommandHandler('help', start_info))

    dp.add_handler(CommandHandler('new', new))
    dp.add_handler(CommandHandler('del', delete))
    dp.add_handler(CommandHandler('add', add))
    dp.add_handler(CommandHandler('view', view))

    # messages
    dp.add_handler(MessageHandler(Filters.text, text_message))

    # start
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()