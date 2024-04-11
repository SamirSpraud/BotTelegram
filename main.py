import telebot
from telebot import types
#conectar con el bot
TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)

#Implementacion de comandos '/start' y 'help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    btn_menu = types.InlineKeyboardButton('Menu principal', callback_data='menuPrin')
    markup2.add(btn_menu)
    bot.reply_to(message, 'Hola, soy tu Asistente Virtual del ITLA. ¡Bienvenido al Instituto Tecnológico de las Américas (ITLA)! Somos una institución líder en educación tecnológica en la República Dominicana. Estoy aquí para ayudarte en lo que necesites.',reply_markup=markup2)
    
# @bot.callback_query_handler(func=lambda call:True)
# def callback_query(call):
#     if call.data == 'menuPrin':
#         bot.send_message(call.message.chat.id, 'Elegiste la opción 1')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'menuPrin':
        markup_menu_principal = types.InlineKeyboardMarkup(row_width=1)
        btn_informacion_general = types.InlineKeyboardButton('Información General', callback_data='info_general')
        btn_carreras_tecnologicas = types.InlineKeyboardButton('Carreras Tecnológicas', callback_data='carreras_tecnologicas')
        btn_transporte = types.InlineKeyboardButton('Transporte', callback_data='transporte')
        btn_registro = types.InlineKeyboardButton('Registro', callback_data='registro')
        btn_admisiones = types.InlineKeyboardButton('Admisiones', callback_data='admisiones')
        btn_preguntas_frecuentes = types.InlineKeyboardButton('Preguntas Frecuentes', callback_data='preguntas_frecuentes')
        
        markup_menu_principal.add(btn_informacion_general, btn_carreras_tecnologicas, btn_transporte, btn_registro, btn_admisiones, btn_preguntas_frecuentes)
        

        bot.send_message(call.message.chat.id, 'Selecciona una opción:', reply_markup=markup_menu_principal)

    elif call.data == 'info_general':
        markup_volver_atras = types.InlineKeyboardMarkup(row_width=1)
        btn_volver_atras = types.InlineKeyboardButton('Volver atrás', callback_data='menuPrin')
        markup_volver_atras.add(btn_volver_atras)
       
        bot.send_message(call.message.chat.id, '📌 Información General:\nUbicación: https://maps.app.goo.gl/4bQt2qDU7iNxxAaH8\nTeléfonos: 809-738-4852 / 809-793-2557\nCorreo Electrónico: info@itla.edu.do', reply_markup=markup_volver_atras)

    elif call.data == 'carreras_tecnologicas':
        mensaje_carreras = "Carreras Tecnológicas:\n"
        mensaje_carreras += "1. Simulaciones Interactivas y Videojuegos\n"
        mensaje_carreras += "2. Telecomunicaciones\n"
        mensaje_carreras += "3. Inteligencia Artificial\n"
        mensaje_carreras += "4. Informática Forense\n"
        mensaje_carreras += "5. Energía Renovable\n"
        mensaje_carreras += "6. Redes de Información\n"
        mensaje_carreras += "7. Mecatrónica\n"
        mensaje_carreras += "8. Manufactura Automatizada\n"
        mensaje_carreras += "9. Manufactura de Dispositivos Médicos\n"
        mensaje_carreras += "10. Diseño Industrial\n"
        mensaje_carreras += "11. Multimedia\n"
        mensaje_carreras += "12. Sonido\n"
        mensaje_carreras += "13. Desarrollo de Software\n"
        mensaje_carreras += "14. Analítica y Ciencia de Datos\n"
        mensaje_carreras += "15. Seguridad Informática\n"
    
        markup_volver_atras = types.InlineKeyboardMarkup(row_width=1)
        btn_volver_atras = types.InlineKeyboardButton('Volver atrás', callback_data='menuPrin')
        markup_volver_atras.add(btn_volver_atras)
    
        bot.send_message(call.message.chat.id, mensaje_carreras, reply_markup=markup_volver_atras)

    elif call.data == 'transporte':
        mensaje_transporte = "Transporte:\n"
        mensaje_transporte += "Consulta nuestro horario y mapa de ubicación para facilitar tu llegada al campus:\n"
        mensaje_transporte += "https://www.google.com/maps/d/u/2/viewer?mid=10bNTYESub5N0jc6x7kYPiUkrKL2ypCA&ll=18.497541480313174%2C-69.82063475000001&z=12"
    
        markup_volver_atras = types.InlineKeyboardMarkup(row_width=1)
        btn_volver_atras = types.InlineKeyboardButton('Volver atrás', callback_data='menuPrin')
        markup_volver_atras.add(btn_volver_atras)

        bot.send_message(call.message.chat.id, mensaje_transporte, reply_markup=markup_volver_atras)
 




















@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Usa /start para ir al inicio')

@bot.message_handler(commands=['hola'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    #Creacion de botones
    btn_opt01 = types.InlineKeyboardButton('Opcion1', callback_data='hola_Opcion1')
    btn_opt02 = types.InlineKeyboardButton('Opcion2', callback_data='hola_Opcion2')

    #Add botones
    markup.add(btn_opt01,btn_opt02)

    #Enviar los mensajes
    bot.send_message(message.chat.id, "Elige una opcion", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'hola_Opcion1':
        # bot.answer_callback_query(call.id,'Elegiste la opcion 1')
        bot.send_message(call.message.chat.id, 'Elegiste la opción 1')
    elif call.data == 'hola_Opcion2':
        # bot.answer_callback_query(call.id,'Elegiste la opcion 2')
        bot.send_message(call.message.chat.id, 'Elegiste la opción 2')


@bot.message_handler(commands=['foto'])
def send_image(message):
    img='https://static.wikia.nocookie.net/zelda/images/e/e1/Link_Artwork_2_%28The_Minish_Cap%29.png/revision/latest?cb=20120124213342&path-prefix=es'
    bot.send_photo(chat_id=message.chat.id, photo=img, caption="Link de The  minish Cap")


if __name__ == "__main__":
    bot.polling(none_stop=True)