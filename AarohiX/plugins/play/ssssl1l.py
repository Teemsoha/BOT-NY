"""
-------------------------------------
- Copyright (©️) 2024-4-28
- Writen by T.me/programer_senzir
- Ch, T.me/Tepthon
-------------------------------------
"""
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

#»ꫝ 𝘿𝙀𝙑 𝙎𝙀𝙉𝙕𝙄𝙍 ℡ 🝁« 𝟭𝟲𝐊@app.on_message(filters.command("رتبتي", ""))
async def rotba(_: Client, message: Message):
    user_id = message.from_user.id 
    member = await app.get_chat_member(message.chat.id ,user_id)
    if member.status == ChatMemberStatus.MEMBER: return await message.reply("- رتبتك هي العضو.", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.ADMINISTRATOR: return await message.reply("- رتبتك هي الادمن.", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.OWNER: return await message.reply("- رتبتك هي المالك.", reply_to_message_id=message.id)
    
    print("»ꫝ 𝘿𝙀𝙑 𝙎𝙀𝙉𝙕𝙄𝙍 ℡ 🝁« 𝟭𝟲𝐊")