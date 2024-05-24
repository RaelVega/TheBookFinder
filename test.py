import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot("6950817217:AAGepJmJQfktaVToQcUS-HkF7qOQoX96xgg") 


#/start & /help
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message, 
        f"""¡Hola {message.from_user.first_name}✨ 
        \n Bienvenido a TheBookFinder! 🕵️‍♂️📚
        \n Soy tu asistente personal para encontrar libros.
        \n¿Necesitas encontrar algún libro en específico o buscas recomendaciones de lecturas? 
        \n¡Estás en el lugar correcto!
        \n Comandos disponibles:
        \n /search - Busca un libro en especifico 🔍
        \n /suggestion - Busca alguna recomendación de lectura  🧐🤓""",
    )


#/search
@bot.message_handler(commands=["search"])
def search(message):
    board = ReplyKeyboardMarkup(
        row_width=2, resize_keyboard=True, one_time_keyboard=True
    )
    board.add(KeyboardButton("Buscar por nombre"), KeyboardButton("Buscar por ISBN"), KeyboardButton("Buscar por Descripción"))
    bot.send_message(message.chat.id, "Elige el tipo de busqueda que deseas realizar para tu libro!", reply_markup=board)
    bot.register_next_step_handler(message, handle_search_choice)


def handle_search_choice(message):
    # Comprobar la elección 
    if message.text.lower() == "buscar por nombre":
        bot.send_message(
            message.chat.id, "Dime el nombre del libro que deseas buscar"
        )
        bot.register_next_step_handler(message, name_search)
    elif message.text.lower() == "buscar por isbn":
        bot.send_message(
            message.chat.id, "Escribe el ISBN del libro que deseas buscar"
        )
        bot.register_next_step_handler(message, isbn_search)
    elif message.text.lower() == "buscar por descripción":
        bot.send_message(
            message.chat.id, "Dime una descripción del libro que deseas buscar"
        )
        bot.register_next_step_handler(message, desc_search)


def name_search(message):
    bot.reply_to(message, f"En proceso...")

def isbn_search(message):
    bot.reply_to(message, f"En proceso...")

def desc_search(message):
    bot.reply_to(message, f"En proceso...")

#/suggestion
@bot.message_handler(commands=["suggestion"])
def suggestion(message):
    bot.reply_to(
        message, "Parece ser que quieres una recomendación de algo interesante para leer, Dime qué buscas y haré todo lo posible para ayudarte. ",
    )

# Respuesta mensajes por default
@bot.message_handler(content_types=["text"])
def hola(message):
    if message.text.lower() in ["hola", "hello", "hi"]:
        bot.send_message(
            message.chat.id,
            f"Hola {message.from_user.first_name}, escribe '/start' para comenzar",
        )
    else:
        bot.send_message(
            message.chat.id,
            "Comando no encontrado. Por favor, usa /start para empezar",
        )

#Recibir mensajes 
#bot.infinity_polling()
bot.polling()

"""
response = chat_session.send_message("Hola, como te llamas?")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(response.text)
    print(chat_session.history)
	#bot.reply_to(message, message.text)
	
bot.infinity_polling()
"""

