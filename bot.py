import telebot
import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
       
    
bot = telebot.TeleBot("7855280820:AAEPDO74yi-paooy8b7NKQpjlU--SczXOVA")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['psw'])
def send_bye(message):
        bot.reply_to(message,gen_pass(8))   
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()