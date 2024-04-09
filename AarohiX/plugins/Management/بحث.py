from AarohiX import app 
import requests as r
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import filters 

API_URL = "https://sugoi-api.vercel.app/search"

@app.on_message(filters.command("بحث", "ابحث"))
async def bing_search(dilop, message):
    try:
        if len(message.command) == 1:
            await message.reply_text("عن ماذا تبحث؟.")
            return

        keyword = " ".join(message.command[1:])
        params = {"keyword": keyword}
        response = r.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("لم يتم العثور على نتائج.")
            else:
                message_text = ""
                for result in results[:7]:
                    title = result.get("title", "")
                    link = result.get("link", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("عذرًا، حدث خطأ ما أثناء البحث.")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {str(e)}")
