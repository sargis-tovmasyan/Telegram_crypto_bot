from variables import*
import logging
import telebot
import cryptocompare
import json

bot = telebot.TeleBot(TOKEN)

strJsonBTC = str(cryptocompare.get_price('BTC',curr='USD')).replace("\'","\"")
jsonData = json.loads(strJsonBTC)

#==================Commands========================#
@bot.message_handler(commands = ['start'])
def start_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, start_msg)

@bot.message_handler(commands = ['help'])
def help_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, help_msg)

@bot.message_handler(commands = ['about'])
def help_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, about_msg)

#==================================================#
@bot.message_handler(commands = ['btc'])
def start_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, "1BTC = " + str(jsonData['BTC']['USD']) + " $")
#==================================================#

#resend messages from users to current chat
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    try:
        if message.chat.id == int(CHAT_BOT):
            bot.send_message(CHAT_BOT, "Wrong command!")
            #bot.send_message(message.from_user.id, message.text)
            print(success_msg)
        #DEBUG
        print("DEBUG: Message sends to chat:" + message.chat.id)
    except Exception as error:
        print("Exception in \"message_handler\". info: " + str(error))
#==================================================#
