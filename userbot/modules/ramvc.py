from pytgcalls import StreamType as kontol
from pytgcalls.exceptions import AlreadyJoinedError as babi
from pytgcalls.types.input_stream import (
    InputAudioStream as memek, 
    InputStream as asu,
)
from userbot import call_py as goblok
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as tod

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
    ram = await eor(event, "**Hoi aku datang....**")
    if len(event.text.split()) > 1:
        chats = event.text.split()[1]
        try:
            chats = await event.client.get_peer_id(int(chats))
        except Exception as e:
            return await eor(event, f"**ERROR:** `{e}`")
    else:
        chats = event.chats
    if chats:
        file = "http://duramecho.com/Misc/SilentCd/Silence01s.mp3"
        try:
            await goblok.join_group_call(
                chats,
                asu(
                    memek(
                        file,
                    ),
                ),
                stream_type=kontol().local_stream,
            )
            await ede(ram,
                f"⚝ **{first_name} Berhasil Join Ke Obrolan Suara**\n┗ **Chat ID:** `{chats}`", 5
            )
        except babi:
            return await ede(
                ram, "**ERROR**: `Kayak Nya lo udh naik os Dah ngentod.`", 10
            )
        except Exception as e:
            return await ede(ram, f"**ERROR:** `{e}`", 10)


@tod(pattern="lvc(?: |$)(.*)")
@register(pattern=r"^\.clvc(?: |$)(.*)", sudo=True)
async def vc_end(event):
    await eor(event, "`Saatnya Pergi....`")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            await event.client.get_peer_id(int(chat))
        except Exception as e:
            return await ede(event, f"**ERROR:** `{e}`", 10)
    else:
        chatid = event.chats
    if chatid:
        try:
            await goblok.leave_group_call(chatid)
            await ede(
                ram,
                f"⚝ **Babay Anak anak Ngentod, {first_name} Turun dulu.**\n┗ **Chat ID:** `{chatid}`", 10
            )
        except Exception as e:
            return await ede(ram, f"**INFO:** `{e}`", 10)
