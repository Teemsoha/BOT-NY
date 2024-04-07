
 ###### ###### ###### #####   ################
   ##   ##       ##  ##   ##  #######
   ##   ##       ##  ##   ##  ###########
   ##   #####    ##  ##   ##  #########
   ##   ##       ##  ##   ##  ############
   ##   ##       ##  ##   ##  #####𝗔𝗵𝗺𝗲𝗱 𝗧𝗲𝘁𝗼
   ##   ######   ##   ##### ################


from pyrogram import Client, filters, idle
from pyrogram import Client
import requests
from AarohiX import app

async def get_prayer_times(address, method, school):
    url = f"http://api.aladhan.com/timingsByAddress?address={address}&method={method}&school={school}"
    response = requests.get(url)
    data = response.json()
    return data["data"]["timings"]

@app.on_message(filters.command(["اوقات الصلاة"], ""))
async def get_times(client, message):
        address = "Cairo"
        method = 4  
        school = 0  
        prayer_times = await get_prayer_times(address, method, school)

        times_message = f"↢ أوقـاتُ الصلاة فـي {address} 🕌:\n"
        times_message += f"الفجر: {prayer_times['Fajr']}\n"
        times_message += f"الشروق: {prayer_times['Sunrise']}\n"
        times_message += f"الظهر: {prayer_times['Dhuhr']}\n"
        times_message += f"العصر: {prayer_times['Asr']}\n"
        times_message += f"المغرب: {prayer_times['Maghrib']}\n"
        times_message += f"العشاء: {prayer_times['Isha']}\n"

        await message.reply_text(times_message)


 ###### ###### ###### #####   ################
   ##   ##       ##  ##   ##  #######
   ##   ##       ##  ##   ##  ###########
   ##   #####    ##  ##   ##  #########
   ##   ##       ##  ##   ##  ############
   ##   ##       ##  ##   ##  #####𝗔𝗵𝗺𝗲𝗱 𝗧𝗲𝘁𝗼
   ##   ######   ##   ##### ################
