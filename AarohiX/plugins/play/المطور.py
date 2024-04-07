from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/8623fdb7fd5bb7349bb3f.jpg",
        caption="• Dev Bot ↦ 𝖬𝗈𝗁𝖺𝗆𝗆𝖺𝖽 🇵🇸 \n ━━━━━━━━━━━━ \n • Dev ↦ @PPF22 . ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝖬𝗈𝗁𝖺𝗆𝗆𝖺𝖽 🇵🇸", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🇵🇸", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
