from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!
😁 I am KINGBOT Music Player. 
🥳 I can play music in your Telegram Group's Voice Chat😉
Developed by ⚡ @Sendenolmazbiyoll ⚡
My commands - /oynat, /bitir, /atla, /duraklat, /devam, which work in grp
Thanks for using .
Regrards [MAMAKLİBOT](https://t.me/Mamaklimusicbot)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 DEPLOY LINKİ🛠", url="vermicem😂😂😂")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Mamaklininmekani"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/mamaklichannnel"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ BENİ BİR GRUBA EKLE ➕", url="https://t.me/Mamaklimusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐ ARTIK BABANIZ AKTİF⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Mamaklichannnel")
                ]
            ]
        )
   
