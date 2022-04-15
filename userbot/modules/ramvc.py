from pytgcalls import StreamType as kontol
from pytgcalls.types.input_stream import (
    AudioPiped as asu,
)
from pytgcalls.exceptions import (
    AlreadyJoinedError as memek,
)

from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest as babi
from telethon.tl.functions.channels import GetFullChannelRequest as kentod

from userbot import CMD_HANDLER as cmd
from userbot import call_py as sayang
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as tod
async def get_call(event):
    call = await event.client(kentod(event.chat.id))
    return call.full_chat.call

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"

eor = edit_or_reply
ede = edit_delete

# credits by @vckyaz < vicky \>
# recode by @lahsiajg < starboy \>

@tod(pattern="jvc(?: |$)(.*)")
async def join_(event):
    await eor(event, f"**Hoi Aku datang....**")
    if len(event.text.split()) > 1:
        chatid = event.text.split()[1]
        try:
            chats = await event.client(babi(chatid))
        except Exception as e:
            await ede(event, f"**ERROR:** `{e}`", 30)
    else:
        chatin = event.chats
        await event.get_chat()
        from_user = vcmention(event.sender)
    if chatin:
        try:
            await sayang.join_group_call(
                chatin,
                AudioPiped(
                    'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
                ),
            stream_type=kontol().pulse_stream,
            )
            await ede(event, f"⚝ **{from_user} Berhasil Join Obrolan Suara**\n**┗ Chat ID: {chatin}")
        except memek:
            await sayang.leave_group_call(chatin)
            await ede(
                rambot,
                f"**ERROR:** `Akun Anda Sudah Berada Di Obrolan Suara!`\n\n**Noted :** __Silahkan Ketik__ `{cmd}jvc` __Untuk Naik kembali.__",
                10,
            )
        except Exception as e:
            await eor(event, f"**INFO:** `{e}`")

@tod(pattern="lvc(?: |$)(.*)")
async def leavevc(event):
    await eor(event, "`Saatnya Turun...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client(babi(chat_id))
        except Exception as e:
            return await ede(event, f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await ede(
                event,
                f"⚝ {from_user} Berhasil Turun Dari Obrolam Suara!\n┗ Chat ID : {chat_id}", 5
            )
        except Exception as e:
            await eor(event, f"**INFO:** `{e}`")
