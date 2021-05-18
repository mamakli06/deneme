from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("duraklat") & other_filters)
@errors
@authorized_users_only
async def duraklat(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: valla mal bilmiyon sen!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: ▶️ tamam iki dk sigara içip geleyim!!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: 😏 oynama la bi!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: ⏸ çalmaya devam mamakliya selam!")


@Client.on_message(command("bitir") & other_filters)
@errors
@authorized_users_only
async def bitir(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: 🙄 BOŞ YAPMA!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: ❌ AL İŞTE BİTTİ!")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**⭐ MAMAKLİBOT⭐**: ❗ ya mal ney atlim!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("**⭐ MAMAKLİBOT⭐**: ♂️ atladım dinlesen ne vardı!")
