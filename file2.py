import telebot

bot = telebot.TeleBot("6174675822:AAG4WSvZdKl5wWy5SeyL7YXPCGnJWpIjDBQ")

#------קבלת מידע ממשתמש -----
@bot.message_handler(commands=['start', 'hello'])
    #לכאן תתקבל ההודעה
def start(message):
    mess = f'Привет!! {message.from_user.first_name} {message.from_user.last_name}, бляяяя, как ваше нечего??'
    #chat.id -אומר לשלוח הודעה לאותה השיחה\צ'אט
    bot.send_message(message.chat.id, mess)

@bot.message_handler()
def get_user_text(message):
    if message.text == ("Hello").lower():
        bot.send_message(message.chat.id, f"Hello братан!!")
    elif message.text == ("Id").lower():
        bot.send_message(message.chat.id, f"Hello братан!! your ID: ", {message.from_user.id})
    else:
        bot.send_message(message.chat.id, f"Hello братан!! your ID: ", {message.from_user.id})


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

#עשה שהבוט יעבוד כל הזמן בלי הפסקה
bot.polling(none_stop=True)

