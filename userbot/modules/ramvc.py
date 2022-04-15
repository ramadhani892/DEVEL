from pytgcalls import StreamType
from pytgcalls.types.input_stream import (
    AudioPiped,
)
from pytgcalls.exceptions import (
    AlreadyJoinedError,
)

from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot import CMD_HANDLER as cmd
from userbot import call_py
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as tod
async def get_call(event):
    call = await event.client(GetFullChannelRequest(event.chat.id))
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
    rambot = await eor(event, f"**Processing**")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client(GetFullUserRequest(chat_id))
        except Exception as e:
            await ede(rambot, f"**ERROR:** `{e}`", 30)
    else:
        chat_id = event.chat_id
        await event.get_chat()
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                AudioPiped(
                    'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
                ),
            stream_type=StreamType().pulse_stream,
            )
            await ede(rambot, f"**{from_user} Berhasil Naik Ke VC Group!**")
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await ede(
                rambot,
                f"**ERROR:** `Akun Anda Sudah Berada Di VC Group!`\n\n**Noted :** __Silahkan Ketik__ `{cmd}joinvc` __untuk menggunakan command kembali.__",
                30,
            )
        except Exception as e:
            await geezav.edit(f"**INFO:** `{e}`")

@tod(pattern="lvc(?: |$)(.*)")
async def leavevc(event):
    rambot = await eor(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client(GetFullUserRequest(chat_id))
        except Exception as e:
            return await ede(rambot, f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await ede(
                rambot,
                f"{from_user} Berhasil Turun Dari VC Group!",
            )
        except Exception as e:
            await eor(event, f"**INFO:** `{e}`")
