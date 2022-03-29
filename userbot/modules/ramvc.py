import asyncio
from pytgcalls.methods.groups import JoinGroupCall
from pytgcalls import StreamType as ya
from pytgcalls.types.input_stream import AudioPiped as rambot
from pytgcalls.exceptions import (
    NoActiveGroupCall as memek,
    AlreadyJoinedError as asu,
    NotInGroupCallError as ajg
)
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest as ngentod
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import call_py
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as boy
from userbot.events import register as ok

from userbot.utils.queues.queues import clear_queue

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"



# credits by @vckyaz < vicky \>
# FROM GeezProjects < https://github.com/vckyou/GeezProjects \>
# ambil boleh apus credits jangan ya ka:)

@boy(pattern="joinvc(?: |$)(.*)")
@ok(pattern=r"^\.jvc(?: |$)(.*)", sudo=True)
async def join_(event):
    star = await edit_or_reply(event, f"**Otw Naik os, Sapa tau ada giveaway.**")
    if len(event.text.split()) > 1:
        chat = event.chat_id
        chats = event.pattern_match.group(1)
        try:
            chat = await event.client(ngentod(chats))
        except asu as e:
            await call_py.leave_group_call(chat)
            clear_queue(chat)
            await asyncio.sleep(3)
            return await edit_delete(event, f"**ERROR:** `{e}`", 30)
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return await edit_or_reply(event, "NodeJs is not installed or installed version is too old.")
    else:
        chat_id = event.chat_id
        chats = event.pattern_match.group(1)
        from_user = vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat_id,
        rambot(
            'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
        ),
        chats,
        stream_type=ya().pulse_stream,
    )
    await star.edit(f"**{from_user} Ngentot Naik Os!**")


@boy(pattern="leavevc(?: |$)(.*)")
@ok(pattern=r"^\.lvc(?: |$)(.*)", sudo=True)
async def leavevc(event):
    """ leave video chat """
    geezav = await edit_or_reply(event, "Processing")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (memek, ajg):
            await edit_or_reply(event, f"{from_user} Tidak Berada Di VC Group.")
        await geezav.edit(f"**{from_user} Berhasil Turun Dari VC Group.**")

CMD_HELP.update(
    {
        "vcplugin": f"**Plugin : **`vcplugin`\
        \n\n  •  **Syntax :** `{cmd}play` <Judul Lagu/Link YT>\
        \n  •  **Function : **Untuk Memutar Lagu di voice chat group dengan akun kamu\
        \n\n  •  **Syntax :** `{cmd}vplay` <Judul Video/Link YT>\
        \n  •  **Function : **Untuk Memutar Video di voice chat group dengan akun kamu\
          "
    }
)
