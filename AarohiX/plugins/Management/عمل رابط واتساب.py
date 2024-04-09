from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app 

@app.on_message(filters.command("واتساب", ""))
async def generate_whatsapp_link(client, message: Message):
    if len(message.command) < 2:
        await message.reply("الرجاء إدخال رقم هاتفك بعد الأمر. مثال: واتساب +1234567890")
        return

    phone_number = message.command[1]

    whatsapp_link = f"https://wa.me/{phone_number}"

    await message.reply(f"انقر على الرابط لفتح الواتس اب بالرقم {phone_number}:\n{whatsapp_link}")
