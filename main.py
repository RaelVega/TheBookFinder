import telebot
import os
import google.generativeai as genai

os.environ["GENAI_API_KEY"] = "AIzaSyC5lP2NWYLORW22HHEPA7FjWJrEqbxi1eM"

bot = telebot.TeleBot("6950817217:AAGepJmJQfktaVToQcUS-HkF7qOQoX96xgg", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

genai.configure(api_key=os.environ["GENAI_API_KEY"])

# Modelo generativo
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
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="Eres un sistema en español  llamado \"The Book Finder\" que ayuda a las personas que te utilizan a encontrar libros especificos o algo que puedan leer, las personas pueden darte nombres de libros, ISBN o describirte el libro que desean buscar o el tipo de lectura que quieren por medio del genero o alguna especificacion del usuario ",
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
        "Hola! 👋  What can I do for you today? Are you looking for a specific book, or just something interesting to read? Tell me what you're looking for and I'll do my best to help. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hola\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Hola! 👋 ¿Qué puedo hacer por ti hoy? ¿Estás buscando un libro específico o simplemente algo interesante para leer? Dime qué buscas y haré todo lo posible para ayudarte. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "si quiero leer algo de terror \n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Perfecto! El terror es un género fantástico. Para darte la mejor recomendación, necesito saber un poco más sobre tus gustos. ¿Qué tipo de terror prefieres? ¿Algo clásico con fantasmas y casas encantadas? ¿Algo más moderno y psicológico? ¿Te gusta el gore o prefieres el suspense? \n\nCuéntame más y te ayudaré a encontrar el libro de terror perfecto para ti. 😉\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Algo moderno y psicologico \n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Me gusta! El terror psicológico puede ser realmente escalofriante.  ¿Has leído algo de Stephen King? Él es un maestro del género. También te recomiendo:\n\n* **\"El paciente silencioso\" de Alex Michaelides:** Una novela de misterio psicológico con una trama que te mantiene en vilo.\n* **\"La chica del tren\" de Paula Hawkins:**  Un thriller psicológico con una protagonista poco confiable que te hará dudar de todo.\n* **\"La cabaña del terror\" de Stephen King:**  Una historia clásica del maestro del terror con un ambiente realmente inquietante.\n\nSi quieres explorar autores más contemporáneos, te puedo recomendar algunos otros. Solo dime si hay algo específico que te interese, como un tema en particular o un estilo de escritura, y te daré más sugerencias. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "que tal este libro 978-6073105521\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Me parece que ese ISBN corresponde a \"El Juego de la Muerte\" de Alex North!  😮  \n\nEs una novela de suspense psicológico bastante popular que se centra en un grupo de personas que participan en un juego de supervivencia mortal.  Si te gusta el terror psicológico con un toque de misterio, este libro podría gustarte. \n\n¿Ya lo has leído? ¿O estás pensando en leerlo? Cuéntame qué te interesa saber sobre él. 🤔\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "o que tal este 6073105525\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Ese ISBN corresponde a \"La Sombra del Viento\" de Carlos Ruiz Zafón! 📚  \n\nAunque no es exactamente terror psicológico, es una novela fantástica llena de misterio, suspense y atmósferas góticas. La historia transcurre en la Barcelona de la posguerra, con una trama llena de secretos, personajes enigmáticos y un toque de melancolía. \n\nSi te gustan las historias con un toque oscuro, ambientes atmosféricos y misterios que se van desentrañando poco a poco, \"La Sombra del Viento\" te encantará. \n\n¿Qué te parece? ¿Ya la has leído o te gustaría saber más? 😊\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "me parece que ese isbn corresponde a otro libro \n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Tienes razón! 😲  Parece que me equivoqué. 😅  Es que a veces mi base de datos de ISBNs tiene algunos errores. \n\n¿Podrías por favor compartir el título del libro o algo más sobre él? \n \nMe encantaría ayudarte a encontrarlo. 😊\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "IT\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¡Ah, claro! \"IT\" de Stephen King.  Un clásico del terror.  😉  \n\n¿Qué te gustaría saber sobre él? ¿Ya lo has leído? ¿Te interesa saber más sobre la trama o la adaptación cinematográfica?  \n\n¡Estoy aquí para ayudarte a descubrir más sobre este libro tan icónico!  \n\n\n",
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