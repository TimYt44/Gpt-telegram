from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from asyncio.exceptions import TimeoutError
import time

def register(cb):
    cb(KKTextMod())

class KKTextMod(loader.Module):
    """K&K Text by @ktxtBot"""
    strings = {'name': 'GPTofTim'}

    async def gptcmd(self, message):
        """Используйте .gpt <текст или реплай>."""
        try:
            text = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            chat = "@GPT4Telegrambot"
            if not text and not reply:
                await message.edit("<b>Нет текста или реплая.</b>")
                return
            if text:
                await message.edit("<b>Минуточку...</b>")
                async with message.client.conversation(chat) as conv:
                    try:
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=5896221213))
                        await message.client.send_message(chat, text)
                        response = await response
                    except YouBlockedUserError:
                        await message.reply("<b>Разблокируй бота @GPT4Telegrambot.</b>")
                        return
                    if not response.text:
                        await message.edit("<Бот ответил не текстовым форматом, попробуйте ещё раз.</b>")
                        return
                    await message.delete()
                    await message.client.send_message(message.to_id, response.text)
            if reply:
                await message.edit("<b>Минуточку...</b>")
                async with message.client.conversation(chat) as conv:
                    try:
                        
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=5896221213))
                        time.sleep(30)
                        response2 = conv.wait_event(events.NewMessage(incoming=True, from_users=5896221213))
                        
                        await message.client.send_message(chat, reply)
                      
                        response2 = await response2
                    except YouBlockedUserError:
                        await message.reply("<b>Разблокируй бота @GPT4Telegrambot.</b>")
                        return
                    if not response2.text:
                        await message.edit("<Бот ответил не текстовым форматом, попробуйте ещё раз.</b>")
                        
                        return
                    await message.delete()
                    await message.client.send_message(message.to_id, response2.text)
        except TimeoutError:
            return await message.edit("<b>Истекло время ожидания. Либо бот сдох, либо текст слишком большой, и бот не отвечает.</b>")