import telebot
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API = os.getenv('API_PASSWORD')

bot = telebot.TeleBot(CHAVE_API)

rooms = []
people = []


@bot.message_handler(commands=['help'])
def help(message):
    texto = """O fridayReminder é um bot onde você consegue adicionar tasks e pessoas à essas tasks e toda sexta-feira todos os envolvidos serão notificados do que deve ser feito naquela semana.
    /add_user Para adicionar usuário
    """
    bot.reply_to(message, texto)


@bot.message_handler(commands=['add_user'])
def add_user(message):
    bot.reply_to(message, f'{message.text} pessoa adicionada com sucesso!')


@bot.message_handler(commands=['add_task'])
def add_task(message):

    bot.reply_to(message, f'{message.text} Task adicionada com sucesso!')


def verificar(message):
    return True


@bot.message_handler(func=verificar)
def responder(message):
    texto = """
    Seja bem-vindo ao fridayremider_bot,
    para prosseguir, clique em uma das opções:
     /help Para saber mais sobre o bot"""
    bot.reply_to(message, texto)


bot.infinity_polling()
