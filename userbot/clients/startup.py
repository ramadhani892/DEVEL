import sys

from telethon.utils import get_peer_id

from userbot import BOT_TOKEN
from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    RAM2,
    RAM3,
    RAM4,
    RAM5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    bot,
    call_py,
    tgbot,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\n✨ RAM - UBOT ✨ v{}, Copyright © 2021-2022 merdhani• <https://github.com/ramadhani892>"
MSG_BLACKLIST = "MAKANYA GA USAH BANYAK BAT LAGA LU KONTOL, MAMPUS BOT LU DI MATIIN KAN, LAPORKAN KESALAHAN KE @ramsupportt"


async def ram_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def ramulti():
    if 1883494460 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001692751821 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1883494460 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(ram_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))


    if STRING_2:
        try:
            RAM2.start()
            LOOP.run_until_complete(ram_client(RAM2))
            user = RAM2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            RAM3.start()
            LOOP.run_until_complete(ram_client(RAM3))
            user = RAM3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            RAM4.start()
            LOOP.run_until_complete(ram_client(RAM4))
            user = RAM4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            RAM5.start()
            LOOP.run_until_complete(ram_client(RAM5))
            user = RAM5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
