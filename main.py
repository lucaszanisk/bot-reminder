import telebot

CHAVE_API = '5302146321:AAG8Ae-EduMXCN_XYNtUJCkqIerubjcCmh8'

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["adicionar"])
def adicionar(mensagem):
    texto = """
    O que você deseja adicioanr? (Clique em uma opção)
    /pessoa Pessoa
    /task Task"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["deletar"])
def deletar(mensagem):
    texto = """ O que você deseja deletar?
    /pessoa Pessoa
    /task Task"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["listar"])
def listar(mensagem):
    bot.send_message(mensagem.chat.id, "Listando todas as tasks")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /adicionar Para adicionar 
     /deletar Para deletar
     /listar Para mostrar todas as tasks"""
    bot.reply_to(mensagem, texto)


bot.polling()
