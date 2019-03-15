from bot import*
import logging

#=====================Main=========================#
def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=.5)

if __name__ == '__main__':
    main(True, 'INFO')
#==================================================#