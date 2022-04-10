# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import time
from datetime import datetime
from random import choice, randint

from telethon.events import StopPropagation
from telethon.tl.functions.account import UpdateProfileRequest

from userbot import AFKREASON, BOTLOG_CHATID, PM_AUTO_BAN, bot, owner
from userbot.events import ram_cmd, register

# ========================= CONSTANTS ============================
AFKSTR = [
    f"! 𝗔𝗙𝗞 🐨\n╭✠╼━━━━━━━━━━━━ \n┣ {owner} 𝐋𝐚𝐠𝐢 𝐍𝐆𝐄𝐍𝐓𝐎𝐓\n╰✠╼━━━━━━━━━",
    f"! 𝗔𝗙𝗞 🐨\n╭✠╼━━━━━━━━━━━━ \n┣ {owner} 𝐋𝐚𝐠𝐢 𝐍𝐆𝐄𝐍𝐓𝐎𝐓\n╰✠╼━━━━━━━━━",
    f"! 𝗔𝗙𝗞 🐨\n╭✠╼━━━━━━━━━━━━ \n┣ {owner} 𝐋𝐚𝐠𝐢 𝐍𝐆𝐄𝐍𝐓𝐎𝐓\n╰✠╼━━━━━━━━━",
    f"! 𝗔𝗙𝗞 🐨\n╭✠╼━━━━━━━━━━━━ \n┣ {owner} 𝐋𝐚𝐠𝐢 𝐍𝐆𝐄𝐍𝐓𝐎𝐓\n╰✠╼━━━━━━━━━",
]
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@bot.on(ram_cmd(outgoing=True, pattern=r"off(?: |$)(.*)"))
async def set_afk(afk_e):
    """For .afk command, allows you to inform people that you are afk when they message you"""
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await bot.get_me()
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\n{owner} Sibuk Dulu Gaes...\
        \n𝘼𝙡𝙖𝙨𝙖𝙣: `{string}`\n╰✠╼━━━━━━❖━━━━━━━✠╯")
    else:
        await afk_e.edit(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\n{owner} Sibuk Dulu Kawan, Udah Ange berat...\n╰✠╼━━━━━━❖━━━━━━━✠╯")
    if user.last_name:
        await afk_e.client(
            UpdateProfileRequest(
                first_name=user.first_name, last_name=user.last_name + "【 •𝗕𝗨𝗦𝗬• 】"
            )
        )
    else:
        await afk_e.client(
            UpdateProfileRequest(first_name=user.first_name, last_name="【 •𝗕𝗨𝗦𝗬• 】")
        )
    if BOTLOG_CHATID:
        await afk_e.client.send_message(BOTLOG_CHATID, f"#OFF\n**{owner} SIBUK BERAT!**")
    ISAFK = True
    afk_time = datetime.now()
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """This sets your status as not afk automatically when you write something while being afk"""
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await bot.get_me()
    last = user.last_name
    if last and last.endswith("【 •𝗕𝗨𝗦𝗬• 】"):
        last1 = last[:-12]
    else:
        last1 = ""
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond(f"**{owner} Kembali! Kangen gak?**")
        time.sleep(7)
        await msg.delete()
        await notafk.client(
            UpdateProfileRequest(first_name=user.first_name, last_name=last1)
        )
        if BOTLOG_CHATID:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Anda Mendapatkan "
                + str(COUNT_MSG)
                + " Pesan Dari "
                + str(len(USERS))
                + " Obrolan Pas Lu lagi Sibuk!",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "["
                    + name0
                    + "](tg://user?id="
                    + str(i)
                    + ")"
                    + " Mengirim Mu "
                    + "`"
                    + str(USERS[i])
                    + " Pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**𝙏𝙚𝙧𝙖𝙠𝙝𝙞𝙧 𝙊𝙣𝙡𝙞𝙣𝙚**"
    if mention.message.mentioned and not (await mention.get_sender()).bot and ISAFK:
        now = datetime.now()
        datime_since_afk = now - afk_time
        time = float(datime_since_afk.seconds)
        days = time // (24 * 3600)
        time %= 24 * 3600
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        if days == 1:
            afk_since = "**𝙆𝙚𝙢𝙖𝙧𝙞𝙣**"
        elif days > 1:
            if days > 6:
                date = now + datetime.timedelta(
                    days=-days, hours=-hours, minutes=-minutes
                )
                afk_since = date.strftime("%A, %Y %B %m, %H:%I")
            else:
                wday = now + datetime.timedelta(days=-days)
                afk_since = wday.strftime("%A")
        elif hours > 1:
            afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
        elif minutes > 0:
            afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
        else:
            afk_since = f"`{int(seconds)} Detik`"
        if mention.sender_id not in USERS:
            if AFKREASON:
                await mention.reply(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\n{owner} Sibuk gaes **\nLama 𝗔𝗙𝗞 : {afk_since}.\
                        \n𝘼𝙡𝙖𝙨𝙖𝙣: `{AFKREASON}`\n╰✠╼━━━━━━❖━━━━━━━✠╯")
            else:
                await mention.reply(str(choice(AFKSTR)))
            USERS.update({mention.sender_id: 1})
        else:
            if USERS[mention.sender_id] % randint(2, 4) == 0:
                if AFKREASON:
                    await mention.reply(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\n{ALIVE_NAME} Masih Sibuk banget Brader **\nLama 𝗔𝗙𝗞 : {afk_since}.\
                            \n𝘼𝙡𝙖𝙨𝙖𝙣: `{AFKREASON}`\n╰✠╼━━━━━━❖━━━━━━━✠╯")
                else:
                    await mention.reply(str(choice(AFKSTR)))
            USERS[mention.sender_id] = USERS[mention.sender_id] + 1
        COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """Function which informs people that you are AFK in PM"""
    global ISAFK
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**𝗕𝗲𝗹𝘂𝗺 𝗟𝗮𝗺𝗮**"
    if (
        sender.is_private
        and sender.sender_id != 777000
        and not (await sender.get_sender()).bot
    ):
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved

                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time %= 24 * 3600
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**𝙆𝙚𝙢𝙖𝙧𝙞𝙣**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime("%A")
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\nMohon Maaf `{owner}` Lagi Sibuk! Jangan Batu deh...**\nLama 𝗔𝗙𝗞 : {afk_since}.\
                        \n𝘼𝙡𝙖𝙨𝙖𝙣: `{AFKREASON}`\n╰✠╼━━━━━━❖━━━━━━━✠╯")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"**! 𝗔𝗙𝗞  🐨**\n╭✠╼━━━━━━❖━━━━━━━✠╮\nMohon Maaf `{owner}` Lagi Sibuk...**\nLama 𝗔𝗙𝗞 : {afk_since}.\
                        \n𝘼𝙡𝙖𝙨𝙖𝙣: `{AFKREASON}`\n╰✠╼━━━━━━❖━━━━━━━✠╯")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                COUNT_MSG = COUNT_MSG + 1
