from variables import*
import telebot

bot = telebot.TeleBot(TOKEN)

#==================================================#
# to get id for group chat!
#print(bot.get_updates()[0].message.chat.id)
#==================================================#

#==================Commands========================#
@bot.message_handler(commands = ['start'])
def start_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, start_msg)
    else:
        bot.send_message(CHAT_GROUP, start_msg)

@bot.message_handler(commands = ['help'])
def help_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, help_msg)
    else:
        bot.send_message(CHAT_GROUP, help_msg)

@bot.message_handler(commands = ['about'])
def help_handler(message):
    if  message.chat.id == int(CHAT_BOT):
        bot.send_message(message.from_user.id, about_msg)
    else:
        bot.send_message(CHAT_GROUP, about_msg)
#==================================================#

#===========Non command message handler============#
#resend messages from users to current chat
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    try:
        if message.chat.id == int(CHAT_BOT):
            bot.send_message(message.from_user.id, message.text)
        else:
            bot.send_message(CHAT_GROUP, "i do not know this command i will send your request to group master, he will answer you soon!")
            bot.forward_message(CHAT_BOT, message.chat.id, message.message_id)
            bot.send_message(CHAT_BOT,str('@'+ message.from_user.username))

        #DEBUG
        #print("DEBUG: Message.chat.id = " + str(message.chat.id))
        #print("DEBUG: message.from_user.id = " + str(message.from_user.id))

    except Exception as error:
        print("Exception in \"message_handler\". info: " + str(error))
#==================================================#