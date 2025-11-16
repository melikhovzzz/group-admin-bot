import telebot # telebot library
from TranslatorBot.config import token # token import

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am a chat manager bot.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: # checking that this command was called in response to a message 
        chat_id = message.chat.id # saving chat id
        user_id = message.reply_to_message.from_user.id # saving user id
        # user check
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Unable to ban administrator.")
        else:
            bot.ban_chat_member(chat_id, user_id) # the user with user_id will be banned from the chat with chat_id
            bot.reply_to(message, f"User @{message.reply_to_message.from_user.username} was banned.")
    else:
        bot.reply_to(message, "This command should be used in response to a message from a user you want to ban.")

@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.reply_to_message: # checking that this command was called in response to a message 
        chat_id = message.chat.id # saving chat id
        user_id = message.reply_to_message.from_user.id # saving user id
        #user_status = bot.get_chat_member(chat_id, user_id).status 
        bot.unban_chat_member(chat_id, user_id) # the user with user_id will be unbanned from the chat with chat_id
        bot.reply_to(message, f"User @{message.reply_to_message.from_user.username} was unbanned.")
    else:
        bot.reply_to(message, "This command should be used in response to a message from a user you want to ban.")

@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
bot.infinity_polling(none_stop=True)

