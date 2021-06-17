from typing import Text
from telethon import TelegramClient, sync, events
import json

with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)
api_id = config['login']['api_id']
api_hash = config['login']['api_hash']
with TelegramClient('session', api_id, api_hash) as client:
    @client.on(events.NewMessage())
    async def handler(event):
        for key in config['keys']:
            if key.lower() in event.message.raw_text.lower():
                await event.reply(config['message'])
    client.run_until_disconnected()