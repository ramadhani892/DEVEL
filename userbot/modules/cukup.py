from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import register
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import ram_cmd, edit_or_reply as babi

# Aku nambah kredit sdikit
# rama ganteng bgt kan?
# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits


@ram_cmd(pattern="allout$")
@register(pattern="^\.callout$", sudo=True)
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await babi(event, "Lu bukan admin, NGENTOOOOTTTTTT!!")
        return
    await babi(event, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await babi(event, str(e))
        await sleep(.5)
    await babi(event, "Tidak Ada yang Terjadi di sini🙃🙂")

CMD_HELP.update(
    {
        "cukup": f"**Plugin : **`cukup`\
    \n\n**Syntax : **`{cmd}allout`\
    \n**Function : **ban all members in 1 comand"
    }
)
