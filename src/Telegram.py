from src.Fanpage import fanpage_main
from src.Focus import focus_main
from src.LaRepubblica import larepubblica_main
from src.PuntoInformatico import puntoinformatico_main
from src.TomsHardware import tomshw_main
from src.Wired import wired_main
import configparser
import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, updater
from telegram import Bot, Poll, PollOption


def salve(update, context):
    user_username = update.message.from_user.username
    text = "Ciao, cosa succede nel mondo oggi?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def news(update, context, news):
    text = news
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def deliver_urls(news, token, id_dest):
    bot = telegram.Bot(token)
    bot = telegram.Bot(token=token)
    for n in news:
        bot.sendMessage(chat_id= id_dest, text = n)


def main():
    config = configparser.ConfigParser()
    config.read('config/config.cfg')
    token = config['Telegram']['Token']
    id_dest = config['Telegram']['Id_Destinatari']
    larepubblica = larepubblica_main()
    focus = focus_main()
    wired = wired_main()
    tomshw = tomshw_main()
    puntoinformatico = puntoinformatico_main()
    fanpage = fanpage_main()
    urls = []
    row = 0
    tot_n_articles = len(larepubblica) + len(focus) + len(wired) + len(tomshw) + len(puntoinformatico)
    if tot_n_articles < 5:
        treshold_articles = tot_n_articles
    else:
        treshold_articles = 6

    while len(urls) < treshold_articles:
        try:
            urls.append(larepubblica[row][0])
        except:
            pass
        try:
            urls.append(focus[row][0])
        except:
            pass
        try:
            urls.append(wired[row][0])
        except:
            pass
        try:
            urls.append(tomshw[row][0])
        except:
            pass
        try:
            urls.append(puntoinformatico[row][0])
        except:
            pass
        try:
            urls.append(fanpage[row][0])
        except:
            pass
        row += 1
    print(urls)
    deliver_urls(urls, token, id_dest)



if __name__ == "__main__":
    main()
