from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("7062651138:AAE47fpsRxZvbq6M1iVl6L8ZJ36BEslShQ0", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def send_welcome(message):
  javob = '**Assalomu alaykum , Xush kelibsiz!**'
  javob += '\nLotin ga yoki Kirl ga o\'tqizmoqchi bo\'lgan matinni yuborishingiz mumkin.'
  bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  matn = message.text
  if matn.isascii():
    matn = to_cyrillic(matn)
  else:
    matn = to_latin(matn)
  bot.reply_to(message, matn)

bot.polling()


