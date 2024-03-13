import telebot
from telebot import types

bot = telebot.TeleBot("6468510348:AAFGtANMxeAp3Ea_NvdawRY6eVohp6wIqXg")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name})', )
    bot.send_message(message.chat.id, 'А теперь немного об Ученическом самоуправлении:')
    bot.send_message(message.chat.id, 'Ученическое Самоуправление – это механизм самоорганизации коллектива школьников, позволяющий школьникам на практике реализовать “Право на участие в управлении образовательной организацией”.Социальная значимость Ученического Самоуправления заключается в воспитании высокоразвитой личности с активной гражданской позицией, готовой к “взрослой жизни”, обладающей общественным опытом и сознанием; демократизации общества.')
    bot.send_message(message.chat.id, 'Чтобы узнать больше об Ученическом Самоуправлении, введите кодовое слово: <b>УСУ</b>.', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт лицея', url='https://sch17himki.edumsko.ru/')
    btn2 = types.InlineKeyboardButton('Цель создания', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Основные признаки', callback_data='edit')
    btn4 = types.InlineKeyboardButton('Функции', callback_data='func')
    btn5 = types.InlineKeyboardButton('Формирование и структура', callback_data='formstructure')
    btn6 = types.InlineKeyboardButton('Способы формирования', callback_data='formway')
    btn7 = types.InlineKeyboardButton('Совет Обучающихся', callback_data='so')
    btn8 = types.InlineKeyboardButton('Роли и должности', callback_data='rangs')
    btn9 = types.InlineKeyboardButton('Рекоммендуемые направления работы (министерства)', callback_data='ministries')
    btn10 = types.InlineKeyboardButton('Организационные направления работы', callback_data='orgways')
    markup.row(btn1)
    markup.row(btn7)
    markup.row(btn2, btn3, btn4)
    markup.row(btn5, btn6, btn8)
    markup.row(btn9, btn10)
    bot.reply_to(message, '<b>Кодовое слово успешно введено</b>', reply_markup=markup, parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.send_message(callback.message.chat.id, '<i>Цель создания Совета Обучающихся</i> – вовлечение обучающихся в управление общеобразовательной организацией; учет мнения обучающихся; и самостоятельное принятие решений и их реализация в интересах ученического коллектива', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 1)
    elif callback.data == 'edit':
        bot.send_message(callback.message.chat.id, '<i>Основные признаки Совета Обучающихся</i>: \n •Совет Обучающихся позволяет обучающимся решать проблемы в общеобразовательной организации силами обучающихся, а также реализовывать дела, которые действительно интересны и полезны для ученического сообщества. \n •Совет Обучающихся как орган Ученического Самоуправления может создаваться только в общеобразовательной организации. \n •Совет Обучающихся работает на основании устава общеобразовательной организации, положения о Совете Обучающихся и плана работы Совета Обучающихся. \n •Руководителем Совета Обучающихся является <u>обучающийся</u>. \n •Специалист, сопровождающий деятельность Совета Обучающихся (советник директора по воспитанию и взаимодействию с детскими общественными объединениями), в работе Совета Обучающихся выступает в роли куратора и координатора деятельности.', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 2)
    elif callback.data == 'func':
        bot.send_message(callback.message.chat.id, '<i>Функции Совета Обучающихся</i>: \n •<u>Представительская</u> – Совет Обучающихся представляет мнение всех обучающихся общеобразовательной организации в органах управления общеобразовательной организацией. \n •<u>Посредническая</u> – Совет Обучающихся взаимодействует с органами управления и самоуправления общеобразовательной организации, помогает в разрешении конфликтов на внутриклассном или общешкольном уровне. \n •<u>Правозащитная</u> – Совет Обучающихся содействует защите гражданских прав учеников внутри общеобразовательной организации. \n •<u>Образовательная</u> – члены Совета Обучающихся передают организационный опыт от старших к младшим через совместную деятельность. \n •<u>Организаторская</u> – Совет Обучающихся поддерживает инициативы обучающихся, помогает в реализации проектов.', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 3)
    elif callback.data == 'formstructure':
        bot.send_message(callback.message.chat.id, '<i>Формирование и структура Совета Обучающихся</i>: Совет обучающихся необходимо формировать ежегодно. Это позволяет соблюдать принципы обновляемости, преемственности, выборности и демократичности.', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 4)
    elif callback.data == 'formway':
        bot.send_message(callback.message.chat.id, '<i>Способы формирования совета обучающихся</i>: \n •<u>Делегирование</u>  - при таком подходе класс выбирает и направляет в совет обучающихся своего делегата, который представляет мнение своего классного коллектива. \n •<u>Общешкольные выборы</u> – такой формат предполагает голосование избирателей на общешкольных выборах за конкретных кандидатов из общего перечня. \n •<u>Инициатива обучающихся</u> – этот способ формирования совета предполагает свободное вступление в совет обучающихся по личному заявлению обучающихся на имя руководителя совета или исполняющего его обязанности. ', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 5)
    elif callback.data == 'so':
        bot.send_message(callback.message.chat.id, '<i>Совет Обучающихся</i> - это постоянный представительный орган <u>Ученического Самоуправления (УСУ)</u>, который выбирается обучающимися общеобразовательной организации с целью решения группы задач, отражающих интересы ученического сообщества.', parse_mode='html')
    elif callback.data == 'rangs':
        bot.send_message(callback.message.chat.id, '<i>Роли и должности Совета Обучающихся</i>: \n •<u>Руководитель Совета Обучающихся</u> \n 1)Проведение заседаний \n 2)Утверждение решений \n 3)Координация и контроль деятельности \n •<u>Секретарь Совета Обучающихся</u> \n 1)Ведение протоколов заседаний, оформление документов \n 2)Помощь руководителю в проведении заседаний \n 3)Ответственность за хранение и распространение документации \n •<u>Руководитель совета по направлению (министр)</u> \n 1)Планирование и организация активистов по своему направлению \n 2)Подготовка и реализация проектов по задачам своего направления \n 3)Представление результатов проделанной работы по направлению \n •<u>Активист Совета Обучающихся</u> \n 1)Выполнение поручений руководителя совета и министра \n 2)Внесение предложений по работе СО и развитию школы \n 3)Принимает участие в реализации проектов СО ', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 6)
    elif callback.data == 'ministries':
        bot.send_message(callback.message.chat.id, '<i>Рекоммендуемые направления работы (министерства) Совета обучающихся</i>: \n •Образование \n •Спорт \n •Информационное \n •Культура и досуг \n •Наставничество \n •Дисциплина и порядок \n •Инфраструктура \n •Аналитика ', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 7)
    elif callback.data == 'orgways':
        bot.send_message(callback.message.chat.id, '<i>Организационные направления работы Совета Обучающихся</i>: \n •Проведение заседаний Совета Обучающихся \n •Разработка и введение правоустанавливающей документации \n •Мониторинг и анализ деятельности совета обучающихся \n •Обучение действующих и потенциальных членов совета обучающихся \n •Унификация деятельности совета обучающихся \n •Социальное партнёрство \n •Поддержка мотивации и инициатив обучающихся', parse_mode='html')
        bot.delete_message(callback.message.chat.id, callback.message.message_id + 8)
bot.infinity_polling()
