import asyncio
import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply, progress
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify

@bot.on(admin_cmd(pattern="lyrics(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lyrics(?: |$)(.*)", allow_sudo=True))
async def nope(aura):
    LEGEND = aura.pattern_match.group(1)
    if not LEGEND:
        if aura.is_reply:
            (await aura.get_reply_message()).message
        else:
            await aura.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(LEGEND))}")

    await troll[0].click(
        aura.chat_id,
        reply_to=aura.reply_to_msg_id,
        silent=True if aura.is_reply else False,
        hide_via=True,
    )

    await aura.delete()
