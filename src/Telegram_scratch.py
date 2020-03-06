
                                                                                                                             
                                                                                                                             
#     EEEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDDDD       UUUUUUUU     UUUUUUUUBBBBBBBBBBBBBBBBB        OOOOOOOOO     TTTTTTTTTTTTTTTTTTTTTTT
#     E::::::::::::::::::::ED::::::::::::DDD    U::::::U     U::::::UB::::::::::::::::B     OO:::::::::OO   T:::::::::::::::::::::T
#     E::::::::::::::::::::ED:::::::::::::::DD  U::::::U     U::::::UB::::::BBBBBB:::::B  OO:::::::::::::OO T:::::::::::::::::::::T
#     EE::::::EEEEEEEEE::::EDDD:::::DDDDD:::::D UU:::::U     U:::::UUBB:::::B     B:::::BO:::::::OOO:::::::OT:::::TT:::::::TT:::::T
#       E:::::E       EEEEEE  D:::::D    D:::::D U:::::U     U:::::U   B::::B     B:::::BO::::::O   O::::::OTTTTTT  T:::::T  TTTTTT
#       E:::::E               D:::::D     D:::::DU:::::D     D:::::U   B::::B     B:::::BO:::::O     O:::::O        T:::::T        
#       E::::::EEEEEEEEEE     D:::::D     D:::::DU:::::D     D:::::U   B::::BBBBBB:::::B O:::::O     O:::::O        T:::::T        
#       E:::::::::::::::E     D:::::D     D:::::DU:::::D     D:::::U   B:::::::::::::BB  O:::::O     O:::::O        T:::::T        
#       E:::::::::::::::E     D:::::D     D:::::DU:::::D     D:::::U   B::::BBBBBB:::::B O:::::O     O:::::O        T:::::T        
#       E::::::EEEEEEEEEE     D:::::D     D:::::DU:::::D     D:::::U   B::::B     B:::::BO:::::O     O:::::O        T:::::T        
#       E:::::E               D:::::D     D:::::DU:::::D     D:::::U   B::::B     B:::::BO:::::O     O:::::O        T:::::T        
#       E:::::E       EEEEEE  D:::::D    D:::::D U::::::U   U::::::U   B::::B     B:::::BO::::::O   O::::::O        T:::::T        
#     EE::::::EEEEEEEE:::::EDDD:::::DDDDD:::::D  U:::::::UUU:::::::U BB:::::BBBBBB::::::BO:::::::OOO:::::::O      TT:::::::TT      
#     E::::::::::::::::::::ED:::::::::::::::DD    UU:::::::::::::UU  B:::::::::::::::::B  OO:::::::::::::OO       T:::::::::T      
#     E::::::::::::::::::::ED::::::::::::DDD        UU:::::::::UU    B::::::::::::::::B     OO:::::::::OO         T:::::::::T      
#     EEEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDDDD             UUUUUUUUU      BBBBBBBBBBBBBBBBB        OOOOOOOOO           TTTTTTTTTTT      
                                                                                                                             
                                                                                                                             
                                                                                                                             
#Various imports
import threading
import logging
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
from telegram import Bot, Poll, PollOption

#Log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#EduBot answers to /hi
def hi(update, context):
    user_username = update.message.from_user.username
    text = "Hi " + user_username + ", I'm EduBot!"
    context.bot.send_message(chat_id=update.effective_chat.id, text = text)


#Edubot shuts down /r
def stop_bot():
    updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def shutdown(update, context):
    update.message.reply_text('Bot is shutting down...')
    stop_bot()
    

#EduBot echoes the message received
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


#NOT WORKING
#EduBot sends the user a poll /poll
def poll(update, context):
    bot = Bot('917804964:AAEQ4Vt5-A0h6DYQG0wYnd8zBGFn7m9PTJQ', base_url=None, base_file_url=None, request=None, private_key=None, private_key_password=None)
    risposte_poll = [PollOption('si', 1), PollOption('no', 2)]
    question = 'Vuoi una mela?'
    update.message.poll('test',question, risposte_poll)
    #poll_test = Poll(id = 'test', question = 'Vuoi una mela?', options = risposte_poll, is_closed = False)

if __name__ = "__main__":
    token = '917804964:AAEQ4Vt5-A0h6DYQG0wYnd8zBGFn7m9PTJQ'
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    #Handlers
    start_handler = CommandHandler('hi', hi)
    echo_handler = MessageHandler(Filters.text, echo)
    poll_handler = CommandHandler('poll', poll)
    stop_handler = CommandHandler('r', shutdown, filters=Filters.user(username='@Pellawoof'))

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(poll_handler)
    dispatcher.add_handler(stop_handler)

    updater.start_polling()
    updater.idle()
