from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""⬇️ nasıl kullanacağını öğretiyorum bı kerede anla⬇️
- `/oynat` la bebe /oynat yap çalsın uzatma
- `/bul` gardaş /bul şarkı adi yaz bulur.
- `/oynat` diğerinin aynısı
- `/atla` senin anlican diger şarkıya geçiyor
- `/bitir` müzik biter
- `/duraklat` durdurur
- `/devam` devam ettirir anlatırken yoruldum. 
- bilmem anladinmi.""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
          f"""⬇️ nasıl kullanacağını öğretiyorum bı kerede anla⬇️
- `/oynat` la bebe /oynat yap çalsın uzatma
- `/bul` gardaş /bul şarkı adi yaz bulur.
- `/oynat` diğerinin aynısı
- `/atla` senin anlican diger şarkıya geçiyor
- `/bitir` müzik biter
- `/duraklat` durdurur
- `/devam` devam ettirir anlatırken yoruldum. 
- Bilmem anladinmi.""")
