from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["المطور", "السورس", "المبرمج"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/17eb3640be82fc02d1b91.jpg",
        caption="• ხ᥆ƚ ძᥱ᥎ᥱᥣ᥆ρᥱᖇ 🇵🇸 \n ━━━━━━━━━━━━ \n •  . ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ძᥱ᥎ᥣ᥆ρᥱᖇ 🇵🇸", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗖𝗛 🇵🇸", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
