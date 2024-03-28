import os

from aiogram import *
from config import *
from pytube import YouTube
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'bot started')

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt= YouTube(url=url)
    if message.text.startswith == 'htts://youtube.com' or 'http://www.youtu.be.com':
        await bot.send_message(chat_id,f'Starting dowloading video : {yt.title}'
                               f'from channel {yt.author }, {yt.channel_url}')

async def video_message(url , message , bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}' f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='This your video *', parse_mode='Markdown')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')


if __name__ == '__main__':
    executor.start_polling(dp)