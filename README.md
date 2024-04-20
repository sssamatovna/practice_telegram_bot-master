# Бот для создания списка терминов и определений к ним

Команды /start и /help отправляют пользователю инструкцию к боту

![start_help](https://user-images.githubusercontent.com/55056268/87755469-1d072800-c818-11ea-8138-859d0ae9ff1b.gif)

/new <название списка> - создает новый словарь

![new](https://user-images.githubusercontent.com/55056268/87755504-2abcad80-c818-11ea-9492-69afadae2eda.gif)

/add <название списка>, <термин = определение>, ... - добавляет определения в словарь

![add](https://user-images.githubusercontent.com/55056268/87755511-2db79e00-c818-11ea-9f16-cc9f5e8a9674.gif)

/view и /view <название списка> отправляют пользователю все списки и содержимое указанного списка соответственно

![view](https://user-images.githubusercontent.com/55056268/87755518-314b2500-c818-11ea-86be-9c5cada621e7.gif)

/del <название списка> удаляет указанный список

![del](https://user-images.githubusercontent.com/55056268/87755525-3314e880-c818-11ea-992c-ca95b6408acf.gif)

## Запуск

В config.py нужно указать токен вашего бота

```python
TELEGRAM_API_TOKEN = '<ваш токен>'
```

## В планах

Добавление "тренировок" для запоминания введенных терминов
