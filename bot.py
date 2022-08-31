from telethon.sync import TelegramClient
import asyncio
import sys

api_id = 18650979
api_hash = '80f326c75b6d4674b5078b2c875265df'
bot_token = '5558504790:AAGcoMGZ_6YbLUIv8CCrgpbgMFugV_N1Q68'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


# Entity - your telegram username or user id
async def send_message(msg, entity):
    await bot.send_message(entity, msg)

bot.start(bot_token=bot_token)
loop = asyncio.get_event_loop()
loop.run_until_complete(send_message(sys.argv[1], 'Example_name'))
