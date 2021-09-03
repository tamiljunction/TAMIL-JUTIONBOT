
import asyncio
import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply, progress
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify

@bot.on(admin_cmd(pattern="lyri(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lyri(?: |$)(.*)", allow_sudo=True))
async def nope(legend):
    LEGEND = legend.pattern_match.group(1)
    if not LEGEND:
        if legend.is_reply:
            (await legend.get_reply_message()).message
        else:
            await legend.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(LEGEND))}")

    await troll[0].click(
        legend.chat_id,
        reply_to=legend.reply_to_msg_id,
        silent=True if legend.is_reply else False,
        hide_via=True,
    )

    await legend.delete()

#>>>>>>>>>>>>>>>>>>✓✓✓✓✓<<<<<<<<<<<<<<<<<<<

@bot.on(admin_cmd(pattern="gaana ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gaana ?(.*)", allow_sudo=True))
async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit(
                "```Please unblock``` @FindmusicpleaseBot``` and try again```"
            )

            return

        await gaana.edit("`Sending Your Music...wait!!! 😉😎`")

        await bot.send_file(gaana.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()


# -------------------------------------------------------------------------------




# -------------------------------------------------------------------------------
import os
from telethon.tl.functions.channels import JoinChannelRequest

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)



@bot.on(admin_cmd(pattern="getsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="getsong(?: |$)(.*)", allow_sudo=True))
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/anitimeofficial"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await edit_or_reply(so, "🔹Ok wait... 📡Searching your song🔸")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await edit_or_reply(so, "📥Downloading...Please wait🤙")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(so, "Please unblock @SongsForYouBot and try searching again🤐")
            return
        await edit_or_reply(so, "Ohh.. I got something!! Wait sending😋🤙")
        await asyncio.sleep(3)
        await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await so.delete()


# -------------------------------------------------------------------------------

import asyncio
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@bot.on(admin_cmd(pattern="dwlsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="dwlsong(?: |$)(.*)", allow_sudo=True))
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await edit_or_reply(Deezlod, "` I need a link to download something pro.`**(._.)**")
    else:
        await edit_or_reply(Deezlod, "**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(Deezlod, "**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await bot.send_file(Deezlod.chat_id, song, caption=details.text)
        await Deezlod.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )
        await Deezlod.delete()


# -------------------------------------------------------------------------------


from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest


@bot.on(admin_cmd(pattern="sdd ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="sdd?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezLoadBot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            try:
                await borg(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            await borg.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await borg.send_file(
                event.chat_id,
                songh,
                caption="🔆**Here's the requested song!**🔆\n`Check out` [LEGENDBOT](https://t.me/LEGENDSupport)",
            )
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
CmdHelp("songs").add_command(
  "song", "<song name>", "Searches the song from youtube and upload in current chat in audio(.mp3) format. •Highest Quality"
).add_command(
  "vsong", "<song name>", "Searches the song from youtube and upload in current chat in video(.mp4) format. •Highest Quality"
).add_command(
  "getsong", "<song name>", "Searches song from a local tg bot @Songsforyoubot and sends the music in current chat"
).add_command(
  "gaana", "<song name>", "Searches song from a local tg bot @FindmusicpleaseBot and sends the music in current chat"
).add_command(
  "sdd", "<song link>", "Downloads the song from given link"
).add_command(
  "dwlsong", "<song link>", "Same as .sdd but downloads from spotify and deezer"
).add_command(
  "lyri", "<song name>", "Sends the lyrics of given song."
).add()
