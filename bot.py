import os
import telebot
from gtts import gTTS

CHAVE_DO_BOT = "8778955103:AAE7IL0rE1bWNcHKxMv2Xu5QZIXXSwyTeYQ"
bot = telebot.TeleBot(CHAVE_DO_BOT)

@bot.message_handler(commands=['start', 'help'])
def enviar_mensagem_inicial(mensagem):
    bot.reply_to(mensagem, "Olá Me chamou? Eu sou um bot que converte texto em voz. Envie-me uma mensagem e eu responderei com um áudio!")

@bot.message_handler(func=lambda mensagem: True)
def responder_em_voz(mensagem):
    texto_usuario = mensagem.text
    nome_arquivo = f"voz_{mensagem.chat.id}.mp3"
    
    try:
        # Cria o áudio em português ('pt')
        tts = gTTS(text=texto_usuario, lang='pt', tld='com.br')
        tts.save(nome_arquivo)
        
        # Envia o arquivo como mensagem de voz no Telegram
        with open(nome_arquivo, 'rb') as audio:
            bot.send_voice(mensagem.chat.id, audio)
            
    except Exception as e:
        bot.reply_to(mensagem, "Desculpe, ocorreu um erro ao gerar o áudio.")
        print(f"Erro: {e}")
        
    finally:
        # Remove o arquivo temporário do seu computador após o envio
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)

bot.polling()
