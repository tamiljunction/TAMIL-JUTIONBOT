import asyncio
from telethon import TelegramClient, sync,events
from telethon.tl.functions.photos import DeletePhotosRequest
from . import *
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
@borg.on(admin_cmd(pattern=r"rmdp", outgoing=True))
@borg.on(sudo_cmd(pattern=r"rmdp$", allow_sudo=True))
async def _(event):
    pic = await borg.get_profile_photos('me')
    await borg(DeletePhotosRequest(pic))
    await event.edit("Done!!!")
CmdHelp("Remove dp").add_command(".rmdp", None, 'Romves dp')