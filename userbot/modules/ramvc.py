from pytgcalls import StreamType as kontol

from pytgcalls.types.input_stream import (
    InputAudioStream as bego,
)
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import GetGroupCallRequest as getvc

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
@register(pattern=r"^\.cjvc(?: |$)(.*)", sudo=True)
async def _(event):
    Man = await eor(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Man.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        file = "./userbot/resources/SEPI.mp3"
        try:
            await sayang.join_group_call(
                chat_id,
                ngentot(
                    bego(
                        file,
                    ),
                ),
                stream_type=kontol().local_stream,
            )
            await Man.edit(
                f"❏ **Berhasil Join Ke Obrolan Suara**\n└ **Chat ID:** `{chat_id}`"
            )
        except AlreadyJoinedError:
            return await ede(
                Man, "**INFO:** `akun anda sudah berada di obrolan suara`", 45
            )
        except Exception as e:
            return await Man.edit(f"**INFO:** `{e}`")


@man_cmd(pattern="lvc(?: |$)(.*)")
@register(pattern=r"^\.clvc(?: |$)(.*)", sudo=True)
async def vc_end(event):
    Man = await eor(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Man.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        try:
            await sayang.leave_group_call(chat_id)
            await ede(
                Man,
                f"❏ **Berhasil Turun dari Obrolan Suara**\n└ **Chat ID:** `{chat_id}`",
            )
        except Exception as e:
            return await Man.edit(f"**INFO:** `{e}`")
