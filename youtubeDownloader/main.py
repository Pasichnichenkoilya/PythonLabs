import os
import telebot
from YouTubeVideoDownloader import YouTubeVideoDownloader
from telebot.types import InputFile

bot = telebot.TeleBot('6125379497:AAGFLPJcYChg8KdbXxZfPuqRjny7J11Zba4')
yt_downloader = YouTubeVideoDownloader()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Paste a youtube video link to start downloading')


@bot.message_handler()
def try_download(message):
    url = message.text

    if yt_downloader.is_available(url):
        bot.send_message(message.chat.id, 'Download started, plase wait...')
    else:
        bot.send_message(message.chat.id, 'The url is wrong or video is unavailable')
        return

    path = yt_downloader.download(url)

    if os.path.exists(path):
        bot.send_video(message.chat.id, InputFile(path))
        os.remove(path)


print("Bot Started...")
bot.polling(non_stop=True)