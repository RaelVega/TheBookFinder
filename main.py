import os
import telebot
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
TELEGRAM_TOKEN= os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
genai.configure(api_key=os.environ["GENAI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="Eres un sistema en español  llamado \"The Book Finder\" que ayuda a las personas que te utilizan a encontrar libros especificos o algo que puedan leer, las personas pueden darte nombres de libros, ISBN o describirte el libro que desean buscar o el tipo de lectura que quieren por medio del genero o alguna especificacion del usuario, basicamente eres un asistente que ayuda a fomentar lecura y ayuda a los lectores por medio de inteligencia artificial.  Funcionas siendo un bot de telegram por lo que el texto que generes como respuesta no debe tener NINGUN TIPO DE FORMATO ni asterisco, solo emojis. ",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Hola\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hola! 👋 ¿Qué tipo de libro estás buscando hoy? 🤔📚 \n",
      ],
    },
  ]
)



@bot.message_handler(func=lambda m: True)
def echo_all(message):
    response = chat_session.send_message(message.text)
    respuesta = (response.text)
    #print(chat_session.history)
    bot.reply_to(message, respuesta)
	
bot.infinity_polling()