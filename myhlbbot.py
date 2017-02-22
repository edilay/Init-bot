import telebot

TOKEN = '256401745:AAF0saxCynIWv_u8M2N9Udeu84mVX8Ms3cM'


bot = telebot.TeleBot(TOKEN)


User = bot.get_me()

#si comando start o help
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Este Bot es supervisado satelitalmente por Cthulhu.:= ")
    #bot.reply_to(message,message.text)
    bot.reply_to(message,message.chat.type)
    cid = message.chat.id  # Guardamos el ID de la conversacion para poder responder.

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "there is no help in hell.")
    #cid = message.chat.id  # Guardamos el ID de la conversacion para poder responder.

#
#Si tipo de mensaje documento audio
@bot.message_handler(content_types=[ 'audio'])
def handle_audio(message):
    bot.reply_to(message, "Lo siento ahora no puedo hablar")

#comando ingress
@bot.message_handler(commands=['ingress'])
def ingress_message(message):
    bot.reply_to(message, "Ingress es un juego muy cool JOIN THE RESISTANCE.R&R. ")
    bot.reply_to(message,message.from_user.first_name+" AKA:"+message.from_user.username+'->'+message.text );

#ERes nuevo... so wellcome to the party
@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return

    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)

    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)

    bot.reply_to(message, text_messages['Bienvenido a este desolado lugar: '].format(name=name))

############################################################################################




#ping
@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Quieres un poco del ping de la muerte pequenio demonio?")




#si cualquier mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,message.text)


bot.polling()
