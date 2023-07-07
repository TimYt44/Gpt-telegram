from telethon.sync import TelegramClient, events


# Замените значения ниже ID чатов, из которых и в которые вы хотите пересылать сообщения
source_chat_id = 5835402883
destination_chat_id = 1980194086

with TelegramClient('session_name', api_id, api_hash) as client:
    @client.on(events.NewMessage(chats=source_chat_id))
    async def handler(event):
        message = event.message
        await client.send_message(destination_chat_id, message)

    client.run_until_disconnected()
