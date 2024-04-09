from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from AarohiX import app
from config import OWNER_ID
from pyrogram.types import Message
from AarohiX.utils.admin_check import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(["تثبيت", "تثبيت المسدج"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("↢ وخر، ما يمديك تستخدم هالميزة بس في المجموعات.")
    elif not replied:
        await message.reply_text("↢ أبشر ثبتت الرسالة\n\n ༄")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"↢ أبشر ثبتت الرسالة\n\n ༄", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرساله 📝", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("↢ ما في رسالة مُثبتة\n\n ༄")
    try:        
        await message.reply_text("↢ قائمة الرسائل المثبتة",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 عرض الرسالة",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء تثبيت"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("↢ وخر، ما يمديك تستخدم هالميزة بس في المجموعات.")
    elif not replied:
        await message.reply_text("↢ رد على الرسالة عشان يمديني ألغي تثبيتها")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"↢ أبشر لغيت تثبيت الرسالة\n\n༄", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرساله 📝", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ғʀᴏᴍ ɢʀᴏᴜᴘ !\nʙʏ** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**ᴛʜᴇ ᴜsᴇʀ ᴍᴏsᴛ ɴᴇᴇᴅ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ʀᴇᴍᴏᴠᴇ ɢʀᴏᴜᴘ ᴘʜᴏᴛᴏ !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("وضع صورة")& admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("↢ جاري...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("↢ وخر، هذا الأمر يشتغل بالمجموعات.") 
      elif not reply:
           await msg.edit("↢ رُد على الصورة لوضعها.")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("↢ أبشر غيرت صورة المجموعة\nمن : {}\n\n༄".format(message.from_user.mention))
             else:
                await msg.edit("↢ صار فيه خطأ جرب صورة ثانية\n\n༄")
     
          except:
              await msg.edit("↢ أعطيني صلاحية تغيير معلومات المجموعة\n\n༄")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("وضع اسم")& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("جاري...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("↢ هذا الأمر ما يشتغل إلّا بالمجموعات\n\n ༄")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("↢ أبشر غيرت اسم المجموعة\nمن {}\n\n༄".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("↢ أعطيني صلاحية تغيير معلومات المجموعة\n\n༄")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("↢ أبشر غيرت اسم المجموعة\nمن {}\n\n༄".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**↢ أحتاج إلى صلاحية تعديل معلومات المجموعة.**")
          

    else:
       await msg.edit("↢ رد على كلمة؛ لكي أضعها اسمًا للمجموعة.")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("وضع وصف") & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("جاري...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("↢ وخر، هذا الأمر ما يشتغل إلّا بالمجموعات.")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("↢ أبشر غيرت وصف المجموعة\nمن {}\n\n༄".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("↢ أحتاج إلى صلاحية تعديل معلومات المجموعة؛ لكي أغير وصف المجموعة")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("↢ أبشر غيرت وصف المجموعة\nمن {}\n\n༄".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("↢ أحتاج إلى صلاحية تعديل معلومات المجموعة")
    else:
        await msg.edit("*رد على اسم؛ عشان أحطه وصف\n\n༄*")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["غادر", "فهد غادر"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "↢ تم غادرت مطوري\n\n༄"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    await delete_served_chat(chat_id)


# --------------------------------------------------------------------------------- #

