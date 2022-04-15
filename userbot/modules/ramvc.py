from pytgcalls import StreamType as kontol
from pytgcalls.exceptions import (
    AlreadyJoinedError as memek,
)

from pytgcalls.types.input_stream import (
    InputStream as ngentod,
    InputAudioStream as bego,
)
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest as babi
from telethon.tl.functions.channels import GetFullChannelRequest as kentod
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import call_py as sayang
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as tod

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call

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
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            await ede(event, f"**ERROR:** `{e}`", 30)
    else:
        chat_id = event.chat_id
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await sayang.join_group_call(
                chat_id,
                ngentod(
                bego(
                    './userbot/utils/resoure/SEPI.mp3'
                ),
            ),
            stream_type=kontol().local_stream,
            )
            await ede(event, f"⚝ **{from_user} Berhasil Join Obrolan Suara**\n**┗ Chat ID: {chat_id}**")
        except memek:
            await ede(
                rambot,
                f"**ERROR:** `Akun Anda Sudah Berada Di Obrolan Suara!`",
                10,
            )
        except Exception:
            await eor(event, "`Ga ada obrolan suara Ngentot!!!`")

@tod(pattern="lvc(?: |$)(.*)")
async def leavevc(event):
    await eor(event, "`Saatnya Turun...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(babi(chat_id))
        except Exception as e:
            return await ede(event, f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await sayang.leave_group_call(chat_id)
            await ede(
                event,
                f"⚝ {from_user} Berhasil Turun Dari Obrolam Suara!\n┗ Chat ID : {chat_id}", 5
            )
        except Exception as e:
            await eor(event, f"**INFO:** `{e}`")
