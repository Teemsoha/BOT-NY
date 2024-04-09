import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather


@app.on_message(
    command(["بايو","البايو"])
    & filters.group
    & ~filters.edited
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
@app.on_message(
    command(["شخصيتي", "معلوماتي", "شخصية"])
    & filters.group
    & ~filters.edited
)
async def ppdi(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• أنـت »   {message.from_user.mention()} لبيـه يا حلـو 🤍**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
 
 
 
@app.on_message(command(["تحويل الصوره", "تحويل الصورة"]))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("↢ يجب عليك الرد على المُلصق.")
    if not reply.sticker:
        return await message.reply("↢ يجب عليك الرد على المُلصق.")
    m = await message.reply("↢ يتم المُعالجـة....")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



@app.on_message(command(["المجموعة", "الجروب"]) & filters.group & ~filters.edited)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**↢ اسم المجموعة : {chat_name}\n↢ أيدي المجموعـة :  -{chat_idd}\n↢ رابط المجموعة : {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    
