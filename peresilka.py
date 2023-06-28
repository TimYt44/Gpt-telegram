.exec
from telethon import types
from .. import utils
async for msg in client.iter_messages(<5835402883>,
         reverse=True): 
    await client.forward_messages(<1980194086>, msg)