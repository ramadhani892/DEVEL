import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights
from userbot import BOTLOG_MSG
from userbot import BOTLOG_CHATID
from userbot import bot, tgbot
from userbot.utils hadeh_ajg


async def ram_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = RamUbot.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = RamUbot.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await hadeh_ajg(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"{BOTLOG_MSG},
                )
    except BaseException:
        pass
    try:
        if RAM2:
            await hadeh_ajg(RAM2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RAM2.send_message(
                    BOTLOG_CHATID,
                    f"{BOTLOG_MSG},
                )
    except BaseException:
        pass
    try:
        if RAM3:
            await hadeh_ajg(RAM3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RAM3.send_message(
                    BOTLOG_CHATID,
                    f"{BOTLOG_MSG},
                )
    except BaseException:
        pass
    try:
        if RAM4:
            await checking(RAM4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RAM4.send_message(
                    BOTLOG_CHATID,
                    f"{BOTLOG_MSG},
                )
    except BaseException:
        pass
    try:
        if RAM5:
            await checking(RAM5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RAM5.send_message(
                    BOTLOG_CHATID,
                    f"{BOTLOG_MSG}
                )
    except BaseException:
        pass
